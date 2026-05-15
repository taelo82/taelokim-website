# Full Script — Anthropic's June 15 Credit Pool: The Operator Playbook (2026-05-15)

**Format:** Full ready-to-film script. Every line in **bold quotes** is exactly what you say to camera. Brackets are b-roll / screen direction.
**Target length:** 8:30–9:30 · **Voice:** direct, raw, no fluff, real numbers, no hype
**Lead:** Matt Pocock proved the math. Theo gave the verdict. You ship the **operator playbook** neither did.

## Working titles (pick one, A/B the thumbnail)

1. *"Anthropic's June 15 Change: Who Actually Gets Hit (And the 30-Day Playbook)"*
2. *"Matt Pocock Proved the Cut. Theo Called It Quits. Here's What to Actually Do."*
3. *"5 Claude Code Personas. 1 Deadline. Here's Your Move."*
4. *"Anthropic Just Cut Your Claude Code Usage 10x — Read This Before June 15"*

**My pick:** #1 — durable SEO, says exactly what's inside.

## Voice rules

- Polish to clean native cadence — face-cam can stay rough where energy beats grammar
- ❌ No "in today's video", "smash that like", "game-changer", "without further ado", "you NEED to see this NOW"
- ✅ "Here's what actually happened", "The real numbers", "Let me show you", "No BS", "I ran the math"
- Numbers first, hype never
- You did NOT invent the math (Matt did) — credit him in Beat 4 outro, don't bury it
- Hold a clear take in Beat 9. "Inevitable, but the 30-day deadline is punitive." Don't fence-sit.

## 2026 algorithm rule active

First 30 seconds is a hard ranking checkpoint. Cold open delivers **news + number + stakes** in 8 seconds. No setup. No "hey what's up guys."

---

# 🎬 FULL SCRIPT (every line you say, in order)

---

## 0:00–0:08 — COLD OPEN (face cam, direct, no smile)

**"On June 15th, Anthropic puts every Claude Code agent on a meter."**
**"Pro plan: twenty dollars a month."**
**"Max plan: a hundred."**
**"After that, you're paying full API rates. I ran the math on five real operators — three of them are about to lose ten times their Claude Code usage. Here's who, by how much, and the three things you do this week."**

*[B-roll: full-screen text card flashes each number — `$20` → `$100` → `$200` → calendar showing June 15 with red ring → cut to your face for "five real operators"]*

**Retention check:** 8 seconds. Three concrete numbers. A specific date. A specific pain. A specific promise. No filler.

---

## 0:08–0:35 — HOOK (face cam → screen share of Anthropic Help Center)

**"Two days ago Anthropic shipped one of the biggest pricing changes they've ever made to Claude Code. They didn't tweet a big announcement. They quietly updated a help page. Matt Pocock did the math — it's a five-to-twenty-times cut for anyone running agents in the background. Theo at t3.gg posted a forty-five minute video literally called 'I'm done.'"**

**"And here's the thing. Both of them are right. But neither of them answered the question my DMs blew up with this week: am I one of the people getting hit, and what do I actually do about it?"**

*[B-roll: split screen — Matt's video thumbnail left, Theo's "I'm done." right, both ticking through with view counts. Then cut to the Anthropic Help Center page — highlight the credit-tier table with a yellow underline]*

**Retention check:** by 0:35 viewer knows (1) the change is real, (2) it's worse than the headline, (3) you have something the bigger videos didn't.

---

## 0:35–0:55 — THE CONTRACT (face cam, slower)

**"Next eight minutes I'm doing four things. One — I show you exactly what changes and what doesn't, because half the coverage I've read this week gets it wrong. Two — the real math. What twenty bucks actually buys you in Claude tokens, and the hidden number that turns this from a small cut into a ten-x cut. Three — five real operator personas. I'll tell you which one you are and what your number looks like. Four — the three moves I'm making before June 15th."**

**"No fluff. Let's go."**

*[B-roll: four cards stack on screen as you list — "What changes" / "The math" / "Who gets hit" / "Three moves" — each card numbered]*

---

## 0:55–2:00 — BEAT 1: WHAT'S COVERED VS WHAT'S NOT

**"First the clean line, because everyone's confusing this."**

**"On June 15th, your Claude subscription splits into two buckets. Bucket one — interactive. That means anything you type into Claude.ai, anything you do inside Claude Cowork, and any time you sit in your terminal with Claude Code open and a real human conversation happening. That bucket is untouched. Same as today."**

**"Bucket two — programmatic. That means four things specifically. The Claude Agent SDK. The `claude -p` flag — print mode, the headless one you use in scripts. Claude Code GitHub Actions, the one that auto-reviews your PRs. And any third-party tool built on the Agent SDK — OpenClaw, automation pipelines, anything chaining Claude in the background."**

**"That second bucket gets its own monthly credit. Pro: twenty dollars. Max 5x: a hundred. Max 20x: two hundred. The credit does not roll over. When you run out, you stop — unless you've toggled 'extra usage,' which charges you full API rates."**

*[B-roll: two-column table builds on screen.
LEFT column "✅ UNTOUCHED": Claude.ai chat / Claude Cowork / Interactive Claude Code in terminal.
RIGHT column "💸 METERED FROM JUNE 15": Claude Agent SDK / `claude -p` / Claude Code GitHub Actions / Third-party Agent-SDK apps (OpenClaw etc.).
Each line appears as you say it.]*

**Pace note:** this is the explainer beat. Slower. Teacher voice. No sarcasm yet.

---

## 2:00–3:30 — BEAT 2: THE REAL MATH (and the hidden metric)

**"Okay. The math. Here's where it gets ugly."**

**"Twenty dollars sounds fine until you actually translate it into tokens. At standard API rates, twenty dollars of mixed agentic work — roughly 70% input, 30% output — buys you about one-point-three million tokens of Sonnet usage."**

**"That sounds like a lot. It is not. A real Claude Code session — one task, one feature, one agent running for an hour — burns between a hundred thousand and five hundred thousand tokens. So your twenty dollar credit buys you somewhere between three and fourteen full sessions a month. Per month."**

*[B-roll: calculator graphic on screen.
Line 1: "$20 ÷ avg $0.014/1K tokens ≈ 1.43M tokens"
Line 2: "1 Claude Code session ≈ 100K–500K tokens"
Line 3 (lands with a thud): **"≈ 3 to 14 sessions / month"**]*

**"Now here's the hidden metric nobody is talking about."**

**"Right now, with a twenty dollar Pro plan and a tool like OpenClaw, indie hackers have been squeezing about two hundred dollars worth of effective API usage out of that twenty dollar sub. Some people more. That's the arbitrage that's about to die. So when Matt Pocock says 'five to twenty x cut,' that twenty x at the upper end? That's not a worst-case exaggeration. That's the OpenClaw operator. That's a real person. Probably someone watching this right now."**

*[B-roll: a "before / after" bar chart.
Before: $200 of effective monthly Claude value on a $20 Pro plan (tall green bar, "OpenClaw arbitrage").
After: $20 of metered value on the same plan (short red bar).
The cut is visualized as a 90% slash across the bar.]*

**"And the second hidden thing — the 'extra usage' toggle that lets you keep going past your credit? It is off by default. Which means a lot of people are about to hit the wall mid-job and not realize it until their agent silently dies on a Tuesday at 2am."**

*[B-roll: screen-record of your own Anthropic console with the "Extra Usage" toggle highlighted, currently OFF, with a red arrow]*

**Pace note:** Beat 2 is the spike beat. Slow down on the OpenClaw number. Let "ten x cut" hit.

---

## 3:30–5:30 — BEAT 3: THE 5 OPERATOR PERSONAS

**"Right. Now the part Matt and Theo didn't do. Which one of these are you."**

**[Face cam, then cut to a 5-card layout that builds as you go]**

**"Persona one. The OpenClaw operator. You're on a twenty dollar Pro plan, you've got OpenClaw or a similar tool wrapped around Claude Code, and you've been quietly running production agents on what should be a personal plan. Your old effective ceiling: about two hundred bucks a month of API value. Your new hard ceiling on June 15th: twenty dollars. **That's the ten-x cut.** You are the persona hit hardest. By a wide margin."**

*[B-roll: persona card "OpenClaw Operator" — old: $200 effective, new: $20 hard cap, label "10x cut", red]*

**"Persona two. The `claude -p` scripter. You have cron jobs. You have content pipelines. You have a couple of bash scripts that pipe `claude -p` to do things while you sleep. Your usage is moderate but constant. You're looking at a five to ten x cut depending on volume. The fix is mostly painless — but only if you measure it before June 15th."**

*[B-roll: persona card "claude -p scripter" — terminal with cron icon, label "5-10x cut", orange]*

**"Persona three. The GitHub Actions PR reviewer. You set up Claude Code Actions to review every PR in your repo. Real number — a Claude PR review averages somewhere between one and three dollars of token spend depending on diff size. Your twenty dollar credit covers seven to twenty PRs a month. If you ship more than that and you're on Pro, your PR bot stops reviewing on the eighteenth of the month. Quietly."**

*[B-roll: persona card "GitHub Actions PR reviewer" — GitHub Actions logo, label "7-20 PRs / month", yellow]*

**"Persona four. The agentic SaaS founder. You built a small app on the Agent SDK. Your users are hitting your Claude account, not theirs. You now have one of three choices. Eat the cost — keep eating margin. Pass through — make your users plug in their own API key. Or — and this is the move I think most people will land on — gate the agent behind a separate paid tier."**

*[B-roll: persona card "Agentic SaaS founder" — 3-option fork: Eat / Pass / Gate, label "Architecture decision required by Jun 15", purple]*

**"Persona five. And this one is mine. The international operator. If you're like me, running Claude Code-powered client work out of Korea, Singapore, anywhere outside the US, your hourly margin lives in the gap between subscription cost and the value you deliver. June 15th compresses that gap. If you're billing clients for agentic workflows on a Pro plan, you are not on a Pro plan anymore. Move to API key with budget alerts before someone else's bill becomes your problem."**

*[B-roll: persona card "International / client-work operator" — Korea/SEA map highlight, label "Margin compression", blue]*

**Pace note:** this is the cluster beat. Each persona is ~25 seconds. Drop the voice on the number. Use the persona cards as visual anchors for thumbnail screenshots later.

---

## 5:30–7:00 — BEAT 4: THE THREE MOVES BEFORE JUNE 15

**"Three moves. In order. Don't skip ahead."**

**"Move one. Measure. Don't react yet. From today until June 1st you do one thing — you log your actual programmatic token spend. Open the Anthropic console, go to Usage, filter by API key, separate interactive from programmatic. If you've got `claude -p` in scripts, check your shell history. If you're on a third-party tool like OpenClaw, check that dashboard. **You cannot make a decision without your number.** Most people will guess. Be the operator who doesn't."**

*[B-roll: screen record of your own Anthropic console → Usage → filter dropdown highlighted → numbers visible. Annotated callout: "Your real programmatic spend (last 30 days)".]*

**"Move two. Sort each workflow into one of three buckets. Bucket A — keep on credit. Anything you actually use in interactive mode, plus light-use programmatic stuff that fits under twenty bucks. Bucket B — move to API key. Production workflows, anything chained, anything that runs while you sleep, anything that bills a client. Get the API key today, set a budget alert, route the workflow over. Bucket C — kill it. There is always at least one Claude script you wrote three months ago that nobody is using. Find it. Stop paying for it."**

*[B-roll: three buckets animation —
Bucket A "Keep on credit" → green check, light-use stuff.
Bucket B "API key + budget alert" → orange wrench, production stuff.
Bucket C "Kill" → red trash, dead stuff.
Each fills as you list it.]*

**"Move three. If you use any third-party tool built on the Agent SDK — OpenClaw, automation tools, agentic plugins, anything — send the vendor one email today. Ask one question. **'What is your pricing model post-June 15th — are you eating the cost, passing it through, or moving to a metered tier?'** Some will eat it. Some will pass through. The ones that don't reply within seven days — that's your signal. Migrate off."**

*[B-roll: a sample one-line email template on screen, ready to copy.
"Hi [vendor] — quick one. With Anthropic's June 15 programmatic credit change, what is your pricing model going forward? Are you eating the cost, passing it through, or moving to a metered tier? Thanks."]*

**Pace note:** Beat 4 is the deliverable. Slow, prescriptive, no hedging. This is the beat that gets the video shared.

---

## 7:00–8:00 — BEAT 5: THE PATTERN — THIRD CHANGE IN SIX WEEKS

**"Last thing. I want to zoom out for one minute, because this is not a one-off."**

**"Six weeks ago — April 4th — Anthropic banned third-party agents from subscriptions. Two weeks later, April 21st, they briefly removed Claude Code from the Pro plan entirely. They walked it back in 48 hours after the developer outrage. And now, May 14th, the credit split. **Three subscription changes in six weeks.**"**

**"This isn't malice. It's a company that priced subscriptions when Claude Code was a typing assistant, and now that it's running autonomous agents on someone's laptop while they sleep, the unit economics broke. They're rebuilding the meter to match the new workload. That part is inevitable. Every API-priced AI company is going to do this. OpenAI already did it with Workspace Agents — the free preview ended May 6th."**

*[B-roll: timeline graphic builds left-to-right.
Tick 1: "Apr 4 — third-party ban"
Tick 2: "Apr 21 — Pro/Code removal (reversed)"
Tick 3 (lands red): **"May 14 — credit split (live June 15)"**
At the end, an arrow extends past May 14 with "??? next" in gray.]*

---

## 8:00–8:50 — BEAT 6: THE HONEST TAKE

**[Face cam. No b-roll. Just you.]**

**"My honest take. Two parts."**

**"One — the change itself is fair. The era of squeezing two hundred bucks of API value out of a twenty dollar plan was always going to end. That was arbitrage, not pricing. Anyone running production agents on a personal plan was borrowing trouble. Anthropic's not wrong to fix it."**

**"Two — the rollout is punitive. Thirty days is not enough. No rollover on unused credit is a punitive design choice — it tells me they want you to overspend, not budget honestly. They should have given ninety days, doubled the credit for early users for the first three months, and let it roll over for the first quarter. Instead it's twenty bucks, hard wall, the eighteenth of June at 2am, agent dead."**

**"So — inevitable but punitive. Budget like a grown-up starting today. And don't get caught with a script running in the dark on June 16th."**

*[B-roll: a single static slate at the end — the June 15 date, big and red, no animation. Hold for 2 seconds.]*

**Pace note:** Beat 6 is the verdict. Slower than anywhere else in the video. Don't rush. The take has to land.

---

## 8:50–9:30 — OUTRO + BEAT 9 SHOUTOUT + CTA

**"That's the playbook. If this helped, the like and the sub help me ship the next one faster — I've got the new Claude for Small Business plugin queued up for next week, and that one's going to surprise you in a different direction."**

**"Real shoutouts this round. Matt Pocock — go watch his ten-minute breakdown, that's where the five-to-twenty-x math is properly derived. Theo at t3.gg — the long-form verdict for anyone who wants the cathartic version. And Anthropic — credit where it's due, the help center docs on this are actually clear, which is more than I can say for most pricing announcements."**

**"Drop me one thing in the comments — which persona are you? OpenClaw operator? Scripter? Founder? I read them. The top-voted persona becomes the deep-dive video next month."**

**"See you in the next one."**

*[B-roll: end card — your face left, three "Watch next" tiles right: Matt's video, Theo's video, your previous video. Subscribe button bottom-center, no animation.]*

---

# 📌 SEO checklist

**Primary keywords (must appear in title, description, first 3 lines, pinned comment):**
- `anthropic programmatic credit pool`
- `claude agent sdk billing`
- `claude code june 15`
- `claude $20 credit`

**Secondary keywords (description + tags):**
- `claude agent sdk credit pool`
- `anthropic agents billing`
- `claude -p billing`
- `openclaw billing change`
- `claude code github actions billing`
- `matt pocock anthropic`
- `theo t3.gg claude`

**Description first 150 words (front-load — this is what YouTube reads):**

> On June 15, 2026, Anthropic splits Claude Code billing in two. Programmatic usage — Claude Agent SDK, `claude -p`, Claude Code GitHub Actions, and third-party tools like OpenClaw — moves into a separate monthly credit pool. Pro gets $20. Max 5x gets $100. Max 20x gets $200. No rollover. After that, you pay standard API rates. Interactive Claude Code, Claude Cowork, and Claude.ai chat are unchanged. Matt Pocock did the math: it's a 5–20x cut for AFK Claude usage. Theo at t3.gg gave the verdict. This video is the operator playbook neither of them shipped — 5 real personas with real numbers, the hidden metrics nobody is talking about (including the "Extra Usage" toggle that's off by default), and the 3 specific moves to make before the deadline.

**Pinned comment template:**

> Timestamps:
> 0:00 — The news in 8 seconds
> 0:35 — What Matt and Theo missed
> 0:55 — Covered vs not covered
> 2:00 — The real math + the hidden metric
> 3:30 — 5 operator personas
> 5:30 — 3 moves before June 15
> 7:00 — The pattern: 3 changes in 6 weeks
> 8:00 — My honest take
>
> Official source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
> Matt Pocock's math breakdown: https://www.youtube.com/watch?v=lNOQaakmyDU
> Theo's full verdict: https://www.youtube.com/watch?v=131yAOjxHHQ
>
> Which persona are you? Drop it below — top-voted persona becomes the deep-dive video next month.

---

# 🎨 Claude Design intro brief (paste into Claude Design)

> **Brief:** Build an intro graphic + animated lower-third for a YouTube video titled *"Anthropic's June 15 Change: Who Actually Gets Hit (And the 30-Day Playbook)"*. Solo creator Taelo Kim — operator's POV breakdown of Anthropic's Programmatic Credit Pool announcement.
>
> **Visual identity:**
> - Palette: terminal aesthetic — deep slate (#0E1116) bg, Anthropic coral (#D97757) accent, soft cream (#F5F1EB) body, deep red (#E04848) ONLY for "metered" + June 15 deadline
> - Foreground: 3 stacked digital odometers reading `$20.00 / $100.00 / $200.00`, labeled `PRO / MAX 5x / MAX 20x` in monospace
> - Right side: vertical "JUNE 15" deadline stripe, deep red, with `30 DAYS` countdown
> - Below odometers: typewriter line `claude -p "build a feature" --metered`
> - Above: muted gray chyron "PROGRAMMATIC CREDIT POOL"
>
> **Animations:**
> 1. 0–2s: bg fades up → 3 odometers spin from blank to their values (digital flip)
> 2. 2–4s: JUNE 15 stripe slides in → countdown ticks `30 → 29 DAYS` and holds
> 3. 4–5s: `claude -p` line types → `--metered` flag flashes red
> 4. Lower-third (reusable): slate bar + coral underline, monospace "Taelo Kim · The June 15 Playbook"
>
> **Style:** cinematic terminal-meets-odometer. NOT corporate finance dashboard. JetBrains Mono / Fira Code. Saturate the red. No Anthropic logos.
>
> **Output formats:**
> - 16:9 intro card (3840×2160 PNG)
> - Animated MP4 (5 sec, 4K, 60fps, transparent BG)
> - Reusable lower-third PNG sequence (1080p, transparent)
> - Two 1280×720 thumbnails:
>   - **A:** giant `$20` red-stamped center, JUNE 15 stripe right, face-cam expression bottom-left
>   - **B:** 3-meter stack center, diagonal "10x CUT" stamp across, no face-cam

---

# 📋 Shot list (recording day — tomorrow morning, 2026-05-16)

| # | Shot | Setup | Take notes |
|---|---|---|---|
| 1 | **Cold open** (0:00–0:08) | Face cam, direct, no smile, news-anchor energy | Land all 3 numbers. Re-do until the "ten times their Claude Code usage" lands without rushing. |
| 2 | **Hook** (0:08–0:35) | Face cam + screen of Anthropic Help Center | One take face-cam → cut to screen recording. The "my DMs blew up" line needs energy. |
| 3 | **Contract** (0:35–0:55) | Face cam | Slower than the hook. Sets up the structure. |
| 4 | **Beat 1 — covered vs not** (0:55–2:00) | Screen share heavy. Build the two-column table live. | Voiceover. No face-cam needed. |
| 5 | **Beat 2 — math + hidden metric** (2:00–3:30) | Calculator overlay + bar chart + console screen-record | The OpenClaw $200 → $20 reveal needs a pause. Don't talk over the bar chart. |
| 6 | **Beat 3 — 5 personas** (3:30–5:30) | Face cam intros + persona card cuts | Each persona ~25s. Voice drop on the number. Cleanest if you record all 5 intros back-to-back. |
| 7 | **Beat 4 — 3 moves** (5:30–7:00) | Face cam intro + screen recordings of console / buckets / email template | Prescriptive tone. No hedging. The deliverable beat. |
| 8 | **Beat 5 — timeline pattern** (7:00–8:00) | Voiceover only over timeline graphic | Tick 3 lands red. Don't rush the "??? next" beat. |
| 9 | **Beat 6 — verdict** (8:00–8:50) | Face cam only. No b-roll. | Slowest beat in the video. The take has to land. Multiple takes. |
| 10 | **Outro + Beat 9 shoutouts + CTA** (8:50–9:30) | Face cam → end card | Genuine shoutouts to Matt + Theo + Anthropic. CTA is the persona question. |

**Energy map:** Beats 1–3 tight & fast → Beats 4–5 teacher pace → Beat 6 prescriptive-confident → Beat 7 narrator-zoom-out → Beat 8 slow-opinionated → Beat 9 sincere-warm.

---

# 🪒 Shorts cuts (4 vertical Shorts, native 9:16)

1. **"The 10x cut nobody warned you about" (Beat 2 highlight)** — the bar chart reveal + the OpenClaw $200 → $20 number. 45 sec.
2. **"Which Claude Code persona are you?" (Beat 3 highlight)** — quick-fire 5 personas, name-only. 55 sec.
3. **"3 moves before June 15" (Beat 4 highlight)** — checklist format, captions burned in. 55 sec.
4. **"Anthropic's third pricing change in 6 weeks" (Beat 5 highlight)** — timeline ticks, drum-hit cuts. 40 sec.

Cross-post #1 and #3 to TikTok with keyword-loaded captions: "anthropic agent sdk billing", "claude code june 15", "claude $20 credit explained".

---

# 📝 LinkedIn Newsletter companion (write same day as edit)

**Title:** *Operator's Brief #001 — The Anthropic June 15 Change and What 5 Real Operators Should Actually Do*
**Length:** 700–800 words
**Structure:** Mirror the video — what changed / the math / 5 personas / 3 moves / take. Drop the timeline section (LinkedIn audience doesn't need it). Link the YouTube video + Matt's video at the bottom. Send Sunday 2026-05-17 at 8am KST.

---

# 🔗 Sources (description + first-comment)

- [Anthropic Help Center — Agent SDK with your plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- [Matt Pocock — Anthropic's dedicated monthly credit is actually a huge cut](https://www.youtube.com/watch?v=lNOQaakmyDU)
- [Theo - t3.gg — "I'm done."](https://www.youtube.com/watch?v=131yAOjxHHQ)
- [Anthropic @ClaudeDevs original post](https://x.com/ClaudeDevs/status/2054610152817619388)
- [The New Stack — Anthropic splits billing again](https://thenewstack.io/anthropic-agent-sdk-credits/)
- [The Register — agents into the API billing pool](https://www.theregister.com/ai-ml/2026/05/14/anthropic-tosses-agents-into-the-api-billing-pool/5240748)
- [VentureBeat — OpenClaw reinstated with a catch](https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch)
- [InfoWorld — agents on a meter](https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html)
- [XDA Developers — what subscriptions lose](https://www.xda-developers.com/anthropics-claude-subscriptions-no-longer-include-agent-sdk-and-claude-p-usage/)
- [DevToolPicks — Indie Hacker breakdown](https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026)

---

# Ready to film

Every line you say is in **bold quotes**. Every b-roll cue is in brackets. Read it once aloud before you hit record to make sure the rhythm is yours. Adjust the persona-5 (international operator) section if you want to lean harder into Korea/SEA specifics — that's your unique angle in the field and Matt/Theo can't touch it.
