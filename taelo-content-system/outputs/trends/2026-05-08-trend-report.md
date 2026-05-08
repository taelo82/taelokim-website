# Trend Report — 2026-05-08

**Scan command:** `python3 scripts/trend_scan_weekly.py --days 3 --top 25 --limit 25`
**Window:** 2026-05-05 → 2026-05-08 (3 days, post-Brad)
**Channels scanned:** 24 (rows 1–24 of `brand/competitors.md`)
**Recent videos in window:** 25
**Outliers ≥1.0x:** 1
**Outliers ≥2.0x (strong):** 0

---

## ⚠️ Headline: No strong outlier this window

Top adjusted score is **1.108** (Chase AI, 1.21x raw). Per the agent spec, "strong outlier" = 2x+; this window has none. Two structural reasons:

1. **3-day window is too tight for late-week posts.** Most candidates were posted May 7 or May 8 — ≤24h old at scan time. Their view counts are still climbing toward channel-avg, so the ratio is artificially deflated. (Brad's own May 8 video sits at 0.13x for the same reason.)
2. **The week is genuinely soft.** Even videos posted May 6 (now ~48h old) sit between 0.66x and 1.21x — no breakout. Several creators dropped Codex and Hermes-Agent reactions that aren't outpacing their own averages.

**Recommendation:** Either (a) re-run with `--days 7` tomorrow once the May 6–8 videos have had time to settle, or (b) lean on the "Trends Spotted" section below — three themes are clearly forming even if no individual video has outliered yet.

---

## 🏆 Top Pick (weak — read with the warning above)

**"Stop Using Claude Code Without an Agentic OS"** — Chase AI

| Field | Value |
|---|---|
| Channel | Chase AI (@Chase-H-AI) |
| Subscribers | 121,000 |
| Views | 59,094 |
| Channel avg (30d) | 48,922 |
| Outlier | **1.21x** (below "strong outlier" 2x threshold) |
| Size factor | 0.917 |
| Adjusted | **1.108** |
| Posted | 2026-05-06 (≈48h old at scan) |
| Duration | 17:29 |
| URL | https://youtu.be/Bgxsx8slDEA |

**Why it's the top pick:** Only positive outlier in the window. Mid-size channel (121K) means size factor doesn't punish or boost much — the 1.21x is real outperformance, not a small-channel artifact. "Agentic OS" framing is a fresh angle, not yet saturated.

**Taelo angle (operator POV):** Two viable directions —
- **"I tested 3 'Agentic OS' setups for a week — here's what actually shipped"** — operator POV teardown, contrasts marketing claims with measurable wins.
- **"Why I'm Not Buying the 'Agentic OS' Frame (Yet)"** — contrarian take. Risk: too soon to be contrarian when the term hasn't fully landed; could come off as gatekeeping.

**Urgency:** Medium. "Agentic OS" as a term is hot this week but hasn't broken through to mid-channels yet. 7–10-day window before saturation if Chase's video continues climbing.

**Caveat:** 1.21x is barely above noise. If you'd rather wait, see the trends below — "Hermes Agent" and "Claude Video reactions" are louder signals at the trend level even though no single video has outliered yet.

---

## Runner-Ups (all sub-1.0x outlier — not real picks, included for context)

| # | Title | Channel | Views | Avg | Outlier | Adjusted | Posted | URL |
|---|---|---|---|---|---|---|---|---|
| 2 | Claude Video Just Changed Content Creation Forever… | Brock Mesarich | 41,211 | 53,175 | 0.78 | 0.762 | 2026-05-06 | https://youtu.be/k8igQH7SLwI |
| 3 | How I Vibe Coded a $900K App in 13 Minutes (Claude Design + Codex) | Jason Lee | 15,400 | 16,554 | 0.93 | 0.709 | 2026-05-07 | https://youtu.be/Z6C4CY2rLp4 |
| 4 | Claude Video Editing just got MASSIVELY better (Hyperframes V2) | RoboNuggets | 18,960 | 28,564 | 0.66 | 0.555 | 2026-05-07 | https://youtu.be/4E2I_NJkzhI |
| 5 | Hermes Agent might have just killed OpenClaw | Alex Finn | 70,207 | 94,804 | 0.74 | 0.521 | 2026-05-07 | https://youtu.be/Bg-IPiql7x8 |

None of these clear the 1.0x line. They're listed only because they're the next-highest by adjusted score. Don't treat as recommendations.

---

## Honorable Mentions (none qualify)

No videos in the window cleared the 1.5x threshold for honorable mentions. Skipping this section honestly rather than forcing weak picks.

---

## 🔥 Trends Spotted (this is where the real signal is)

Even though no individual video outliered, the **topic clustering** across the 25 videos is loud. Three themes:

### 1. "Hermes Agent" is the new shiny — 3 videos in 3 days

- Alex Finn: "Hermes Agent might have just killed OpenClaw" (198K, 70K views, 0.74x)
- David Ondrej: "100 hours of Hermes Agent lessons in 46 minutes" (376K, 32K views, 0.62x)
- Dubibubii: "Did Hermes Agent just become the best open-source agent? (Tutorial)" (25K, 2.9K views, 0.08x)

**Pattern:** Three different creator sizes, three different framings (vs OpenClaw / lessons-learned / tutorial), all within 48h. None outliered yet but the *cluster* is what matters — Hermes Agent has reached the "everyone is making a video about it" phase. Window is open for an operator-POV "tested it for X days, here's what's actually different" angle, especially before the tutorial flood saturates SEO.

### 2. "Claude Video" reactions — already over-saturated

- Brock Mesarich: "Claude Video Just Changed Content Creation Forever…" (41K views, 0.78x)
- RoboNuggets: "Claude Video Editing just got MASSIVELY better (Hyperframes V2)" (19K, 0.66x)
- Jack Roberts: "Claude Video is Here… Automate Anything" (14K, 0.26x)

**Pattern:** Reaction-video saturation. None outliering. Taelo just shipped his own `/watch`-skill video, so this is adjacent territory but the clean operator-POV angle ("I built X with Claude Video, here's what broke") already exists in his pillar — not the *next* video.

### 3. "Codex vs Claude Code" — comparison fatigue setting in

- Jack Roberts: "How to use Codex Better than 99% of People" (12.7K, 0.24x)
- Chase AI: "STOP Using Claude Code OR Codex" (8K, 0.17x)
- Nate Herk: "Master 97% of Codex in 1 Hour (full course)" (32K, 0.28x)

**Pattern:** All under-performing their own averages. Audience seems tired of the binary "X is better than Y" framing. **Skip this trend.**

### 4. "Design.md / Claude Design" — quieter signal worth watching

- Greg Isenberg: "Google's Design.md is a design team in a file" (627K, 30K views, 0.22x)
- Jason Lee: "How I Vibe Coded a $900K App in 13 Minutes (Claude Design + Codex)" (15K, 0.93x)

**Pattern:** Two different creators, two different framings (file-as-team vs vibe-coded-app), within 48h. Greg's video is way under his average but the *concept* (declarative design specs) is novel. Worth tracking with `--days 7` next week.

---

## What I'm NOT Recommending (And Why)

- **All "Codex" videos** — saturation + audience fatigue (see Trend 3).
- **Hermes-Agent tutorials** — flood incoming. Tutorial format is already 3-deep in 48h. If Taelo wants in, the angle has to be teardown/operator-POV, not "how to install."
- **Claude Video reactions** — already shipped his own; chasing this further dilutes the freshly-published video's positioning.
- **Brad's May 8 video** ("How I'd Learn Claude From Scratch in 2026") — 0.13x. Below his own bar; could be just-posted noise but worth a re-check next week before riding his slipstream again.

---

## Constraint Check

- ⚠️ **Strong outliers exist:** No. Top is 1.21x; threshold is 2x.
- ✅ **Fits content pillars:** Top pick is AI tools / operator POV — yes.
- ✅ **Date data clean:** All 25 entries have valid dates (no "n/a"). Two-pass enrichment worked.
- ⚠️ **No weak picks forced:** Acknowledged the weakness up front; reported the 1.21x with full caveats; did not invent strength that isn't in the data.
- ⚠️ **Window may be too tight:** 3 days under-counts late-week posts. Re-run with 7 days recommended.

---

## Scan Coverage Note

`scripts/trend_scan_weekly.py` ran cleanly across all 24 channels. Subscriber counts and channel-avg views all populated. No channel returned 0 videos. Two channels had `videos_kept` <25 (Brad: 16, Dubibubii: 24) — within tolerance.

---

## Hand-off (conditional)

If Taelo green-lights the Chase AI top pick despite the weak signal, **Script Writer (agent 03)** should pick up:
- **Topic:** Operator POV teardown of "Agentic OS" frameworks (test 2-3, contrast claims vs results)
- **Format:** ~10–12 min, cold open with the "1 worked, 2 didn't" hook
- **Source video:** https://youtu.be/Bgxsx8slDEA (Chase AI, for context only — do not name in script body per reaction-video rule; shoutout in Beat 9 outro only)
- **Companion run:** `/watch https://youtu.be/Bgxsx8slDEA` to extract the actual claims being made before testing them

**Recommended alternative:** Defer Script Writer 24–72h, re-run Trend Scout with `--days 7`, and reassess. The Hermes-Agent cluster is likely to throw a real outlier in the next 2–3 days as the early-posted videos mature. Fresher signal beats forcing a 1.21x pick now.

---

## Files

- Raw scan: `outputs/trends/2026-05-08-scan-results.json`
- Scan log: `outputs/trends/2026-05-08-scan.log`
- This report: `outputs/trends/2026-05-08-trend-report.md`
