# Resume — handoff for next session

> Last session: 2026-05-04. Stopped because of weekly token limits, not because anything was broken.

## What we're shipping
A YouTube reaction/replication video about the **`/watch` Claude Code skill** (free skill that lets Claude analyze any video). Modeled on the structure of the original walkthrough at https://youtu.be/QZMljuD10sU, but with Taelo's unique angles: the YouTube SABR install caveat, Trend Scout × `/watch` operator pipeline, and solo-operator competitive intelligence framing.

## Done

| Status | Item |
|---|---|
| ✅ | Trend Scout expanded from 13 → 24 channels ([brand/competitors.md](brand/competitors.md)) |
| ✅ | Weekly scan run + ranked report ([outputs/trends/2026-05-04-trend-report.md](outputs/trends/2026-05-04-trend-report.md)) |
| ✅ | Top pick locked: Brad Bonanno's `/watch` video, 3.83x outlier on a 6,740-sub channel |
| ✅ | Brad's `/watch` skill installed at `~/.claude/skills/watch/` and validated end-to-end |
| ✅ | YouTube SABR block worked around: Python 3.11 + uv + yt-dlp nightly + Deno + curl_cffi + cookies — copy-paste install at [outputs/scripts/2026-05-04-watch-install-description.md](outputs/scripts/2026-05-04-watch-install-description.md) |
| ✅ | Demo target locked: Gary Tan's GStack video (https://www.youtube.com/watch?v=wkv2ifxPpF8). Pre-pulled transcript + 60 frames |
| ✅ | Live `/watch` output produced for Beat 3 ([outputs/scripts/2026-05-04-watch-demo-output-gstack.md](outputs/scripts/2026-05-04-watch-demo-output-gstack.md)) |
| ✅ | Full polished script drafted, de-Bradified, demo target locked ([outputs/scripts/2026-05-04-watch-skill-script.md](outputs/scripts/2026-05-04-watch-skill-script.md)) |
| ✅ | Beat 3 face-cam take recorded by Taelo, processed via `/watch`, review notes written ([outputs/scripts/2026-05-04-watch-take-review.md](outputs/scripts/2026-05-04-watch-take-review.md)) |

## Open / next session

1. **Apply cuts + polish to Beat 3 take** per the take review (cut "May 5th today", "AI 3.0", and the Gary criticism; polish the `/review`/`/QA` rambling and the skills-repo line; add the meta-callout line before CTA)
2. **Record Beats 1, 2, 4-9** — script is locked, just need to shoot
3. **Pull Beat 6 real numbers** — the "$1/video, 10 videos/week" figures are placeholders; pull from Taelo's actual Anthropic dashboard before recording
4. **B-roll capture list** for editing:
   - Beat 4 split-screen: clean install vs. SABR errors flying
   - Beat 4 patch sequence: `uv tool install`, Deno install, `/watch` succeeding after patch
   - Beat 7: trend report MD scrolling, `/watch` running on top pick, structured output
   - Beat 8: markdown library file growing with topic tags + search
5. **Optional** — draft a tighter 60-second Beat 3 voiceover splicing the 5 best moments from the recorded take with screen-recording cues marked
6. **YouTube SABR fix** — yt-dlp ships a stable patch within days/weeks. When it does, the workaround patches in `~/.claude/skills/watch/scripts/download.py` may be removable. Re-test then.

## Pipeline state

- **Trend Scout**: [scripts/trend_scan_weekly.py](scripts/trend_scan_weekly.py) — supports `--rows N-N` flag for partial scans. Run with `python3 scripts/trend_scan_weekly.py --days 7 --top 30 --limit 25`.
- **Transcript fetcher**: [scripts/fetch_transcript.py](scripts/fetch_transcript.py) — uses youtube-transcript-api, no PO token needed for transcripts.
- **`/watch`** — installed at `~/.claude/skills/watch/`. Local patches in `download.py` are NOT in upstream — see memory `reference_watch_skill_install.md`. Invoke with `WATCH_COOKIES_BROWSER=chrome` env var for YouTube.
- **Groq API key** at `~/.config/watch/.env` — was pasted in chat, should be rotated when convenient (https://console.groq.com/keys).

## Files dashboard

### Script + scripts pipeline
- [outputs/scripts/2026-05-04-watch-skill-script.md](outputs/scripts/2026-05-04-watch-skill-script.md) — locked script (intro + 9 beats)
- [outputs/scripts/2026-05-04-watch-install-description.md](outputs/scripts/2026-05-04-watch-install-description.md) — copy-paste install for video description
- [outputs/scripts/2026-05-04-watch-demo-output-gstack.md](outputs/scripts/2026-05-04-watch-demo-output-gstack.md) — Beat 3 on-screen demo material
- [outputs/scripts/2026-05-04-watch-take-review.md](outputs/scripts/2026-05-04-watch-take-review.md) — Beat 3 face-cam take review (cuts/polish)

### Trend reports + raw scan data
- [outputs/trends/2026-05-04-trend-report.md](outputs/trends/2026-05-04-trend-report.md) — full ranked report
- [outputs/trends/2026-05-04-scan-results.json](outputs/trends/2026-05-04-scan-results.json) — rows 1-13 raw
- [outputs/trends/2026-05-04-scan-rows-14-24.json](outputs/trends/2026-05-04-scan-rows-14-24.json) — rows 14-24 raw

### Transcripts
- [outputs/trends/transcripts/QZMljuD10sU-brad-bonanno-pick.txt](outputs/trends/transcripts/QZMljuD10sU-brad-bonanno-pick.txt) — Brad's source video (private reference, not on-camera)
- [outputs/trends/transcripts/wkv2ifxPpF8-demo-target.txt](outputs/trends/transcripts/wkv2ifxPpF8-demo-target.txt) — Gary Tan GStack (Beat 3 demo source)
- [outputs/trends/transcripts/tn7zXRv3Xmo-jack-roberts-deepseek.txt](outputs/trends/transcripts/tn7zXRv3Xmo-jack-roberts-deepseek.txt) — runner-up
- [outputs/trends/transcripts/jQO9RAmy5lk-jason-lee-seedance.txt](outputs/trends/transcripts/jQO9RAmy5lk-jason-lee-seedance.txt) — earlier top pick (replaced by Brad)

### Brand + agent prompts
- [brand/competitors.md](brand/competitors.md) — 24 channels
- [brand/voice.md](brand/voice.md) — voice anchor (direct, raw, conversational, skeptical of hype)
- [agents/02-trend-scout.md](agents/02-trend-scout.md) — Trend Scout playbook

## Memory anchors (auto-loaded next session)

- `reference_watch_skill_install.md` — local install state + patches at risk
- `feedback_taelo_script_voice_polish.md` — clean to native English; preserve face-cam roughness
- `feedback_taelo_creator_mentions_in_reactions.md` — shoutout in outro, not body
- `feedback_taelokim_auto_push.md` — auto-push after batches of edits
- `feedback_taelokim_dashboard.md` — render asset dashboard at start + after big changes

## How to resume in a new session

Just open Claude Code with the `taelokim-website` repo open. The new session will load these memories automatically and read this RESUME.md if pointed at it. To prime fast: *"Resume the /watch reaction video. Read RESUME.md."*
