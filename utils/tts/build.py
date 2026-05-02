import asyncio
import re
import sys
from pathlib import Path

import edge_tts

DEFAULT_VOICE = "es-AR-ElenaNeural"


def strip_markdown(md_text):
    text = md_text
    text = re.sub(r"^---+\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = text.replace("**", "")
    text = re.sub(r"(?<!\w)[\*_]([^\*_\n]+?)[\*_](?!\w)", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


async def synthesize(text, voice, output_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_path))


def main():
    if len(sys.argv) < 2:
        print("Uso: python build.py <archivo.md> [--voice VOICE]")
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()
    voice = DEFAULT_VOICE
    if "--voice" in sys.argv:
        voice = sys.argv[sys.argv.index("--voice") + 1]

    output_path = input_path.with_suffix(".mp3")
    md_text = input_path.read_text(encoding="utf-8")
    clean_text = strip_markdown(md_text)

    char_count = len(clean_text)
    estimated_minutes = char_count / 900

    print(f"Archivo: {input_path.name}")
    print(f"Caracteres: {char_count} (~{estimated_minutes:.1f} min estimados)")
    print(f"Voz: {voice}")
    print(f"Generando {output_path.name}...")

    asyncio.run(synthesize(clean_text, voice, output_path))

    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"OK -> {output_path} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
