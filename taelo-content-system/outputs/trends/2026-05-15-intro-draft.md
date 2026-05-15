# Intro Draft — Anthropic Programmatic Credit Pool Reaction (2026-05-15)

**Working titles (pick one, A/B the thumbnail):**
1. *"Anthropic Just Put Your Claude Code Agents on a Meter (June 15)"*
2. *"$20. That's All You Get From Anthropic Starting June 15."*
3. *"What Every Claude Code Operator Should Do Before June 15"*
4. *"Anthropic's Third Subscription Change in 6 Weeks — Here's the Math"*

**Target length:** 7–9 min · **Format:** straight reaction + operator math + 3 moves to make · **Lead time:** record tomorrow morning, edit afternoon, publish 2026-05-17

**Why this pick** (carried from trend report):
- Net-new search terms ("programmatic credit pool", "Claude Agent SDK billing", "Claude $20 credit") with a hard June 15 deadline = 30–60 day SEO window minimum
- Zero competing reactions from the AI-builder YouTube roster as of write-time — first-mover lane is wide open
- Affects every Claude Code power user / OpenClaw user / Agent-SDK indie hacker — Taelo's exact audience
- **Pure reaction format — no 24h test, no production rig, no codebase dependency.** Genuinely 1-day prep, 1-day record, 1-day edit.

**Voice rules (active for this script):**
- Polish to clean native cadence (face-cam reaction beats can stay rough where energy beats grammar)
- ❌ Do NOT name specific journalists / outlets in the body — read out the *facts*, not "Decoder said…"
- ✅ Beat 9 outro shoutout: thank Anthropic team genuinely (the docs page is good), tip hat to indie hackers calling out the gap
- Address the audience, not a hypothetical editor
- Hold a clear opinion. "Inevitable, but they should've given 90 days not 30" is a takeable position. Don't fence-sit.

**2026 algorithm rule active here:** First 30 seconds is now a hard ranking checkpoint. Cold-open delivers **the news + the stakes**, not the setup. Numbers in the first 8 seconds.

---

## 🎬 COLD OPEN — 0:00 to 0:08 — the news, the number, the deadline

> **On June 15th — exactly thirty days from today — Anthropic puts every Claude Code agent on a meter.**
> **Pro plan: twenty dollars a month.**
> **Max 5x: one hundred.**
> **After that, you pay full API rates. Here's what changed, who gets hit, and the three things I'd do this week if I were you.**

*[B-roll: full-screen text card flashing each number in turn (`$20`, `$100`, `$200`) → cut to terminal prompt typing `claude -p "..."` with a red overlay flashing "metered"]*

**Why this opens correctly:** Three concrete numbers, a hard date, a viewer-direct stakes line. The viewer knows in 8 seconds whether they need to keep watching. Per 2026 algorithm: news + numbers + deadline → high retention through 0:30.

---

## 🪝 HOOK — 0:08 to 0:28 — what actually changed (in plain English)

> Two days ago Anthropic shipped one of the biggest pricing changes they've ever made to Claude Code. They didn't make a big announcement. They put it in the help center. So here's what it actually says.
>
> Right now, if you've got a Pro plan, you can run Claude Code in the terminal — interactive — and you can also run it programmatically. `claude -p`, the Agent SDK, GitHub Actions, third-party tools like OpenClaw. All of it pulls from the same subscription bucket.
>
> Starting June 15th, that bucket splits in two. Interactive usage stays on the subscription, unchanged. **Programmatic usage** — every Agent SDK call, every `claude -p` script, every GitHub Action, every third-party agent — gets its own monthly credit pool. Pro gets twenty dollars. Max 5x gets a hundred. Max 20x gets two hundred. **And it doesn't roll over.**

*[B-roll: split screen of two pipelines — left labeled "INTERACTIVE", right labeled "PROGRAMMATIC", a meter ticks down on the right side only → freeze on the Anthropic Help Center page, highlight the credit-tier table]*

---

## 🎯 PROMISE — 0:28 to 0:42 — the contract with the viewer

> In the next seven minutes I'm going to do four things. **One** — show you exactly which workflows are affected and which ones aren't, because the press coverage is muddy on this. **Two** — run the actual math on what twenty dollars buys you in real Agent SDK tokens, so you know if you're about to hit the wall. **Three** — give you the three specific moves I would make in the next thirty days if I were running production agents on a Claude subscription. **Four** — my honest take on whether this is fair, predatory, or just inevitable.

*[B-roll: four-card animation, each card prints its label as the line is delivered]*

---

## 📋 Beat structure for the rest of the video

| Beat | Time | What it covers | B-roll |
|---|---|---|---|
| 4. What's covered vs not covered | 0:42–1:45 | The clean line. Covered: Agent SDK, `claude -p`, Claude Code GitHub Actions, third-party Agent-SDK apps (OpenClaw etc.). Not covered: interactive Claude Code, Claude Cowork, Claude.ai chat. | Two-column table animation. Green check marks vs red coin icons |
| 5. The math on $20 | 1:45–3:00 | Real numbers. Use last month's `claude -p` token spend on your own machine as the worked example. Convert "$20 credit" to tokens at standard API rates. How many hours of background work does that actually buy? | Calculator overlay, real token counts pulled from your terminal history; ratio chart |
| 6. Who gets hit hardest | 3:00–4:00 | Three personas: (a) the indie hacker chaining `claude -p` in scripts, (b) the team using GitHub Actions for PR review, (c) the OpenClaw user squeezing $200 of API value out of a Pro sub. Be specific. | Three personas drawn as terminal cards |
| 7. The three moves to make this week | 4:00–5:30 | **Move 1:** measure your actual current programmatic token spend over the next 7 days (don't guess). **Move 2:** decide per-workflow whether it stays on the credit (low-volume, interactive-adjacent) or moves to an API key with a budget alert (production, high-volume). **Move 3:** if you're using third-party Agent-SDK tools, ask the vendor today which model they're moving to — some will eat the cost, some will pass it through. | Each move animates in as a checklist; show the actual budget-alert UI in the Anthropic console |
| 8. The third change in six weeks | 5:30–6:30 | Honest reframe. April 4 third-party ban → April 21 brief Pro/Code removal → May 14 credit split. Pattern: Anthropic built subscription pricing when Claude Code was a lighter workload. Now they're rebuilding the meter to match the new agentic workload. | Timeline graphic, dates land as ticks |
| 9. Verdict + outro | 6:30–8:00 | The honest take. "Inevitable, but the 30-day deadline is too tight — should have been 90 days with a soft-launch credit doubling for early users." Then: who this is *good* for (heavy interactive users), who it punishes (production agentic). End with the one-line summary: "the era of $20 squeezing $200 of API value is over — that was always going to end. Now budget like a grown-up." Beat 9 shoutout. | Final timeline frame, close on the June 15 marker |

---

## 🎨 Claude Design intro brief (paste this into Claude Design)

> **Brief:** Build an intro graphic + animated lower-third for a YouTube video titled *"Anthropic Just Put Your Claude Code Agents on a Meter (June 15)"*. Solo creator (Taelo Kim) reacting to Anthropic's Programmatic Credit Pool announcement.
>
> **Visual identity:**
> - Palette: Anthropic terminal aesthetic — deep slate (#0E1116) background, Anthropic coral/orange accent (#D97757) for the "alert / changed" state, soft cream (#F5F1EB) for body text, deep red (#E04848) ONLY for "metered" and the June 15 deadline marker
> - Foreground: a stylized **digital meter / odometer** counting tokens down — three digital readouts stacked: top reads `$20.00`, middle `$100.00`, bottom `$200.00` — each labeled `PRO`, `MAX 5x`, `MAX 20x` in monospace
> - To the right of the meters: a vertical "JUNE 15" deadline stripe (deep red, thin, full-height) with a tick countdown `30 DAYS`
> - Below the meters: a single line that types out — `claude -p "build a feature" --metered`
> - Above the whole composition: subtle "PROGRAMMATIC CREDIT POOL" chyron in muted gray
>
> **Animations needed:**
> 1. **0–2s open card:** dark slate fades up → three meters spin from blank to `$20.00 / $100.00 / $200.00` (digital flip animation)
> 2. **2–4s reveal:** "JUNE 15" deadline stripe slides in from the right → countdown `30 DAYS` ticks down to `29 DAYS` and holds
> 3. **4–5s callout:** the `claude -p` line types out, the `--metered` flag flashes red
> 4. **Lower-third (reusable):** thin slate bar with coral underline, monospace text "Taelo Kim · The June 15 Change"
>
> **Style notes:**
> - Cinematic terminal-meets-odometer aesthetic. NOT corporate finance dashboard.
> - Monospace font (JetBrains Mono or Fira Code)
> - The **three-meter stack** is the memorable visual — exaggerate the digital-flip motion
> - Don't add Anthropic logos (positioning as independent operator, not affiliate)
> - The red June 15 stripe is the **urgency element** — it should feel like a deadline clock, not a sale banner
>
> **Output formats requested:**
> - 16:9 intro card (3840×2160 PNG static "title frame" — the moment all three meters are visible with the June 15 stripe)
> - Animated MP4 (5 sec, 4K, 60fps, transparent BG) for opening
> - Reusable lower-third PNG sequence (1080p, transparent)
> - Two 1280×720 thumbnail variants:
>    - **A:** giant `$20` red-stamped center, June 15 stripe right, face-cam expression bottom-left
>    - **B:** three-meter stack center, "ON A METER" diagonal stamp across, no face-cam (test the no-face-cam thumbnail)

---

## 📋 Shot list (recording day — tomorrow morning, 2026-05-16)

1. **Cold-open piece-to-camera** (1 take, 8 sec) — deliver the three-number opening cold. Re-do until energy is right. **Don't soften.** This is news + numbers + deadline.
2. **Hook walkthrough** — screen-record of the actual Anthropic Help Center page; cursor highlights the credit-tier table. Voiceover overlay.
3. **Promise card** — face-cam, 14 sec, deliver the four-point contract with measured pacing.
4. **Beat 4 (covered vs not)** — screen-record only, no face-cam. Build the table on screen as you talk through it.
5. **Beat 5 (the math)** — voiceover over a real screen capture of your own past `claude -p` token usage (export from the Anthropic console). Show the actual numbers.
6. **Beat 6 (three personas)** — face-cam for the persona intros, b-roll on each persona's terminal as you describe their workflow.
7. **Beat 7 (three moves)** — face-cam for the intros, screen-record of the actual setup (Anthropic console budget alert UI; one example vendor email).
8. **Beat 8 (the timeline)** — voiceover only, screen builds the timeline.
9. **Beat 9 verdict + outro** — face-cam, slow, deliberate. The honest take has to land. Don't rush. End with the like/sub + tease next video (Claude for Small Business reaction queued for May 20).

**Energy notes:**
- Beats 1–3: tight, fast, news-anchor confident
- Beats 4–6: explainer-mode, slower, teacher pacing
- Beats 7: prescriptive, operator-confident
- Beats 8–9: reflective, opinionated, no fence-sitting

---

## 📌 SEO checklist

**Primary keywords (must appear in title, description, first 3 lines, pinned comment):**
- `anthropic programmatic credit pool`
- `claude agent sdk billing`
- `claude code subscription change`
- `claude $20 credit`

**Secondary keywords (description + tags):**
- `claude code june 15`
- `claude agent sdk credit pool`
- `anthropic agents billing`
- `claude -p billing`
- `openclaw billing`
- `claude code github actions billing`

**Description first 150 words (front-load):**
> On June 15, 2026, Anthropic splits Claude Code billing in two. Programmatic usage — Claude Agent SDK, `claude -p`, Claude Code GitHub Actions, and third-party tools like OpenClaw — moves into a separate monthly credit pool. Pro gets $20, Max 5x gets $100, Max 20x gets $200, with no rollover. After that, you pay standard API rates. Interactive Claude Code, Claude Cowork, and Claude.ai chat are unchanged. This video runs the math on what $20 actually buys in real Agent SDK tokens, names the three personas hit hardest, and gives you the three specific moves to make in the next 30 days before the deadline lands. Includes a frank operator's verdict on whether the change is fair, predatory, or just inevitable — and what every Claude Code power user should budget for from June 15 forward.

**Pinned comment template:**
> Timestamps:
> 0:00 — The news in 8 seconds
> 0:08 — What actually changed (plain English)
> 0:42 — Covered vs not covered
> 1:45 — What $20 actually buys you (real math)
> 3:00 — The 3 personas hit hardest
> 4:00 — The 3 moves to make this week
> 5:30 — The third subscription change in 6 weeks
> 6:30 — My honest take
>
> Official source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
>
> What's your June 15 plan — stay on subscription, or move to an API key with budget alerts? Drop it below.

(The "what's your plan" question doubles as Communities-tab fuel and an early-retention comment magnet.)

---

## 🔗 Sources to cite in description

- [Anthropic Help Center — Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- [The New Stack — Anthropic splits billing again](https://thenewstack.io/anthropic-agent-sdk-credits/)
- [The Register — Anthropic tosses agents into the API billing pool](https://www.theregister.com/ai-ml/2026/05/14/anthropic-tosses-agents-into-the-api-billing-pool/5240748)
- [VentureBeat — OpenClaw reinstated with a catch](https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch)
- [InfoWorld — agents on a meter](https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html)
- [XDA Developers — what subscriptions lose](https://www.xda-developers.com/anthropics-claude-subscriptions-no-longer-include-agent-sdk-and-claude-p-usage/)
- [DevToolPicks — Indie Hacker breakdown](https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026)

---

## 🪒 Shorts to cut from this long-form (4 vertical Shorts, native 9:16)

1. **"The Cold Open" Short (0:00–0:35)** — the three numbers, the June 15 deadline, cut hard. 35 sec.
2. **"$20 vs $200" Short (Beat 5 highlight)** — the math reveal, fast cut. 45 sec.
3. **"3 Moves Before June 15" Short (Beat 7 highlight)** — checklist format, native vertical, captions burned in. 55 sec.
4. **"Anthropic's 3rd Change in 6 Weeks" Short (Beat 8)** — the timeline, ticks land like a drum. 40 sec.

Cross-post #1 and #3 to TikTok with keyword-loaded captions for the TikTok-Search surface.

---

## 📝 LinkedIn Newsletter companion (write same day as edit)

**Title:** *Operator's Brief #001 — The June 15 Anthropic Change That Every Claude Code Power User Should Plan For*
**Length:** 700–800 words
**Structure:** Same four beats as Promise (what changed / the math / who gets hit / what to do). Drop the verdict at the bottom. Link the YouTube video. Audience = indie hackers, founders, ops people. LinkedIn newsletter delivers to inbox = bypasses feed algorithm.

---

## Ready to start writing the full script

Every beat above already has the script-voice line + b-roll direction + energy note. Expand beats 4–9 into full voiceover paragraphs after recording the cold open + hook + promise (so the early-energy locks the rest of the script's rhythm). **The verdict in Beat 9 should be the *last* thing you write — let the math beats inform the strength of the take.**
