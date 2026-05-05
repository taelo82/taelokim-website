# Resume — handoff for next session

> Last updated: **2026-05-06**. Project is past script + face-cam shooting. Now in **edit + fork-publish + OBS-capture** phase.
> To prime fast in a new session: *"Read RESUME.md and resume the /watch reaction video."*

---

## What we're shipping
A YouTube reaction/replication video about the **`/watch` Claude Code skill** (originally Brad Bonanno's free skill). Taelo is forking it into `taeloautomates/claude-video` so viewers download his version (with bundled SABR install patches) — Brad gets shoutout in Beat 9 outro. Final target runtime: 12–14 min.

---

## Status (one-line)

| Phase | Status |
|---|---|
| Script + teleprompter | ✅ Locked, 9 beats + Beat 8.5 |
| Face-cam takes | ✅ All beats shot (across 5 files in `raw-takes/` + `~/Movies/`) |
| Take reviews | ✅ Per-beat keep/cut/polish for every beat |
| Final assembly guide | ✅ Editor's punch list ready |
| Beat 3 cut & shoot guide | ✅ Editor cuts mapped, 4 VO pickups defined |
| OBS / B-roll captures | 🔲 Not started — 4 batched sessions per `obs-shoot-list.md` |
| `taeloautomates/claude-video` GitHub fork | 🔲 **BLOCKING publish** — must exist before video goes live |
| Animations (Beat 5 pipeline diagram, Beat 8 split-screen, optional Beat 8.5 whiteboard) | 🔲 Need design |
| Editor pass (Premiere) | 🔲 Awaiting raw assembly |

---

## Open work for next session (priority order)

1. **🚨 Decide & execute the GitHub fork** (`taeloautomates/claude-video`)
   - Confirm GitHub username/org (`taeloautomates`? `taelo82`? new org?)
   - Fork or re-create from `bradautomates/claude-video` upstream
   - Bundle the SABR patches Taelo applied locally (in `~/.claude/skills/watch/scripts/download.py`)
   - Update `marketplace.json` + `plugin.json` with the new repo URL
   - Add README attribution to Brad
   - Test: `/plugin marketplace add taeloautomates/claude-video` + `/plugin install watch@claude-video` in a clean Claude Code instance
   - **Blocks**: video can't publish until this works
2. **Beat 8.5 path decision** — three options laid out in [final-assembly.md](outputs/scripts/2026-05-06-watch-final-assembly.md). Recommendation: **Path A** (polished take from F2 + executive-producer splice from F4 19-32-59).
3. **Trim plan** — current estimated final is ~14–15 min, target is 10–12. Options: drop Groq-subscription paragraph (Beat 6), drop agent-fooled-by-views paragraph (Beat 8), or drop Beat 5 entirely.
4. **OBS shoot day** — face-cam-first done, OBS still pending. 4 batched sessions, ~85 min total. Critical: capture the actual `/watch` install live for Beat 4 B-roll, including the new `taeloautomates/claude-video` invocation (depends on fork existing first).
5. **Animations** to design before final cut: Beat 5 pipeline diagram, Beat 8 split-screen "scheduled vs on-demand" overlay.
6. **YouTube SABR fix watch** — yt-dlp ships a stable patch within days/weeks. When it does, the workaround patches in `download.py` may be removable. Re-test then.

---

## Files dashboard

### Script + script artifacts
- [outputs/scripts/2026-05-04-watch-skill-script.md](outputs/scripts/2026-05-04-watch-skill-script.md) — locked canonical script (intro + 9 beats + 8.5)
- [outputs/scripts/2026-05-05-watch-teleprompter.md](outputs/scripts/2026-05-05-watch-teleprompter.md) — clean read-aloud copy of the script
- [outputs/scripts/2026-05-04-watch-install-description.md](outputs/scripts/2026-05-04-watch-install-description.md) — copy-paste install for video description (⚠️ still references `bradautomates` — update once fork exists)

### Take reviews + assembly
- [outputs/scripts/2026-05-04-watch-take-review.md](outputs/scripts/2026-05-04-watch-take-review.md) — Beat 3 take-1 review
- [outputs/scripts/2026-05-05-watch-take2-review.md](outputs/scripts/2026-05-05-watch-take2-review.md) — Beat 3 recursive takes review
- [outputs/scripts/2026-05-05-watch-beat3-editor-cut.md](outputs/scripts/2026-05-05-watch-beat3-editor-cut.md) — Beat 3 cut & shoot guide
- [outputs/scripts/2026-05-06-watch-take-review-beat-1.md](outputs/scripts/2026-05-06-watch-take-review-beat-1.md) — Beat 1 take review (from F1)
- [outputs/scripts/2026-05-06-watch-take-review-beats-2-9.md](outputs/scripts/2026-05-06-watch-take-review-beats-2-9.md) — Beats 2 + 4 + 5 + 6 + 7 + 8 + 8.5 + 9 (from F2)
- [outputs/scripts/2026-05-06-watch-final-assembly.md](outputs/scripts/2026-05-06-watch-final-assembly.md) — **the editor's punch list — open this when starting Premiere**

### Production guides
- [outputs/scripts/2026-05-05-watch-obs-shoot-list.md](outputs/scripts/2026-05-05-watch-obs-shoot-list.md) — OBS B-roll capture list, 4 batched sessions

### Source material (gitignored)
- `raw-takes/AI Can't Watch Videos_ Our Solution Revealed!.mp4` (F1) — Beat 1 face-cam, 3:37
- `raw-takes/Cloud Code Watches Videos_ Revolutionize Your Research!.mp4` (F2) — Beats 2–9 + 8.5 face-cam, 17:09
- `~/Movies/2026-05-04 19-20-24.mov` (F3) — Beat 3 original demo take, 4:07
- `~/Movies/2026-05-04 19-32-59.mov` (F4) — Beat 8.5 alt + Beat 3 meta-callout, 6:17
- `~/Movies/2026-05-04 19-40-13.mov` (F5) — Beat 9 sign-off tag, 0:37

### Trend reports + transcripts (reference only, not changing)
- [outputs/trends/2026-05-04-trend-report.md](outputs/trends/2026-05-04-trend-report.md) — full ranked report
- Transcripts in `outputs/trends/transcripts/`

---

## Conventions established this project

- **Path-sharing**: drop new takes into `taelo-content-system/raw-takes/`. Files are gitignored. In chat just say "the latest two" or "the May 6 ones" — the next session does `ls -lt raw-takes/` to pick by recency.
- **Auto-push**: every batch of file edits gets committed and pushed to `taelo82/taelokim-website` automatically (per memory).
- **Solo operator**: Taelo edits his own videos. Address shot lists / cut guides to him directly, never to a hypothetical "editor."
- **On-demand, not compounding**: never propose cron jobs / scheduled scrapers / "second brain library" patterns. Run agents fresh when hunting.
- **Reaction-video etiquette**: never name the source creator (Brad Bonanno) in script body. Shoutout lands in Beat 9 outro only.
- **Voice polish**: clean script drafts to native English; preserve face-cam roughness in actual takes.

---

## Memory anchors (auto-loaded if cwd = `~/Desktop/Content-engine`)

If the next session opens with `~/Desktop/Content-engine` as cwd, these auto-load:
- `feedback_taelokim_auto_push.md` — push after every batch
- `feedback_taelokim_dashboard.md` — render asset dashboard at session start + after major changes
- `feedback_taelo_script_voice_polish.md` — clean to native English; preserve face-cam roughness
- `feedback_taelo_creator_mentions_in_reactions.md` — shoutout in outro only
- `feedback_taelo_solo_editor.md` — Taelo edits his own videos
- `feedback_taelo_on_demand_not_compounding.md` — never propose cron jobs / compounding library patterns
- `reference_watch_skill_install.md` — local install state + patches at risk

If the next session opens with `~/Desktop/taelokim-website` as cwd (or anywhere else), the memories DO NOT auto-load. The new session needs to explicitly read them from `~/.claude/projects/-Users-ek-Desktop-Content-engine/memory/MEMORY.md`.

---

## Pipeline state (technical)

- **`/watch`** — installed at `~/.claude/skills/watch/`. Local patches in `download.py` (cookies + player_client override) are NOT in upstream — see `reference_watch_skill_install.md`. These need to migrate into the `taeloautomates/claude-video` fork.
- **Trend Scout** — [scripts/trend_scan_weekly.py](scripts/trend_scan_weekly.py) — supports `--rows N-N` flag for partial scans. Run with `python3 scripts/trend_scan_weekly.py --days 7 --top 30 --limit 25`.
- **Transcript fetcher** — [scripts/fetch_transcript.py](scripts/fetch_transcript.py) — uses youtube-transcript-api, no PO token needed.
- **Groq API key** at `~/.config/watch/.env` — was pasted in chat early on; rotate when convenient (https://console.groq.com/keys).

---

## Cost note

Across 7 verified `/watch` runs in this project: **Anthropic API $0.00 / Groq Whisper ~$0.07** (well under free tier). Beat 6 in the script reflects current numbers as of 2026-05-06. Re-pull both dashboards on shoot day if recording new costs into the cut.

---

## How to resume in a new session (lowest friction)

1. Open Claude Code with `~/Desktop/Content-engine` as cwd (so memories auto-load).
2. First message: *"Read RESUME.md at ~/Desktop/taelokim-website/taelo-content-system/RESUME.md and resume the /watch reaction video. Start with the open work in priority order."*
3. New session reads this file once → has full state. Keep new turns focused on one open-work item at a time so token bloat stays low.

If cwd is `~/Desktop/taelokim-website` instead, append to step 2: *"Also read MEMORY.md at ~/.claude/projects/-Users-ek-Desktop-Content-engine/memory/MEMORY.md to load the workflow memories."*
