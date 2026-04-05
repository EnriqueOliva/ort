import { mdToPdf } from 'md-to-pdf';
import katex from 'katex';
import { readFileSync, writeFileSync } from 'fs';
import { resolve, dirname, basename, join } from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const require = createRequire(import.meta.url);

const PRINT_CSS = join(__dirname, 'print.css');
const KATEX_CSS = join(dirname(require.resolve('katex')), 'katex.min.css');

function renderLatexToHtml(markdown) {
  let result = markdown;

  result = result.replace(/\$\$([\s\S]*?)\$\$/g, (_match, tex) => {
    try {
      return '<div class="katex-display">' +
        katex.renderToString(tex.trim(), { displayMode: true, throwOnError: false }) +
        '</div>';
    } catch {
      return _match;
    }
  });

  result = result.replace(/(?<![\\$])\$([^\$\n]+?)\$(?!\$)/g, (_match, tex) => {
    try {
      return katex.renderToString(tex.trim(), { displayMode: false, throwOnError: false });
    } catch {
      return _match;
    }
  });

  return result;
}

async function convert(inputPath) {
  const fullPath = resolve(inputPath);
  const outputPath = fullPath.replace(/\.md$/i, '.pdf');
  const markdown = readFileSync(fullPath, 'utf8');
  const processed = renderLatexToHtml(markdown);

  const result = await mdToPdf(
    { content: processed },
    {
      basedir: dirname(fullPath),
      stylesheet: [KATEX_CSS, PRINT_CSS],
      css: '.markdown-body { max-width: 100%; }',
      pdf_options: {
        format: 'A4',
        margin: { top: '22mm', right: '18mm', bottom: '22mm', left: '18mm' },
        printBackground: true,
        displayHeaderFooter: true,
        headerTemplate: '<div></div>',
        footerTemplate: '<div style="font-size:9pt;text-align:center;width:100%;color:#555;">— <span class="pageNumber"></span> / <span class="totalPages"></span> —</div>',
      },
    }
  );

  writeFileSync(outputPath, result.content);
  return outputPath;
}

const files = process.argv.slice(2);

if (files.length === 0) {
  console.error('Uso: node print/build.js <archivo.md> [archivo2.md ...]');
  process.exit(1);
}

let ok = 0;
let fail = 0;

for (const file of files) {
  const name = basename(file, '.md');
  process.stdout.write(`Generando ${name}.pdf... `);
  try {
    const out = await convert(file);
    console.log(`OK -> ${out}`);
    ok++;
  } catch (err) {
    console.log(`ERROR: ${err.message}`);
    fail++;
  }
}

console.log(`\nListo. ${ok} PDF(s) generado(s)${fail > 0 ? `, ${fail} error(es)` : ''}.`);
