# Final assembly guide — `/watch` reaction video

> Beat-by-beat punch list of which take, which timestamp range to cut into the final edit. Use this as your editor's working doc.

---

## Source files

| ID | File | Duration | Covers |
|---|---|---|---|
| F1 | `raw-takes/AI Can't Watch Videos_ Our Solution Revealed!.mp4` | 3:37 | Beat 1 |
| F2 | `raw-takes/Cloud Code Watches Videos_ Revolutionize Your Research!.mp4` | 17:09 | Beats 2, 4, 5, 6, 7, 8, 8.5, 9 |
| F3 | `~/Movies/2026-05-04 19-20-24.mov` | 4:07 | Beat 3 (original take) |
| F4 | `~/Movies/2026-05-04 19-32-59.mov` | 6:17 | Beat 8.5 alt + Beat 3 meta-callout |
| F5 | `~/Movies/2026-05-04 19-40-13.mov` | 0:37 | Beat 9 sign-off tag (optional) |

---

## Cut sequence (in shipping order)

| Beat | Source | Timestamp range | Notes | Final length |
|---|---|---|---|---|
| **1** | F1 | 00:06–03:36 (with internal cuts per [take-review-beat-1](2026-05-06-watch-take-review-beat-1.md)) | Apply 14 internal cuts (retake duplicates, false starts). Keep 3 ad-libs: producer analogy, "Cloud talking by the way," small-window urgency. | ~2:00–2:30 |
| **2** | F2 | 00:00–01:28 | Use limitless-pill cold open. Keep recursive callback ("even this recording"). Cut "for now" duplicate at 01:19. | ~50s |
| **3** | F3 | per [beat3-editor-cut.md](2026-05-05-watch-beat3-editor-cut.md) | Original demo take + 4 VO pickups. Layer screen-recording B-roll. | ~110s |
| **4** | F2 | 01:29–04:25 | **CRITICAL CUT**: drop the "tello automates" wrong-name line at 02:20 — viewers will copy-paste a broken command otherwise. Use 02:15 "bradautomates" version. Keep "I didn't even know what this was either" ad-lib (humanizes). | ~120s |
| **5** | F2 | 04:25–05:05 | Clean. Use as-is. | ~35s |
| **6** | F2 | 05:06–06:38 | Keep Groq-subscription ad-lib (06:11–06:27) — strongest proof of "actually free." Use "many videos" framing (06:03), no need to update count separately. Trim 3 stutters. | ~60s |
| **7** | F2 | 06:38–08:42 | Use **40+ YouTubers** (07:11) version, drop 24 version (06:56). Keep descending team-size pattern (40 → 20 → 5). End on "watches the videos for you" — drop trailing 08:33–08:42 incomplete sentence. | ~75s |
| **8** | F2 | 08:54–12:27 | Major expansion vs script. Keep ALL ad-libs: Karpathy reference, agent-fooled-by-views insight, "second brain that's all hype." Trim 2 stutters. | ~110s |
| **8.5** | **PATH A (Recommended)**: F2 12:27–15:12 + F4 ~05:48 splice | Use polished take F2 as the main body; splice the "executive producer" live quote from F4 (`19-32-59.mov` ~5:48–6:02) as the closing line before transitioning to Beat 9. Keep Hormozy reference, "people can tell by the views," and "you're very early" closer. | ~110s + ~15s splice |
|  | **PATH B (cleanest)**: F2 12:27–15:12 only | One-source. Skip the live splice. | ~110s |
|  | **PATH C (most authentic)**: F4 ~02:00–02:22 + ~05:48–06:15 only | Live take. Skip F2 polished take. Loses Hormozy + early-mover lines. | ~50s |
| **9** | F2 | 15:12–17:09 | Use second Brad shoutout (15:42), drop first attempt. Keep cross-promo CTA (16:31–16:50). Keep one "comment below what you want to see next" (~17:02). Drop trailing "bye bye thank you." | ~70s |

---

## Total final runtime estimate

- Beat 1: 2:30
- Beat 2: 0:50
- Beat 3: 1:50
- Beat 4: 2:00
- Beat 5: 0:35
- Beat 6: 1:00
- Beat 7: 1:15
- Beat 8: 1:50
- Beat 8.5 (Path A): 2:05
- Beat 9: 1:10
- **Total: ~15:00**

**Over the 10–12 min sweet spot in voice.md.** Three options:

1. **Trim ad-libs in Beats 6 + 8** (drop the Groq-subscription paragraph and the agent-fooled-by-views paragraph) → saves ~50s → lands ~14 min. Still long.
2. **Drop Path A splice in Beat 8.5**, use Path B → saves ~15s → marginal.
3. **Hard call**: drop one entire beat. Beat 5 (under the hood) is the most cuttable — if `/watch` already feels magic from Beat 3 demo, viewers don't need the architecture explanation. Could fold a 10-sec version into Beat 4. Saves ~30s.

**Recommended target: 13:00–13:30** — accept it's longer than the canonical sweet spot because the ad-libs are genuine value-adds. The audience for this kind of content (operators, builders) tolerates 13-min videos when the density is high.

---

## Critical edit gotchas

1. **02:20 in F2** — "slash plugin marketplace at **tello** automates slash cloud video" is the wrong command. **Hard cut**. Use 02:15 with `bradautomates`.
2. **F2 frame coverage is sparse** — 80 frames over 17 minutes means I sampled every ~13 seconds. Specific visual moments aren't validated. If you remember anything visually weird mid-take, scrub it manually.
3. **Whisper transcript artifact** — "Cloud" = Claude, "Grok" = Groq throughout. Your audio is correct.
4. **Beat 1 is in F1, not F2** — they're separate files. F2 starts at Beat 2 with the limitless-pill ad-lib.

---

## Companion docs

- Per-beat detail: [take-review-beat-1.md](2026-05-06-watch-take-review-beat-1.md), [take-review-beats-2-9.md](2026-05-06-watch-take-review-beats-2-9.md)
- Beat 3 specifically: [beat3-editor-cut.md](2026-05-05-watch-beat3-editor-cut.md)
- Beat 8.5 splice source: [take2-review.md](2026-05-05-watch-take2-review.md)
- OBS B-roll capture list: [obs-shoot-list.md](2026-05-05-watch-obs-shoot-list.md) — face-cam done, OBS still pending
- Locked script (canonical VO): [watch-skill-script.md](2026-05-04-watch-skill-script.md)

---

*Generated 2026-05-06. Two new `/watch` runs cost ~$0.05 on Groq Whisper. Total verified `/watch` runs across this project: 7.*
