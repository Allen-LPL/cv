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
          -->  wrapped in a doc that inlines the chosen style CSS
          -->  written as a temp .html *inside the md's directory*
               (so relative img/... paths resolve over file://)
          -->  Chromium loads it and prints A4 PDF
          -->  temp .html removed
```

Page geometry (A4, 15mm margins, `printBackground`) is set in `md2pdf.js`;
document typography lives in the `styles/` directory (one CSS per style).

## Install

```bash
cd tools/md-to-pdf
npm install          # pulls markdown-it + puppeteer (downloads a Chromium, ~150MB, once)
```

`node_modules/` is git-ignored — only the source, `package.json` and the
`styles/` CSS are committed.

### Global command (alias)

To run it from any directory, add a shell alias (already set up on this machine):

```bash
# ~/.zshrc
alias md2pdf='node /Users/allen/Code/cv/tools/md-to-pdf/md2pdf.js'
```

Then `md2pdf foo.md` works anywhere. The script finds its `styles/` via
`__dirname`, so the working directory doesn't matter.

## Usage

```bash
# with the alias, from anywhere
md2pdf 2026-简历.md
# → writes 2026-简历.pdf (overwriting) next to the source

# or without the alias, from tools/md-to-pdf
node md2pdf.js ../../2026-简历.md

# custom output path
md2pdf 2026-简历.md -o ~/Desktop/allen-cv.pdf
```

- One file per run — you pass the `.md` you want each time (no batch mode).
- Default output: `<same name>.pdf` next to the source `.md`, overwritten.

## Styles

Pick a built-in style with `-s` / `--style` (default `resume`):

```bash
md2pdf notes.md -s article    # general prose (notes, minutes, posts)
md2pdf contract.md -s plain   # minimal black & white
md2pdf 2026-简历.md            # resume (default)
```

| style     | for                          | look                                            |
| --------- | ---------------------------- | ----------------------------------------------- |
| `resume`  | this repo's CV (default)     | dense 10.5pt, ruled section headings, blue links |
| `article` | prose / notes / minutes      | roomy 11pt, 1.75 line-height, light headings    |
| `plain`   | contracts / typewritten docs | 11pt black-and-white, no accent, boxed code     |

Each style is one file under `styles/<name>.css`; add a style by dropping a new
CSS file there (its filename becomes the `-s` name). For a one-off custom
stylesheet outside `styles/`, use `--css <file>`:

```bash
md2pdf report.md --css ~/my-theme.css
```

## Customising the look

Edit the relevant `styles/<name>.css` (fonts, sizes, colours, spacing,
page-break rules), or add a new one. To bundle a font for cross-machine
consistency instead of relying on the local system CJK font, add it as a
`@font-face` (base64 or a relative path) in that CSS.

## Requirements

Node.js + npm. Puppeteer downloads its own Chromium on install, so no system
Chrome is required.
