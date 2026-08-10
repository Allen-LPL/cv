#!/usr/bin/env node
/*
 * md2pdf.js — render one resume Markdown file to a clean A4 PDF.
 *
 * The resume .md files in this repo embed raw HTML (<img align='right'>,
 * <br/>, <div style="page-break-after">), an inline <svg> avatar, relative
 * asset paths (img/avatar.svg) and Chinese (CJK) text. A markdown-only or
 * LaTeX pipeline mangles those; a headless-Chromium pipeline renders them
 * exactly as a browser would.
 *
 * Pipeline:  Markdown --markdown-it(html:true)--> HTML fragment
 *            --> wrapped in an HTML doc that <link>s print.css
 *            --> written as a temp .html *inside the md's directory* so that
 *                relative file:// assets (img/...) resolve
 *            --> Chromium loads it via file:// and prints A4 PDF
 *            --> temp .html is removed
 *
 * Usage:
 *   node md2pdf.js <input.md> [-o <output.pdf>]
 *
 * Default output is "<input basename>.pdf" next to the source .md (overwritten).
 */

const fs = require("fs");
const path = require("path");
const MarkdownIt = require("markdown-it");
const puppeteer = require("puppeteer");

function parseArgs(argv) {
  const args = { input: null, output: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "-o" || a === "--output") {
      args.output = argv[++i];
    } else if (a === "-h" || a === "--help") {
      args.help = true;
    } else if (!args.input) {
      args.input = a;
    } else {
      throw new Error(`Unexpected argument: ${a}`);
    }
  }
  return args;
}

// Resolve a Chromium/Chrome executable. Puppeteer ships its own Chromium, but
// that download can be corrupt or unsigned on some macOS setups. Preference:
//   1. PUPPETEER_EXECUTABLE_PATH (explicit override)
//   2. a working system Chrome/Chromium/Edge
//   3. undefined -> Puppeteer's bundled Chromium
function resolveExecutablePath() {
  if (process.env.PUPPETEER_EXECUTABLE_PATH) {
    return process.env.PUPPETEER_EXECUTABLE_PATH;
  }
  const candidates =
    process.platform === "darwin"
      ? [
          "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
          "/Applications/Chromium.app/Contents/MacOS/Chromium",
          "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        ]
      : [
          "/usr/bin/google-chrome",
          "/usr/bin/chromium",
          "/usr/bin/chromium-browser",
        ];
  for (const c of candidates) {
    if (fs.existsSync(c)) return c;
  }
  return undefined; // let Puppeteer use its bundled Chromium
}

function usage() {
  console.log(
    "Usage: node md2pdf.js <input.md> [-o <output.pdf>]\n" +
      "\n" +
      "  Renders a Markdown file (raw HTML/SVG + CJK supported) to a clean A4 PDF.\n" +
      "  Default output is <input basename>.pdf next to the source file."
  );
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || !args.input) {
    usage();
    process.exit(args.input ? 0 : 1);
  }

  const inputPath = path.resolve(args.input);
  if (!fs.existsSync(inputPath)) {
    console.error(`Error: input file not found: ${inputPath}`);
    process.exit(1);
  }

  const srcDir = path.dirname(inputPath);
  const base = path.basename(inputPath, path.extname(inputPath));
  const outputPath = args.output
    ? path.resolve(args.output)
    : path.join(srcDir, `${base}.pdf`);

  const markdown = fs.readFileSync(inputPath, "utf8");

  const md = new MarkdownIt({
    html: true, // pass raw HTML/SVG through untouched
    linkify: true, // auto-link bare URLs
    typographer: false,
  });
  const bodyHtml = md.render(markdown);

  const cssPath = path.join(__dirname, "print.css");
  const css = fs.readFileSync(cssPath, "utf8");

  // Full HTML doc. The CSS is inlined so the temp file is self-contained;
  // relative <img src="img/..."> resolve because the temp file lives in srcDir.
  const htmlDoc = `<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>${base}</title>
<style>
${css}
</style>
</head>
<body>
${bodyHtml}
</body>
</html>`;

  // Write the temp HTML next to the source so relative assets resolve via file://.
  const tmpHtmlPath = path.join(srcDir, `.md2pdf.${process.pid}.tmp.html`);
  fs.writeFileSync(tmpHtmlPath, htmlDoc, "utf8");

  let browser;
  try {
    browser = await puppeteer.launch({
      headless: true,
      executablePath: resolveExecutablePath(),
      args: ["--no-sandbox", "--allow-file-access-from-files"],
    });
    const page = await browser.newPage();
    await page.goto("file://" + tmpHtmlPath, { waitUntil: "networkidle0" });
    await page.pdf({
      path: outputPath,
      format: "A4",
      printBackground: true,
      margin: { top: "15mm", right: "15mm", bottom: "15mm", left: "15mm" },
    });
  } finally {
    if (browser) await browser.close();
    fs.rmSync(tmpHtmlPath, { force: true });
  }

  console.log(`✓ ${path.relative(process.cwd(), inputPath)} → ${path.relative(process.cwd(), outputPath)}`);
}

main().catch((err) => {
  console.error("Error:", err.message);
  process.exit(1);
});
