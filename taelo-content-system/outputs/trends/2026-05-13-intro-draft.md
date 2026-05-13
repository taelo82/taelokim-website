# Intro Draft — Claude Code Agent View 24-Hour Operator Test (2026-05-13)

**Working titles (pick one for the test, A/B the thumbnail):**
1. *"I Ran 5 Claude Code Agents in Parallel for 24 Hours"*
2. *"Claude Code's `/goal` Command Is The Update You Missed"*
3. *"Claude Code Just Got A Mission Control — Here's What Shipped in 24 Hours"*

**Target length:** 8–11 min · **Format:** cold-open result → 24h timelapse → operator findings · **Lead time:** record tomorrow morning, publish 2026-05-15

**Why this pick** (carried over from trend report):
- 2-day-old release (May 11), `claude agents` and `/goal` are net-new search terms
- WorldofAI (217K subs) already shipped a *feature explainer* — 18K views in 24h — but the **operator-test lane is empty**
- Pillar-perfect: Claude Code, solo operator POV
- One-day prep, one-day record, one-day edit. 3x faster than skill-build videos.

**Voice rules (active for this script):**
- Polish to clean native cadence (face-cam takes can stay rough)
- ❌ Do NOT name WorldofAI / Anthropic / any creator in body
- ✅ Beat 9 outro shoutout: thank Anthropic team + WorldofAI's coverage
- Address the audience, not a hypothetical editor (Taelo edits his own videos)

**2026 algorithm rule active here:** First 30 seconds is now a hard ranking checkpoint. If <50% drop off by 0:30, distribution collapses. Cold-open delivers **the result**, not the setup.

---

## 🎬 COLD OPEN — 0:00 to 0:08 — the result first

> **Five Claude Code agents.**
> **Twenty-four hours.**
> **Three pull requests shipped, one agent stuck for six hours, and one trap that almost cost me my whole side project.**

*[B-roll: split-screen — `claude agents` dashboard with 5 rows pulsing → fast-cut to 3 green "merged" PR badges → freeze on a red "blocked" agent row]*

**Why this opens correctly:** Three specific numbers, one stakes line, zero preamble. Viewer knows by 0:08 what they're going to learn. Per 2026 algorithm: result-first → 90%+ retention through 0:30.

---

## 🪝 HOOK — 0:08 to 0:25 — what's new and why anyone should care

> Two days ago Claude Code shipped a feature called **agent view**. Type `claude agents` and you get a single dashboard of every session you've spun up — which ones are running, which ones are blocked waiting on you, which ones already finished. They also shipped a new command, `/goal` — you tell Claude what "done" looks like, and it just keeps working until it hits that condition.
>
> So I gave it a stress test. Five real codebases. Five real goals. Twenty-four hours, no babysitting.

*[B-roll: terminal open, type `claude agents` slowly → dashboard fills in → cursor hovers over the `/goal` indicator on one row]*

---

## 🎯 PROMISE — 0:25 to 0:38 — the contract

> In the next eight minutes you're going to see exactly what shipped in those 24 hours, which agent stalled and why, the one setup mistake that wiped two hours of work, and whether this actually replaces tmux and stacked terminal tabs — or whether it's another Research Preview that looks great in the demo and falls over in production.

*[B-roll: tmux grid → fade-cross to agent view dashboard → checkmark animation on three of five rows, red X on one]*

---

## 📋 The 24-hour test setup (0:38 to 1:30)

Show on screen:
1. The 5 codebases used (your taelokim-website, the content-system repo, the /watch fork, two others)
2. The 5 `/goal` strings you set (specific, measurable)
3. The hardware/laptop you ran it on
4. The one rule: **no interventions for 24 hours** (you check phone notifications only)

**Script beat:**
> Before we hit play — the rules. Five agents, five different repos. Each one gets a single `/goal` instruction, sized so it should be finishable. I'm not allowed to touch any of them for the next twenty-four hours. If an agent gets stuck, it gets stuck. If `/goal` mis-judges "done," we find out. Phone gets notifications only.

*[B-roll: typing each `/goal` command into a fresh session, then hitting `/bg` to send it to background — repeat ×5 with quick cuts]*

---

## 📦 Beat structure for the rest of the video

| Beat | Time | What it covers | B-roll |
|---|---|---|---|
| 4. The hour-1 check-in | 1:30–2:15 | First wait-on-input prompt comes in. Show the inline-reply flow. | Phone notification → laptop → agent view row turns yellow → reply inline |
| 5. The 6-hour stall | 2:15–3:30 | Which agent stalled, why, and how `/goal` handled (or failed) ambiguity | Screen-record of the failure mode, then the recovery prompt |
| 6. The 12-hour timelapse | 3:30–4:45 | Speed-ramped capture of the dashboard over 12h | 4x speed timelapse with timestamp overlay |
| 7. The 24-hour state | 4:45–6:00 | What actually got merged. Open each PR, show the diff. | Real PRs in GitHub, scroll through diffs |
| 8. The trap | 6:00–7:15 | The setup mistake that cost 2 hours (`/goal` interpreting "done" too literally on one task) | Annotate the bad prompt → show the fix → re-run |
| 9. Operator verdict + outro | 7:15–8:30 | Does this replace tmux? When to use it. When NOT to use it. Beat 9 shoutout. | Final dashboard frame → split-screen verdict card |

---

## 🎨 Claude Design intro brief (paste this into Claude Design)

> **Brief:** Build an intro graphic + animated lower-third for a YouTube video titled *"I Ran 5 Claude Code Agents in Parallel for 24 Hours"*. Solo creator (Taelo Kim) doing an operator-POV stress test of Anthropic's new Claude Code Agent View + `/goal` command.
>
> **Visual identity:**
> - Palette: Anthropic terminal aesthetic — deep slate (#0E1116) background, Anthropic coral/orange accent (#D97757) for the live/active state, soft cream (#F5F1EB) for body text, electric-blue (#3E7BFA) ONLY for the "completed" state badge
> - Foreground: a stylized terminal "agent view" dashboard — five horizontal rows stacked, each row has a status pill on the left, a session title in monospace, and a tiny pulsing dot on the right
> - Rows light up in sequence (top → bottom), each in a different status color: yellow (waiting on you), orange (running), green (done), red (blocked), gray (queued)
> - Above the dashboard: clock readout that animates from `00:00` to `24:00` over 4 seconds
> - Below the dashboard: a single line that types out — `> claude agents`
>
> **Animations needed:**
> 1. **0–2s open card:** dark slate fades up → clock starts at `00:00` → terminal prompt blinks
> 2. **2–4s reveal:** five dashboard rows slide in from the right, each lighting up its status pill
> 3. **4–5s timelapse:** clock spins to `24:00`, rows update their statuses (some flip green, one flips red)
> 4. **Lower-third (reusable):** thin slate bar with coral underline, monospace text "Taelo Kim · 24h Claude Code Test"
>
> **Style notes:**
> - Cinematic terminal aesthetic, NOT corporate dashboard
> - Monospace font (JetBrains Mono or Fira Code)
> - No stock-vector look — every element should feel hand-tuned
> - Don't add Anthropic logos (positioning as independent operator, not affiliate)
> - The status-pill colors are the **memorable visual** — exaggerate the saturation
>
> **Output formats requested:**
> - 16:9 intro card (3840×2160 PNG static "title frame" — the moment all 5 rows are visible)
> - Animated MP4 (5 sec, 4K, 60fps, transparent BG) for opening
> - Reusable lower-third PNG sequence (1080p, transparent)
> - Two 1280×720 thumbnail variants:
>    - **A:** terminal dashboard center, giant text "5 AGENTS · 24 HOURS" overlaid left
>    - **B:** face-cam Taelo expression on left half, dashboard with one red row on right, single word "STALLED" stamped diagonally

---

## 📋 Shot list (recording day — tomorrow morning, post 24h run)

1. **Cold-open piece-to-camera** (1 take, 8 sec) — deliver the three-number opening cold. Re-do until energy is right.
2. **Setup explainer (b-roll heavy)** — voiceover over actual screen-record of `claude agents` opening, the 5 sessions starting.
3. **Hour-1 check-in piece** — face-cam, 30 sec, react to the first agent waiting on input.
4. **The 6-hour stall walkthrough** — screen-record only, voiceover.
5. **The 12-hour timelapse** — 4x speed of the agent view dashboard, full-screen, music bed.
6. **The 24-hour reveal** — face-cam at 24:00 mark, open each PR in GitHub on screen, react live.
7. **The trap segment** — screen-record + annotated overlay, no face-cam (keep face-cam for emotional beats).
8. **Operator verdict** — face-cam, 60 sec, deliberate pacing. List 3 use cases where this wins, 2 where tmux still wins.
9. **Beat 9 outro** — face-cam, 45 sec. Shoutout Anthropic for the release + WorldofAI for their coverage video. Reminder to like/sub. Tease next video.

---

## 📌 SEO checklist

**Primary keywords (must appear in title, description, first 3 lines, pinned comment):**
- `claude code agent view`
- `claude code /goal`
- `claude code parallel agents`

**Secondary keywords (description + tags):**
- `claude code v2.1.139`
- `claude code research preview`
- `multiple claude code sessions`
- `tmux vs claude agents`

**Pinned comment template:**
> Timestamps:
> 0:00 — The result
> 0:08 — What `agent view` and `/goal` are
> 0:38 — The 24h test setup
> 1:30 — Hour-1 check-in
> 2:15 — The agent that stalled
> 4:45 — What actually shipped
> 6:00 — The setup mistake that cost me 2 hours
> 7:15 — Operator verdict — does this replace tmux?
>
> Setup I used: Claude Code v2.1.139, Max plan, MacBook. Activate with `claude agents` in any v2.1.139+ terminal. Docs: https://code.claude.com/docs/en/agent-view
>
> Which `/goal` should I test next? Drop it below — I'll pick the top-voted one for the next video.

(The "next video" question is the Communities-tab-tactic insurance + a comment magnet for early retention.)

---

## 🔗 Sources to cite in description

- [Anthropic blog — agent view announcement](https://claude.com/blog/agent-view-in-claude-code)
- [Claude Code docs — agent view](https://code.claude.com/docs/en/agent-view)
- [Claude Code v2.1.139 release notes](https://claude-world.com/articles/claude-code-21139-release/)
- [Anthropic official intro video](https://www.youtube.com/watch?v=-INveHwbRz4)

---

## Ready to start writing the full script

This intro draft is structured so the full script can be written top-down: each beat already has the script-voice line + the b-roll direction. The next step is to expand beats 4–9 into full voiceover paragraphs as the 24h test produces real footage. **Don't pre-write the verdict — let the test tell you what to say.**
