#!/usr/bin/env python3
"""
Trend Scout — Weekly outlier scan with size-adjusted scoring.

Two-pass scan:
  Pass 1 — flat-playlist per channel: titles, IDs, upload dates, follower count,
            and view_count when YouTube exposes it on the tile.
  Pass 2 — detail fetch for any video missing view_count (typically very fresh
            uploads). Single yt-dlp call per channel batched by ID list.

Outlier vs. channel's last-N average. Adjusted = outlier × log10(1M / subs).

Usage:
    python3 scripts/trend_scan_weekly.py [--days 7] [--top 25] [--limit 25]
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


def channel_handle(url):
    m = re.search(r"@([\w\.\-]+)", url)
    return m.group(1) if m else url


def run_ytdlp(args, timeout=120):
    try:
        return subprocess.run([YTDLP, *args], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None


def fetch_channel_followers(url):
    """Use a single recent video to extract channel + follower count."""
    target = url.rstrip("/")
    if not target.endswith("/videos"):
        target += "/videos"
    r = run_ytdlp([
        "--no-warnings", "--skip-download", "--playlist-end", "1",
        "--print", "%(channel)s\t%(channel_follower_count)s",
        target,
    ], timeout=60)
    if r is None or not r.stdout.strip():
        return None, 0
    line = r.stdout.strip().splitlines()[0]
    parts = line.split("\t")
    name = parts[0] if parts else None
    try:
        subs = int(parts[1]) if len(parts) > 1 and parts[1] not in ("", "NA") else 0
    except ValueError:
        subs = 0
    return name, subs


def fetch_flat_videos(url, limit=25):
    target = url.rstrip("/")
    if not target.endswith("/videos"):
        target += "/videos"
    r = run_ytdlp([
        "--no-warnings", "--ignore-errors", "--flat-playlist",
        "--extractor-args", "youtubetab:approximate_date",
        "--print", "%(title)s\t%(view_count)s\t%(upload_date)s\t%(id)s\t%(duration)s",
        "--playlist-end", str(limit),
        target,
    ], timeout=120)
    if r is None:
        return []
    rows = []
    for line in r.stdout.strip().splitlines():
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        title, views_raw, date_raw, vid = parts[:4]
        duration_raw = parts[4] if len(parts) > 4 else "NA"
        try:
            views = int(views_raw) if views_raw not in ("NA", "") else None
        except ValueError:
            views = None
        try:
            d = datetime.strptime(date_raw, "%Y%m%d").replace(tzinfo=timezone.utc)
        except ValueError:
            d = None
        try:
            dur = int(float(duration_raw)) if duration_raw not in ("NA", "") else 0
        except ValueError:
            dur = 0
        rows.append({
            "title": title, "views": views, "date": d,
            "id": vid, "duration_sec": dur,
            "video_url": f"https://youtu.be/{vid}",
        })
    return rows


def enrich_missing_views(videos):
    """For videos with views=None or duration=0, batch-fetch detail in one call."""
    needs = [v for v in videos if v["views"] is None or v["duration_sec"] == 0]
    if not needs:
        return
    urls = [v["video_url"] for v in needs]
    r = run_ytdlp([
        "--no-warnings", "--skip-download",
        "--print", "%(id)s\t%(view_count)s\t%(duration)s\t%(upload_date)s",
        *urls,
    ], timeout=180)
    if r is None:
        return
    by_id = {}
    for line in r.stdout.strip().splitlines():
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        vid, views_raw, dur_raw, date_raw = parts[:4]
        try:
            views = int(views_raw) if views_raw not in ("NA", "") else 0
        except ValueError:
            views = 0
        try:
            dur = int(float(dur_raw)) if dur_raw not in ("NA", "") else 0
        except ValueError:
            dur = 0
        try:
            d = datetime.strptime(date_raw, "%Y%m%d").replace(tzinfo=timezone.utc)
        except ValueError:
            d = None
        by_id[vid] = (views, dur, d)
    for v in needs:
        info = by_id.get(v["id"])
        if not info:
            continue
        views, dur, d = info
        if v["views"] is None:
            v["views"] = views
        if v["duration_sec"] == 0:
            v["duration_sec"] = dur
        if v["date"] is None and d is not None:
            v["date"] = d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--include-shorts", action="store_true")
    args = ap.parse_args()

    channels = parse_competitors()
    print(f"Scanning {len(channels)} channels (last {args.days} days)...", file=sys.stderr)

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    all_videos = []

    for url in channels:
        handle = channel_handle(url)
        print(f"  -> @{handle}", file=sys.stderr)
        name, subs = fetch_channel_followers(url)
        vids = fetch_flat_videos(url, args.limit)
        if not vids:
            print(f"     (no videos returned)", file=sys.stderr)
            continue
        # Enrich any video where flat-playlist didn't include view_count.
        enrich_missing_views(vids)
        # Drop rows still missing views (rare — usually private/deleted).
        vids = [v for v in vids if v["views"] is not None]
        if not vids:
            print(f"     (no usable views)", file=sys.stderr)
            continue
        avg = sum(v["views"] for v in vids) / len(vids)
        for v in vids:
            v["channel_name"] = name or handle
            v["subscribers"] = subs
            v["channel_avg"] = avg
            v["outlier"] = v["views"] / avg if avg else 0
            denom = max(subs, 1000)
            size_factor = math.log10(1_000_000 / denom)
            v["size_factor"] = round(size_factor, 3)
            v["adjusted"] = round(v["outlier"] * size_factor, 3)
            v["handle"] = handle
        all_videos.extend(vids)
        print(f"     subs={subs:,} avg_views={int(avg):,} videos_kept={len(vids)}", file=sys.stderr)

    recent = []
    for v in all_videos:
        if v["date"] is None:
            continue
        if v["date"] < cutoff:
            continue
        if not args.include_shorts and 0 < v["duration_sec"] < 60:
            continue
        recent.append(v)

    recent.sort(key=lambda v: v["adjusted"], reverse=True)

    print(f"\nTotal recent videos: {len(recent)}", file=sys.stderr)

    out = []
    for v in recent[:args.top]:
        out.append({
            "title": v["title"],
            "channel": v["channel_name"],
            "handle": "@" + v["handle"],
            "subscribers": v["subscribers"],
            "views": v["views"],
            "channel_avg": int(v["channel_avg"]),
            "outlier": round(v["outlier"], 2),
            "size_factor": v["size_factor"],
            "adjusted": v["adjusted"],
            "date": v["date"].strftime("%Y-%m-%d"),
            "duration_sec": v["duration_sec"],
            "url": v["video_url"],
        })
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
