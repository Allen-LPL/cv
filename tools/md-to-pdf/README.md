# md-to-pdf

Render a resume Markdown file to a clean **A4 PDF** using headless Chromium
(Puppeteer). Built for this repo's resumes, which embed **raw HTML/SVG**
(`<img align='right'>`, `<br/>`, `<div style="page-break-after">`, an inline
`<svg>` avatar), reference **relative images** (`img/avatar.svg`), and are in
**Chinese (CJK)** — cases a markdown-only or LaTeX pipeline mangles.

## Why Chromium

The `.md` files are HTML-rich and CJK. A headless browser renders them exactly
as a browser would: raw HTML passes through, `<svg>` and relative `file://`
assets load, explicit page breaks are honoured, and system CJK fonts
(PingFang SC …) are used with no per-file font config.

## How it works

```
Markdown  --markdown-it(html:true)-->  HTML fragment
          -->  wrapped in a doc that inlines print.css
          -->  written as a temp .html *inside the md's directory*
               (so relative img/... paths resolve over file://)
          -->  Chromium loads it and prints A4 PDF
          -->  temp .html removed
```

Page geometry (A4, 15mm margins, `printBackground`) is set in `md2pdf.js`;
document typography lives in `print.css`.

## Install

```bash
cd tools/md-to-pdf
npm install          # pulls markdown-it + puppeteer (downloads a Chromium, ~150MB, once)
```

`node_modules/` is git-ignored — only the source, `package.json` and
`print.css` are committed.

## Usage

```bash
# from tools/md-to-pdf
node md2pdf.js ../../2026-简历.md
# → writes ../../2026-简历.pdf (overwriting)

# custom output path
node md2pdf.js ../../2026-简历.md -o ~/Desktop/allen-cv.pdf
```

- One file per run — you pass the `.md` you want each time (no batch mode).
- Default output: `<same name>.pdf` next to the source `.md`, overwritten.

## Customising the look

Edit `print.css` (fonts, sizes, colours, spacing, page-break rules). To bundle
a font for cross-machine consistency instead of relying on the local system
CJK font, add it as a `@font-face` (base64 or a relative path) in `print.css`.

## Requirements

Node.js + npm. Puppeteer downloads its own Chromium on install, so no system
Chrome is required.
