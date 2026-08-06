#!/usr/bin/env python3
"""
make_transparent_svg.py — turn a photo with a plain (studio) background into a
background-removed, transparent SVG (the raster cutout is embedded as a PNG
data-URI inside the SVG).

This is the tool used to build img/avatar.svg for this CV site from a B&W
studio portrait. It needs no ML model: when the subject sits on a roughly
uniform background, the background is the set of light/dark pixels that are
connected to the image border, so a connected-component key mattes it cleanly.

Usage
-----
    python3 make_transparent_svg.py INPUT.png -o OUTPUT.svg [options]

Common examples
    # B&W portrait on a light studio bg (what we used for the avatar):
    python3 make_transparent_svg.py photo.png -o ../../img/avatar.svg --gray

    # keep full colour, also drop the intermediate cutout PNG next to the SVG:
    python3 make_transparent_svg.py photo.jpg -o out.svg --keep-png

Options
    -o/--output      output .svg path (required)
    --bg auto|light|dark   which background to remove (default: auto from corners)
    --threshold N    luminance cutoff 0-255 (default: auto = corner mean -/+ 40)
    --max-width N    downscale embedded image to this width (default: 560)
    --gray           store as grayscale+alpha (much smaller for B&W photos)
    --pad N          transparent padding kept around the subject, px (default: 20)
    --feather N      edge feather blur radius, px (default: 1.1)
    --keep-png       also write the trimmed cutout as a sibling .png

Dependencies: numpy, scipy, pillow  (see requirements.txt)
"""
import argparse
import base64
import io
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def detect_background(lum: np.ndarray, mode: str) -> tuple[str, float]:
    """Return ('light'|'dark', threshold).

    Auto-detection samples the TWO TOP corners plus the top edge: for a
    portrait/headshot the background sits above and behind the subject, whereas
    the bottom corners are usually the body (which may be dark, e.g. a hoodie)
    and would otherwise fool a four-corner mean.
    """
    h, w = lum.shape
    c = max(8, min(h, w) // 40)
    top = np.concatenate([
        lum[:c, :c].ravel(),        # top-left corner
        lum[:c, -c:].ravel(),       # top-right corner
        lum[:c, :].ravel(),         # whole top edge
    ])
    bg_lum = float(np.median(top))
    if mode == "light" or (mode == "auto" and bg_lum >= 128):
        return "light", bg_lum - 40
    return "dark", bg_lum + 40


def build_alpha(lum: np.ndarray, bg_kind: str, thresh: float, feather: float) -> np.ndarray:
    """Connected-component key -> feathered 0..255 alpha for the subject."""
    bg_like = lum > thresh if bg_kind == "light" else lum < thresh

    # background = bg-like pixels connected to the image border
    lab, _ = ndimage.label(bg_like)
    border = set(np.unique(np.concatenate(
        [lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]])))
    border.discard(0)
    bg = np.isin(lab, list(border))

    fg = ndimage.binary_fill_holes(~bg)          # keep trapped holes (e.g. lenses)

    # erode 1px to kill the bg halo, then feather for an anti-aliased edge
    hard = (ndimage.binary_erosion(fg, iterations=1).astype(np.uint8)) * 255
    a = np.asarray(Image.fromarray(hard, "L")
                   .filter(ImageFilter.GaussianBlur(feather))).astype(np.float32) / 255.0

    # graded transparency in the transition band: only pull alpha down where the
    # pixel actually looks like background, so stray fringes fade out softly
    lo, hi = thresh, thresh + (35 if bg_kind == "light" else -35)
    if bg_kind == "light":
        grade = np.clip((hi - lum) / (hi - lo), 0, 1)      # 1 dark(keep)..0 light
    else:
        grade = np.clip((lum - hi) / (lo - hi), 0, 1)
    a = a * (0.35 + 0.65 * grade)

    a[ndimage.binary_erosion(fg, iterations=6)] = 1.0      # solid interior stays opaque
    return (np.clip(a, 0, 1) * 255).astype(np.uint8)


def make_svg(png_bytes: bytes, w: int, h: int, label: str) -> str:
    b64 = base64.b64encode(png_bytes).decode()
    uri = f"data:image/png;base64,{b64}"
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
        f'aria-label="{label}">'
        f'<image width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" '
        f'href="{uri}" xlink:href="{uri}"/></svg>'
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Photo -> transparent SVG (bg removed).")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", required=True, help="output .svg path")
    ap.add_argument("--bg", choices=["auto", "light", "dark"], default="auto")
    ap.add_argument("--threshold", type=float, default=None)
    ap.add_argument("--max-width", type=int, default=560)
    ap.add_argument("--gray", action="store_true", help="store grayscale+alpha")
    ap.add_argument("--pad", type=int, default=20)
    ap.add_argument("--feather", type=float, default=1.1)
    ap.add_argument("--keep-png", action="store_true")
    ap.add_argument("--label", default="portrait")
    args = ap.parse_args()

    im = Image.open(args.input).convert("RGB")
    rgb = np.asarray(im).astype(np.float32)
    lum = rgb.mean(axis=2)
    H, W = lum.shape

    bg_kind, auto_t = detect_background(lum, args.bg)
    thresh = args.threshold if args.threshold is not None else auto_t
    print(f"background: {bg_kind}  threshold: {thresh:.0f}")

    alpha = build_alpha(lum, bg_kind, thresh, args.feather)

    rgba = np.dstack([rgb.astype(np.uint8), alpha])
    res = Image.fromarray(rgba, "RGBA")

    # trim to content bbox with padding
    ys, xs = np.where(alpha > 12)
    if len(xs) == 0:
        print("error: nothing left after keying — check --bg/--threshold", file=sys.stderr)
        return 2
    y0, y1 = max(0, ys.min() - args.pad), min(H, ys.max() + args.pad)
    x0, x1 = max(0, xs.min() - args.pad), min(W, xs.max() + args.pad)
    res = res.crop((x0, y0, x1, y1))

    # downscale for embedding
    w, h = res.size
    scale = min(1.0, args.max_width / w)
    if scale < 1.0:
        res = res.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    if args.gray:
        res = res.convert("LA")
    W2, H2 = res.size

    buf = io.BytesIO()
    res.save(buf, "PNG", optimize=True)
    png = buf.getvalue()

    svg = make_svg(png, W2, H2, args.label)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg)

    if args.keep_png:
        png_path = args.output.rsplit(".", 1)[0] + ".png"
        res.save(png_path)
        print(f"wrote {png_path}")

    print(f"wrote {args.output}  ({len(svg)//1024} KB svg, {len(png)//1024} KB png, {W2}x{H2})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
