# transparent-svg

Auxiliary tool for this CV site. Turns a photo shot on a **plain (studio)
background** into a **background‑removed, transparent SVG** — the raster cutout
is embedded as a PNG data‑URI inside the SVG, so a single `.svg` file drops in
anywhere an `<img>` goes.

This is the exact tool used to generate [`img/avatar.svg`](../../img/avatar.svg)
(the floating hero portrait) from a black‑and‑white studio headshot.

## How it works (no ML needed)

When the subject sits on a roughly uniform background, the background is simply
the set of light (or dark) pixels **connected to the image border**. So:

1. Sample the top corners/edge to decide whether the background is light or dark.
2. Threshold to a "background‑like" mask, label connected components, keep only
   the ones touching the border → that's the true background.
3. `binary_fill_holes` so trapped interior gaps (e.g. glasses lenses) stay part
   of the subject.
4. Erode 1px to kill the background halo, Gaussian‑feather the edge, and apply a
   graded alpha in the transition band so stray hair fringes fade instead of a
   hard cut.
5. Trim to the subject's bounding box, downscale, optionally convert to
   grayscale+alpha (much smaller for B&W photos), embed as a PNG data‑URI in an
   `<svg>`.

Because it's a border‑connected key, it works precisely when the subject's
silhouette fully encloses any interior features — true for headshots.

## Install

```bash
pip install -r requirements.txt   # numpy, scipy, pillow
```

## Usage

```bash
python3 make_transparent_svg.py INPUT -o OUTPUT.svg [options]
```

Reproduce the site avatar from the source portrait:

```bash
python3 make_transparent_svg.py portrait.png -o ../../img/avatar.svg --gray
```

| Option | Default | Meaning |
| --- | --- | --- |
| `-o, --output` | — | output `.svg` path (required) |
| `--bg auto\|light\|dark` | `auto` | which background to remove; `auto` reads the top of the image |
| `--threshold N` | auto | luminance cutoff 0–255 (override auto) |
| `--max-width N` | `560` | downscale the embedded raster to this width |
| `--gray` | off | store grayscale+alpha (≈half the size for B&W photos) |
| `--pad N` | `20` | transparent padding kept around the subject (px) |
| `--feather N` | `1.1` | edge feather blur radius (px) |
| `--keep-png` | off | also write the trimmed cutout as a sibling `.png` |
| `--label TEXT` | `portrait` | SVG `aria-label` |

## Notes & limits

- Designed for **plain / studio backgrounds**. Busy or cluttered backgrounds
  need a segmentation model (e.g. `rembg`) instead.
- Auto‑detection assumes the background is at the **top** of the frame (normal
  for portraits). If the subject is dark‑on‑dark or the bg is at the bottom,
  pass `--bg` and/or `--threshold` explicitly.
- On the site the portrait is displayed as a free‑standing hero image; the dark
  hoodie is dissolved into the dark theme with a CSS bottom‑fade mask on
  `#avatar` (see the `<style>` block in `index.html`), not by this tool.
- The embedded SVG for a 560px B&W portrait is ~0.5 MB. Lower `--max-width` for a
  smaller file if load size matters.
