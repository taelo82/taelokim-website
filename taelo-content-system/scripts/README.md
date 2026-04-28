# Scripts

## Trend Scout — two ways to run

### Option B: `trend_scan.py` (yt-dlp, no API key)
Default. Works immediately, scrapes channel pages.
```bash
python3 scripts/trend_scan.py --days 14 --top 25 --limit 20
```
- ✅ No API key needed
- ✅ Free, unlimited
- ⚠️ Upload dates sometimes "n/a" (yt-dlp limitation on flat-playlist mode)
- ⚠️ Channel page scraping can be rate-limited if run too often

### Option A: `trend_scan_api.py` (YouTube Data API v3)
Setup once, then more reliable.
```bash
# 1. Get an API key
#    https://console.cloud.google.com/apis/credentials
#    Enable "YouTube Data API v3" first
# 2. Configure
cp .env.example .env  # fill in YOUTUBE_API_KEY
pip3 install --user requests python-dotenv
# 3. Run
python3 scripts/trend_scan_api.py --days 14 --top 25 --limit 20
```
- ✅ Accurate upload dates
- ✅ Subscriber counts (size-adjusted scoring becomes possible)
- ✅ Stable, no scraping
- ⚠️ ~1,300 quota units per scan; free daily quota is 10,000

## How to add a channel
Edit `brand/competitors.md` and drop the channel URL into the table. Both scripts auto-pick it up.

## Output
JSON to stdout. Pipe into the trend report or read as-is.
