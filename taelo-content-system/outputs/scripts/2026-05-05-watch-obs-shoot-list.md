# OBS shoot list — `/watch` reaction video

> Your personal shooting checklist. Every screen capture you'll layer under face-cam + VO, organized so you can knock out related shots in single OBS sessions instead of jumping between setups.
> Source script: [2026-05-04-watch-skill-script.md](2026-05-04-watch-skill-script.md). Beat 3 cut detail: [2026-05-05-watch-beat3-editor-cut.md](2026-05-05-watch-beat3-editor-cut.md).

---

## OBS quick setup

- **Resolution**: 2560×1440 (or 1920×1080 if your machine struggles). Terminal text needs the headroom — you'll zoom into specific lines in post.
- **Bitrate**: 25–40 Mbps CBR. Low bitrate destroys terminal text in compression.
- **Source types you'll use**:
  - **Display Capture** for `/watch` live runs (cursor + multi-window).
  - **Window Capture** for isolated single-app shots (Anthropic console, GitHub repo).
  - **Browser Source** if you want clean dashboard re-renders (optional).
- **Show cursor**: ON for terminal demos. OFF for browser zooms where you don't want a stray pointer.
- **Recording format**: MKV (won't lose footage if OBS crashes). Remux to MP4 in OBS after.
- **Scene template**: build one OBS scene per group below so you're not rebuilding sources mid-shoot.

---

## Shoot in this order (groups setups together — saves you ~40 min of context-switching)

### Session A — Claude Code terminal (one OBS window the whole session)

Open a fresh Claude Code session, dark theme, font ~16pt. Have the URLs and demo files queued.

| # | Beat | Shot | Action | Target length |
|---|---|---|---|---|
| A1 | Beat 2 | `/watch` typed clean | Type `/watch https://www.youtube.com/watch?v=wkv2ifxPpF8` slowly. Hit enter. Let it run all the way through. **This is the hero shot.** Wall-clock visible somehow (menu-bar clock works). | 90s raw |
| A2 | Beat 2 | "Sorry, I can't watch the video" baseline | Open a *different* Claude (claude.ai or a base model in Claude Code without the skill installed). Ask: "summarize this video https://www.youtube.com/watch?v=wkv2ifxPpF8". Capture the refusal. | 15s |
| A3 | Beat 4 (easy path) | `/plugin marketplace add bradautomates/claude-video` typed live, then `/plugin install watch@claude-video`, then a restart. | 30s |
| A4 | Beat 4 (messy path) | `uv tool install --pre 'yt-dlp[default]'` running. Then `deno --version` to prove Deno is installed. | 20s |
| A5 | Beat 4 (proof) | `/watch` running on a YouTube video successfully **after** the patch. Just need 5 seconds of "it works". | 10s |
| A6 | Beat 7 | `/watch` running on the current week's Trend Scout top pick. Live. | 60s |
| A7 | Beat 3 (B-roll for face-cam already shot) | Re-run `/watch` on the Gary Tan URL silently — purely for picture-in-picture under your existing Beat 3 face-cam take. You already have `/tmp/watch-gstack/` if you want to skip this and just screencap the cached frames + output instead. | 60s or skip |

### Session B — Browser captures (one OBS scene, browser full-screen)

Chrome/Safari, no extensions visible, no bookmarks bar, clean profile if possible.

| # | Beat | Shot | Action | Target length |
|---|---|---|---|---|
| B1 | Beat 1 | YouTube AI-tool thumbnail flood | Open YouTube, search "Claude Code", scroll the results page fast. Capture the rapid thumbnail flood. Cut as a flicker montage in post. | 30s raw |
| B2 | Beat 4 | Groq dashboard signup → API keys page → key creation → Dashboard landing | Walk the full flow in real time. Slow, deliberate clicks. | 90s |
| B3 | Beat 6 | Anthropic Console — Cost page showing `USD 0.00` / "No data" / Month-to-date. **You already have this screenshot — re-capture as a video pan with cursor for motion.** | 15s |
| B4 | Beat 6 | Groq Dashboard — Usage tab showing `$0.02 USD` total, Whisper-large-v3 line item. | 15s |
| B5 | Beat 6 | Groq Logs — the 2-line whisper-large-v3 entries (247 audio sec each, 200 OK). | 10s |
| B6 | Beat 9 | GitHub: `bradautomates/claude-video` repo landing page. Scroll README. | 20s |
| B7 | Beat 9 | Brad's source video thumbnail on YouTube (`youtu.be/QZMljuD10sU`). | 5s |

### Session C — File system / VS Code (one OBS scene, VS Code full-screen)

VS Code with the `taelokim-website` repo open. Dark theme, sidebar visible.

| # | Beat | Shot | Action | Target length |
|---|---|---|---|---|
| C1 | Beat 1 | Old screenshot-frames-into-Claude story | Open any old chat where you pasted screenshots one-by-one (Anthropic Console → Logs would have these). If no real footage exists, skip — VO carries it. | 15s or skip |
| C2 | Beat 4 | The patched `~/.claude/skills/watch/scripts/download.py` opened in VS Code. Highlight the `WATCH_COOKIES_BROWSER` and player_client lines. | 15s |
| C3 | Beat 7 | The week's trend report markdown ([2026-05-04-trend-report.md](../trends/2026-05-04-trend-report.md)) scrolling. Highlight the top-pick row. | 20s |
| C4 | Beat 7 | File-tree pan: `outputs/trends/` → click into the saved `/watch` summary file. Show it. | 15s |
| C5 | Beat 8 | Markdown competitive-intel library file growing — entries with topic tags, source links, summaries. **You'll need to actually have this file built before you can shoot it** — see "Things to build first" below. | 30s |
| C6 | Beat 8 | VS Code search (⌘⇧F) finding a specific competitor's hook breakdown from 3 weeks ago. Type the search, watch results populate, click into one. | 20s |

### Session D — Stock / overlay captures

Quick browser captures, no narration.

| # | Beat | Shot | Action | Target length |
|---|---|---|---|---|
| D1 | Beat 5 | Quick cuts of the public yt-dlp GitHub repo, FFmpeg landing page, Whisper docs — proof of "two old free tools doing the heavy lifting". | 20s |
| D2 | Beat 5 (firehose) | Anthropic / OpenAI / Google release blog posts dated within the last 7 days. Just open the index pages and scroll. | 30s raw |
| D3 | Beat 9 | YouTube subscribe button hover on your own channel. Standard end-card asset. | 5s |

---

## Things to build/animate before you shoot (not OBS)

These don't exist yet — design them in Figma / Keynote / After Effects (whichever is fastest for you), then drop into the timeline.

| # | Beat | Asset | Notes |
|---|---|---|---|
| X1 | Beat 5 | Pipeline flow diagram | Boxes: `URL → yt-dlp → FFmpeg → frames + audio → captions OR Whisper → Claude → structured output`. Keynote builds this in 10 min. |
| X2 | Beat 8.5 | "Two parts left" whiteboard animation | Three columns: **Filming** (locked, human icon), **Editing** (locked, scissors/taste icon), **Research/Scripting** (unlocking, `/watch` logo punching through). Hand-drawn aesthetic > polished. |
| X3 | Beat 4 | Split-screen "clean install vs SABR errors" overlay frame | Just a 50/50 vertical split graphic with labels. Composite over A3 + a screen recording of failed yt-dlp output. |
| X4 | Beat 1 | "5–10 minutes wasted" overlay text + progress bar | Lower-third style. Use over a sped-up YouTube video timeline. |

---

## Reusable assets you already have

Don't re-shoot these — they're cached in `/tmp/`:

- `/tmp/watch-gstack/frames/` — 60 frames of Gary Tan's GStack video. Usable as B-roll under Beat 3.
- `/tmp/watch-taelo-take/full-output.txt` — the `/watch` analysis of your own face-cam take. Usable as picture-in-picture during Beat 3 meta-callout.
- [outputs/scripts/2026-05-04-watch-demo-output-gstack.md](2026-05-04-watch-demo-output-gstack.md) — the polished structured output from Beat 3. Can be displayed full-screen as the "what Claude returned" reveal.

---

## Things you have to build *first* (blocks shooting)

| # | What | Why blocking | Effort |
|---|---|---|---|
| P1 | The Beat 8 markdown competitive-intel library file (the searchable archive of every `/watch` output, tagged by topic) | Beat 8's whole visual story is "look at this growing library." If it doesn't exist, you can't shoot C5 or C6. | 30–60 min — set up `outputs/intel/` directory, drop the 3 existing `/watch` runs as entries with frontmatter (topic, source URL, date, summary), commit. |
| P2 | Beat 6 numbers re-verified day-of-shoot | Your `$0.00 / $0.02` numbers are accurate as of today (2026-05-05) but may drift if you run `/watch` heavily before recording. | 2 min — re-check both dashboards on shoot day, update Beat 6 line if needed. |

---

## Total OBS time budget

- Session A (Claude Code): ~30 min
- Session B (Browser): ~25 min
- Session C (VS Code / file system): ~20 min
- Session D (Stock): ~10 min
- **Total raw OBS shooting: ~85 min** (one good afternoon)

Plus build time for X1–X4 animations and P1 (intel library): ~2 hours.

---

*Generated 2026-05-05 from the locked script + Beat 3 cut guide.*
