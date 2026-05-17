# Filler shot index — Anthropic Same-Day Switch (2026-05-15)

Each `.png` is a **search-result grid** captured from Pexels / Giphy / Tenor. Pick the specific clip in the NLE — open the search URL, find your chosen tile, download.

Density target: every 8–15 sec of face-cam should have a filler cut (PLAN.md §2b).

| # | Beat / cue | Grid screenshot | Search URL | Source license |
|---|---|---|---|---|
| 01 | Cold open · "walked out in front of every tech reporter" | `01-coldopen-press-conference-pexels.png` | https://www.pexels.com/search/videos/press%20conference/ | Pexels (free, no attribution) |
| 02 | "Behind our back" · sneaky framing | `02-sneaky-giphy.png` | https://giphy.com/search/sneaky-behind-back | Giphy (fair use) |
| 03 | "$5K → $200" · money disappearing | `03-money-fire-pexels.png` | https://www.pexels.com/search/videos/money%20on%20fire/ | Pexels |
| 04 | "Two a.m., agent silently dies" | `04-robot-crash-giphy.png` | https://giphy.com/search/robot-crash | Giphy |
| 05 | "Weasel move" (literal) | `05-weasel-pexels.png` | https://www.pexels.com/search/videos/weasel/ | Pexels |
| 06 | "OpenClaw bill shock — lived through it" | `06-this-is-fine-giphy.png` | https://giphy.com/search/this-is-fine-dog | Giphy |
| 07 | "Community Noted within hours" | `07-fact-check-giphy.png` | https://giphy.com/search/fact-check-stamp | Giphy |
| 08 | "Three subscription changes in six weeks" | `08-calendar-flip-pexels.png` | https://www.pexels.com/search/videos/calendar%20pages/ | Pexels |
| 09 | Move 1 — "Bookmark the page" | `09-bookmark-tenor.png` | https://tenor.com/search/bookmark-page-gifs | Tenor (fair use) |
| 10 | Move 2 — "Get an API key, set a budget alert" | `10-alarm-giphy.png` | https://giphy.com/search/alarm-clock-ringing | Giphy |
| 11 | Friday reset closer — "market correcting in real time" | `11-stock-ticker-pexels.png` | https://www.pexels.com/search/videos/stock%20market%20ticker/ | Pexels |
| 12 | Outro CTA — subscribe / like prompt | `12-subscribe-giphy.png` | https://giphy.com/search/subscribe-button-click | Giphy |

## How to use this in the NLE

1. Drop a `.png` into a preview window to scan candidates
2. Click the search URL to open Pexels/Giphy/Tenor
3. Locate the tile you picked, download:
   - **Pexels videos**: click the tile → "Free Download" → MP4 (1080p sufficient for B-roll)
   - **Giphy**: click → "Media" → download MP4 (NOT GIF — MP4 cleaner in NLEs)
   - **Tenor**: click → "Share" → download MP4
4. Drop into the timeline at the beat. Cut to face-cam, cut to filler (1–2 sec), cut back. Don't dwell.

## License recap (PLAN.md §8)

- **Pexels** — free for commercial use, no attribution required. Safe.
- **Giphy / Tenor** — standard YouTube fair-use for short reaction-style cuts. Keep clips ≤3 sec, no monetization of the meme itself.
- **AVOID** any Shutterstock/Getty/Alamy thumbnails that may have leaked into a grid — Google Image search sometimes mixes them in. Pexels/Giphy/Tenor native results are all clean.

## Coverage gap

This is **12 candidates → 12 beats**. PLAN.md §2b targets 40–60 filler cuts across the 10-min video (every 8–15 sec). Realistically Taelo will reuse the same clip across multiple cuts and add 5–10 more queries during edit. The "missing" categories:

- "Hands typing fast" — for the bookmark / API-key / measure scenes
- "Server room / racks" — for the "API rates" reveal
- "Confused face" reaction — for the Pocock-can't-decode beat
- "Calendar countdown" — for "June 15th" mentions
- "Phone notification" — for the "$10/cancelled-screenshot" closer

Run `/tmp/cap.sh` with new URLs to add. The helper is preserved at `/tmp/cap.sh` until the session ends; copy it to `taelo-content-system/scripts/` if you want it permanent.
