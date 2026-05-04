#!/usr/bin/env python3
"""
Fetch a YouTube auto-caption transcript and save as plain readable text
with timestamps every ~30s.

Usage:
    python3 scripts/fetch_transcript.py <video_id_or_url> [--out path.txt]
"""
import argparse
import re
import sys
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi


def extract_id(s):
    if len(s) == 11 and "/" not in s:
        return s
    m = re.search(r"(?:youtu\.be/|v=|/shorts/)([\w\-]{11})", s)
    return m.group(1) if m else s


def fmt_time(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", help="Video ID or URL")
    ap.add_argument("--out", help="Output file path")
    ap.add_argument("--block", type=int, default=30,
                    help="Group lines into ~N-second blocks (default 30)")
    args = ap.parse_args()

    vid = extract_id(args.video)
    api = YouTubeTranscriptApi()
    fetched = api.fetch(vid, languages=["en", "en-US", "en-GB"])
    segments = fetched.to_raw_data()

    blocks = []
    cur_start = 0
    cur_text = []
    for seg in segments:
        text = seg["text"].replace("\n", " ").strip()
        if not text:
            continue
        if not cur_text:
            cur_start = seg["start"]
        cur_text.append(text)
        if seg["start"] - cur_start >= args.block:
            blocks.append((cur_start, " ".join(cur_text)))
            cur_text = []
    if cur_text:
        blocks.append((cur_start, " ".join(cur_text)))

    out_lines = [f"# Transcript — https://youtu.be/{vid}", ""]
    for start, text in blocks:
        out_lines.append(f"[{fmt_time(start)}] {text}")
        out_lines.append("")
    output = "\n".join(out_lines)

    if args.out:
        Path(args.out).write_text(output)
        print(f"Wrote {args.out} ({len(blocks)} blocks, {len(segments)} segments)",
              file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
