import json
import subprocess
import sys
import math
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "output"
MAX_PART_SIZE_MB = 95
TARGET_HEIGHT = 480
TARGET_FPS = 10
CRF = 28
AUDIO_BITRATE = "96k"
PRESET = "medium"


def run_ffmpeg(command):
    subprocess.run(command, check=True, encoding="utf-8", errors="replace")


def get_duration(video_path):
    result = subprocess.run(
        [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            str(video_path),
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def compress(source_path, temp_path):
    command = [
        "ffmpeg", "-y",
        "-i", str(source_path),
        "-vf", f"scale=-2:{TARGET_HEIGHT},fps={TARGET_FPS}",
        "-c:v", "libx265",
        "-crf", str(CRF),
        "-preset", PRESET,
        "-c:a", "aac",
        "-b:a", AUDIO_BITRATE,
        str(temp_path),
    ]
    run_ffmpeg(command)


def split_video(compressed_path, output_folder, base_name, duration, num_parts):
    part_duration = duration / num_parts

    for part_index in range(num_parts):
        part_number = part_index + 1
        start_seconds = part_index * part_duration
        part_filename = f"{base_name}-part{part_number}.mp4"
        part_path = output_folder / part_filename

        command = [
            "ffmpeg", "-y",
            "-i", str(compressed_path),
            "-ss", str(start_seconds),
            "-t", str(part_duration),
            "-c", "copy",
            str(part_path),
        ]
        run_ffmpeg(command)
        part_size_mb = part_path.stat().st_size / (1024 * 1024)
        print(f"  {part_filename}: {part_size_mb:.1f} MB")


def process_video(video_path, output_dir):
    video_path = Path(video_path)
    if not video_path.exists():
        print(f"File not found: {video_path}")
        return

    base_name = video_path.stem
    original_size_mb = video_path.stat().st_size / (1024 * 1024)
    print(f"\n{'=' * 60}")
    print(f"Processing: {video_path.name}")
    print(f"Original: {original_size_mb:.0f} MB")
    print(f"{'=' * 60}")

    duration = get_duration(video_path)
    output_folder = output_dir / base_name
    output_folder.mkdir(parents=True, exist_ok=True)

    temp_path = output_folder / "_temp_compressed.mp4"

    print("Compressing...")
    compress(video_path, temp_path)

    compressed_size_mb = temp_path.stat().st_size / (1024 * 1024)
    compression_ratio = original_size_mb / compressed_size_mb
    print(f"Compressed: {compressed_size_mb:.0f} MB ({compression_ratio:.1f}x reduction)")

    if compressed_size_mb <= MAX_PART_SIZE_MB:
        final_path = output_folder / f"{base_name}.mp4"
        temp_path.rename(final_path)
        print(f"  {final_path.name}: {compressed_size_mb:.1f} MB (no split needed)")
    else:
        num_parts = math.ceil(compressed_size_mb / MAX_PART_SIZE_MB)
        print(f"Splitting into {num_parts} parts...")
        split_video(temp_path, output_folder, base_name, duration, num_parts)
        temp_path.unlink()

    print("Done!")


def main():
    if len(sys.argv) < 2:
        print("Usage: python compress.py [--output DIR] video1.mp4 [video2.mp4 ...]")
        sys.exit(1)

    args = sys.argv[1:]
    output_dir = DEFAULT_OUTPUT_DIR

    if args[0] == "--output" and len(args) >= 3:
        output_dir = Path(args[1])
        args = args[2:]

    print(f"Processing {len(args)} video(s)...")
    print(f"Output: {output_dir}")

    for video_path in args:
        process_video(video_path, output_dir)

    print(f"\n{'=' * 60}")
    print(f"All done! Output: {output_dir}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
