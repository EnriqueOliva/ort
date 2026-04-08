import re
import sys
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
COMPRESS_SCRIPT = SCRIPT_DIR / "compress.py"
TEMP_OUTPUT = SCRIPT_DIR / "output"

MONTH_NAMES = {
    "01": "ene", "02": "feb", "03": "mar", "04": "abr",
    "05": "may", "06": "jun", "07": "jul", "08": "ago",
    "09": "sep", "10": "oct", "11": "nov", "12": "dic",
}

COURSE_MAP = {
    "FI-1479": ("ingenieriaSistemas/1erSemestre/programacion1", "Programacion 1"),
    "FI-2103": ("ingenieriaSistemas/1erSemestre/algebraLineal", "Algebra Lineal"),
}


def extract_date(filename):
    match = re.search(r'(\d{2})-(\d{2})-(\d{4})', filename)
    if not match:
        return None
    day, month, year = match.group(1), match.group(2), match.group(3)
    month_name = MONTH_NAMES.get(month, month)
    return f"{day}-{month_name}-{year}"


def extract_course_code(filename):
    for code in COURSE_MAP:
        if code in filename:
            return code
    return None


def find_files(showcase_path, extension):
    results = []
    for item in sorted(showcase_path.rglob(f"*{extension}")):
        if item.is_file():
            results.append(item)
    return results


def place_transcripts(showcase_path):
    txt_files = find_files(showcase_path, ".txt")
    placed = 0

    for txt in txt_files:
        date_name = extract_date(txt.name)
        course_code = extract_course_code(txt.name)
        if not date_name or not course_code:
            print(f"  SKIP (no date/course): {txt.name}")
            continue

        course_rel, course_label = COURSE_MAP[course_code]
        dest_dir = PROJECT_ROOT / course_rel / "theory" / "classesTranscripts" / date_name
        dest_file = dest_dir / f"{date_name}.txt"

        if dest_file.exists():
            print(f"  EXISTS: {course_label} {date_name} transcript")
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(txt, dest_file)
        print(f"  OK: {course_label} {date_name} transcript")
        placed += 1

    return placed


def compress_and_place_videos(showcase_path):
    import subprocess

    mp4_files = find_files(showcase_path, ".mp4")
    placed = 0

    for mp4 in mp4_files:
        date_name = extract_date(mp4.name)
        course_code = extract_course_code(mp4.name)
        if not date_name or not course_code:
            print(f"  SKIP (no date/course): {mp4.name}")
            continue

        course_rel, course_label = COURSE_MAP[course_code]
        dest_dir = PROJECT_ROOT / course_rel / "theory" / "classesVideos" / date_name

        existing = list(dest_dir.glob("*.mp4")) if dest_dir.exists() else []
        if existing:
            print(f"  EXISTS: {course_label} {date_name} video ({len(existing)} file(s))")
            continue

        original_mb = mp4.stat().st_size / (1024 * 1024)
        print(f"\n  Compressing {course_label} {date_name} ({original_mb:.0f} MB)...")

        subprocess.run(
            [sys.executable, str(COMPRESS_SCRIPT), "--output", str(TEMP_OUTPUT), str(mp4)],
            check=True,
        )

        compressed_dir = TEMP_OUTPUT / mp4.stem
        if not compressed_dir.exists():
            print(f"  ERROR: compression output not found for {mp4.name}")
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        parts = sorted(compressed_dir.glob("*.mp4"))

        for i, part in enumerate(parts):
            if len(parts) == 1:
                dest_name = f"{date_name}.mp4"
            else:
                dest_name = f"{date_name}-part{i + 1}.mp4"
            dest_file = dest_dir / dest_name
            shutil.copy2(part, dest_file)
            size_mb = dest_file.stat().st_size / (1024 * 1024)
            print(f"  OK: {dest_name} ({size_mb:.0f} MB)")

        shutil.rmtree(compressed_dir)
        placed += 1

    return placed


def main():
    if len(sys.argv) < 2:
        print("Usage: python process-showcase.py <showcase-folder>")
        print("Example: python process-showcase.py \"C:\\Users\\Enrique\\Documents\\Unvimeo\\Showcase 12151824\"")
        sys.exit(1)

    showcase_path = Path(sys.argv[1])
    if not showcase_path.exists():
        print(f"Folder not found: {showcase_path}")
        sys.exit(1)

    print(f"Processing showcase: {showcase_path.name}")
    print(f"Project root: {PROJECT_ROOT}")

    all_files = list(showcase_path.rglob("*"))
    mp4_count = sum(1 for f in all_files if f.suffix == ".mp4")
    txt_count = sum(1 for f in all_files if f.suffix == ".txt")
    print(f"Found: {mp4_count} video(s), {txt_count} transcript(s)")

    print(f"\n--- Transcripts ---")
    if txt_count > 0:
        transcripts_placed = place_transcripts(showcase_path)
        print(f"Transcripts placed: {transcripts_placed}")
    else:
        print("No transcripts found.")

    print(f"\n--- Videos ---")
    if mp4_count > 0:
        videos_placed = compress_and_place_videos(showcase_path)
        print(f"\nVideos compressed and placed: {videos_placed}")
    else:
        print("No videos found.")

    if TEMP_OUTPUT.exists() and not any(TEMP_OUTPUT.iterdir()):
        TEMP_OUTPUT.rmdir()

    print(f"\n{'=' * 60}")
    print("Done!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
