#!/usr/bin/env python3
"""
Trend Scout — Option B (yt-dlp based).
Scans all competitor channels, computes outlier scores against each channel's
own recent average, and prints a ranked list.

Usage:
    python3 scripts/trend_scan.py [--days 14] [--top 20]

Reads channel URLs from brand/competitors.md (markdown table).
"""
import argparse
import json
import math
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

YTDLP = "/Users/ek/Library/Python/3.9/bin/yt-dlp"
ROOT = Path(__file__).resolve().parent.parent
COMPETITORS_MD = ROOT / "brand" / "competitors.md"


def parse_competitors():
    text = COMPETITORS_MD.read_text()
    urls = re.findall(r"https://www\.youtube\.com/@[\w\.\-]+", text)
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def channel_name_from_url(url):
    m = re.search(r"@([\w\.\-]+)", url)
    return m.group(1) if m else url


def fetch_channel(url, limit=15, attempts=2):
    name = channel_name_from_url(url)
    target = url.rstrip("/")
    if not target.endswith("/videos"):
        target += "/videos"
    cmd = [
        YTDLP, "--no-warnings", "--ignore-errors",
        "--flat-playlist",
        "--extractor-args", "youtubetab:approximate_date",
        "--print", "%(title)s\t%(view_count)s\t%(upload_date)s\t%(id)s",
        "--playlist-end", str(limit),
        target,
    ]
    for _ in range(attempts):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        except subprocess.TimeoutExpired:
            continue
        rows = []
        for line in r.stdout.strip().splitlines():
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            title, views, date, vid = parts[:4]
            try:
                views = int(views)
            except ValueError:
                continue
            try:
                d = datetime.strptime(date, "%Y%m%d").replace(tzinfo=timezone.utc)
            except ValueError:
                d = None
            rows.append({
                "title": title, "views": views, "date": d,
                "id": vid, "channel": name, "url": url,
                "video_url": f"https://youtu.be/{vid}",
            })
        if rows:
            return rows
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14, help="Window of recent uploads to consider")
    ap.add_argument("--top", type=int, default=25, help="Top N outliers to print")
    ap.add_argument("--limit", type=int, default=15, help="Videos per channel to fetch")
    args = ap.parse_args()

    channels = parse_competitors()
    print(f"Scanning {len(channels)} channels (limit={args.limit}/channel)...", file=sys.stderr)

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    all_videos = []

    for url in channels:
        print(f"  -> {url}", file=sys.stderr)
        vids = fetch_channel(url, args.limit)
        if not vids:
            print(f"     (no data)", file=sys.stderr)
            continue
        # Average across all fetched videos for this channel (signal of typical performance)
        avg = sum(v["views"] for v in vids) / len(vids)
        for v in vids:
            v["channel_avg"] = avg
            v["outlier"] = v["views"] / avg if avg else 0
        all_videos.extend(vids)

    recent = [
        v for v in all_videos
        if v["date"] is None or v["date"] >= cutoff
    ]
    recent.sort(key=lambda v: v["outlier"], reverse=True)

    out = []
    for v in recent[:args.top]:
        out.append({
            "title": v["title"],
            "channel": v["channel"],
            "views": v["views"],
            "channel_avg": int(v["channel_avg"]),
            "outlier": round(v["outlier"], 2),
            "date": v["date"].strftime("%Y-%m-%d") if v["date"] else "n/a",
            "url": v["video_url"],
        })
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
