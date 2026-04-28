#!/usr/bin/env python3
"""
Trend Scout — Option A (YouTube Data API v3).
Same logic as scripts/trend_scan.py but uses the official API for accurate
upload dates, channel subscriber counts, and rate-stable scanning.

Setup:
    1. Get an API key: https://console.cloud.google.com/apis/credentials
       (enable "YouTube Data API v3" for the project first)
    2. cp .env.example .env, fill in YOUTUBE_API_KEY
    3. pip3 install --user requests python-dotenv
    4. python3 scripts/trend_scan_api.py [--days 14] [--top 25]

Quota: ~100 units per channel scanned (1 channels.list + 1 search.list +
1 videos.list batch). 13 channels ≈ 1,300 units. Free tier = 10,000/day.
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dep: pip3 install --user requests python-dotenv")
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

API_KEY = os.environ.get("YOUTUBE_API_KEY", "").strip()
ROOT = Path(__file__).resolve().parent.parent
COMPETITORS_MD = ROOT / "brand" / "competitors.md"
BASE = "https://www.googleapis.com/youtube/v3"


def parse_competitors():
    text = COMPETITORS_MD.read_text()
    handles = re.findall(r"https://www\.youtube\.com/(@[\w\.\-]+)", text)
    seen, out = set(), []
    for h in handles:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out


def api_get(path, **params):
    params["key"] = API_KEY
    r = requests.get(f"{BASE}/{path}", params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def resolve_channel(handle):
    """Resolve @handle -> channelId + uploads playlist + sub count."""
    data = api_get("channels", part="snippet,statistics,contentDetails", forHandle=handle)
    items = data.get("items", [])
    if not items:
        return None
    it = items[0]
    return {
        "channel_id": it["id"],
        "title": it["snippet"]["title"],
        "subscribers": int(it["statistics"].get("subscriberCount", 0)),
        "uploads_playlist": it["contentDetails"]["relatedPlaylists"]["uploads"],
    }


def fetch_uploads(playlist_id, limit=20):
    data = api_get("playlistItems", part="contentDetails,snippet",
                   playlistId=playlist_id, maxResults=min(limit, 50))
    return [
        {
            "video_id": it["contentDetails"]["videoId"],
            "title": it["snippet"]["title"],
            "published_at": it["contentDetails"].get("videoPublishedAt"),
        }
        for it in data.get("items", [])
    ]


def fetch_video_stats(video_ids):
    """Batch call — videos.list accepts up to 50 IDs per call."""
    out = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        data = api_get("videos", part="statistics,snippet,contentDetails", id=",".join(batch))
        for it in data.get("items", []):
            out[it["id"]] = {
                "views": int(it["statistics"].get("viewCount", 0)),
                "likes": int(it["statistics"].get("likeCount", 0)),
                "duration": it["contentDetails"].get("duration"),
                "published_at": it["snippet"].get("publishedAt"),
            }
    return out


def main():
    if not API_KEY:
        sys.exit("YOUTUBE_API_KEY missing — copy .env.example to .env and fill it in.")

    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    handles = parse_competitors()
    print(f"Scanning {len(handles)} channels...", file=sys.stderr)

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    all_videos = []

    for handle in handles:
        print(f"  -> {handle}", file=sys.stderr)
        ch = resolve_channel(handle)
        if not ch:
            print(f"     (could not resolve)", file=sys.stderr)
            continue
        uploads = fetch_uploads(ch["uploads_playlist"], args.limit)
        if not uploads:
            continue
        stats = fetch_video_stats([u["video_id"] for u in uploads])
        rows = []
        for u in uploads:
            s = stats.get(u["video_id"], {})
            published = u["published_at"] or s.get("published_at")
            try:
                d = datetime.fromisoformat(published.replace("Z", "+00:00")) if published else None
            except (ValueError, AttributeError):
                d = None
            rows.append({
                "title": u["title"],
                "views": s.get("views", 0),
                "date": d,
                "id": u["video_id"],
                "channel": ch["title"],
                "subscribers": ch["subscribers"],
                "video_url": f"https://youtu.be/{u['video_id']}",
            })
        avg = sum(r["views"] for r in rows) / len(rows) if rows else 0
        for r in rows:
            r["channel_avg"] = avg
            r["outlier"] = (r["views"] / avg) if avg else 0
        all_videos.extend(rows)

    recent = [v for v in all_videos if v["date"] is None or v["date"] >= cutoff]
    recent.sort(key=lambda v: v["outlier"], reverse=True)

    out = []
    for v in recent[:args.top]:
        out.append({
            "title": v["title"],
            "channel": v["channel"],
            "subscribers": v["subscribers"],
            "views": v["views"],
            "channel_avg": int(v["channel_avg"]),
            "outlier": round(v["outlier"], 2),
            "date": v["date"].strftime("%Y-%m-%d") if v["date"] else "n/a",
            "url": v["video_url"],
        })
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
