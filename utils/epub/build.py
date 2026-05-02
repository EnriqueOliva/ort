import re
import sys
from pathlib import Path
from uuid import uuid4

import markdown
from ebooklib import epub


DEFAULT_LANGUAGE = "es"
DEFAULT_AUTHOR = "Enrique"


def split_chapters(md_text):
    lines = md_text.split("\n")
    preface_lines = []
    chapters = []
    current_title = None
    current_lines = []

    for line in lines:
        heading_match = re.match(r"^##\s+(.+)$", line)
        if heading_match:
            if current_title is None:
                preface_lines = current_lines
            else:
                chapters.append((current_title, "\n".join(current_lines).strip()))
            current_title = heading_match.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_title is None:
        preface_lines = current_lines
    else:
        chapters.append((current_title, "\n".join(current_lines).strip()))

    preface_text = "\n".join(preface_lines).strip()
    return preface_text, chapters


def build_epub(input_path, output_path, language, author):
    md_text = input_path.read_text(encoding="utf-8")
    md_text = re.sub(r"^---+\s*$", "", md_text, flags=re.MULTILINE)

    first_line = md_text.split("\n", 1)[0]
    title_match = re.match(r"^#\s+(.+)$", first_line)
    if title_match:
        title = title_match.group(1).strip()
        body_text = md_text[len(first_line):].lstrip("\n")
    else:
        title = input_path.stem
        body_text = md_text

    preface_md, chapters_md = split_chapters(body_text)

    book = epub.EpubBook()
    book.set_identifier(str(uuid4()))
    book.set_title(title)
    book.set_language(language)
    book.add_author(author)

    md_converter = markdown.Markdown(extensions=["extra", "sane_lists"])

    spine = ["nav"]
    toc = []

    if preface_md:
        md_converter.reset()
        preface_html = md_converter.convert(preface_md)
        preface_item = epub.EpubHtml(
            title="Introducción",
            file_name="preface.xhtml",
            lang=language,
        )
        preface_item.content = f"<h1>Introducción</h1>{preface_html}"
        book.add_item(preface_item)
        spine.append(preface_item)
        toc.append(preface_item)

    for idx, (chapter_title, chapter_md) in enumerate(chapters_md, start=1):
        md_converter.reset()
        chapter_html = md_converter.convert(chapter_md)
        chapter_item = epub.EpubHtml(
            title=chapter_title,
            file_name=f"chapter-{idx:02d}.xhtml",
            lang=language,
        )
        chapter_item.content = f"<h1>{chapter_title}</h1>{chapter_html}"
        book.add_item(chapter_item)
        spine.append(chapter_item)
        toc.append(chapter_item)

    book.toc = tuple(toc)
    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub(str(output_path), book)

    return title, len(chapters_md) + (1 if preface_md else 0)


def main():
    if len(sys.argv) < 2:
        print("Uso: python build.py <archivo.md> [--lang LANG] [--author AUTHOR]")
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()
    language = DEFAULT_LANGUAGE
    author = DEFAULT_AUTHOR

    if "--lang" in sys.argv:
        language = sys.argv[sys.argv.index("--lang") + 1]
    if "--author" in sys.argv:
        author = sys.argv[sys.argv.index("--author") + 1]

    output_path = input_path.with_suffix(".epub")

    print(f"Archivo: {input_path.name}")
    print(f"Idioma: {language}")
    print(f"Generando {output_path.name}...")

    title, chapter_count = build_epub(input_path, output_path, language, author)

    size_kb = output_path.stat().st_size / 1024
    print(f"Título: {title}")
    print(f"Capítulos: {chapter_count}")
    print(f"OK -> {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
