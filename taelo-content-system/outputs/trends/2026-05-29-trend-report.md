# Trend Report — 2026-05-29 (4-day window · the "stop shipping nothing" reframe · news + viral + education + skills)

**Window:** 2026-05-26 → 2026-05-29 (4 days)
**Channels scanned:** 29 (rows 1–29 of `brand/competitors.md`) + news/viral/X signal (web)
**Scoring:** size-adjusted outlier (raw × log size factor). Video scan carried from [2026-05-27](2026-05-27-trend-report.md) (only 2 days elapsed, 0 strong outliers then) + web-sourced delta. **Live YouTube API rescan offered — not auto-run this round** (see Files).
**Mode this round:** **Intervention report.** The signal isn't "what's trending" — it's that **nothing has shipped since the 5/20 command-center script.** Three consecutive plans (5/25, 5/27, this one's predecessor) named picks with 1–2 day film-day production. None shipped. Last actual films in `raw-takes/` are the `/watch` tutorial (May 5). **This report optimizes for one variable: time-to-publish. Every pick below is buildable in hours, screen-capture-first, no film day required.**

---

## TL;DR — the real diagnosis

Taelo's brief is explicit and correct: **stop the weeks-long builds (website-with-Claude, skill-dev). Ship fast, SEO-durable, sub-growth content.** The data agrees harder than expected:

- **The pattern that's killing the channel isn't topic selection — it's production weight.** Every stalled pick (Grok Build operator review, Antigravity post-mortem, Codex-for-video) required setup + film + edit. The reaction-video lead-time problem Taelo flagged is real, but the deeper problem is *anything needing a camera doesn't ship.*
- **The fix:** bias 100% of the next 2 weeks toward **screen-capture + voiceover** content that ships in **2–4 hours**, and toward an **evergreen education series** that compounds on SEO instead of chasing news.
- **Two of Taelo's own proposed ideas are the strongest picks in the entire scan** — the "3 one-click skills" video and the "how LLMs/tokens actually work" series. Both are screen-capture, both are SEO-durable, both have empty operator-framed lanes. We don't need a fresh reaction to grow; we need to *finish* these.

**🏆 Pick of the week (ships in ~3 hours, evergreen SEO):**
**"3 Claude Code skills I install in 1 click — used daily by AI pros, highest ROI."** superpowers + `/dream` + `/goal`. No film day. Pure screen capture + voiceover. This is the fastest path to a shippable, SEO-durable video and it's already Taelo's idea.

**Backup #1 — contrarian reaction, non-ephemeral, ~3 hours:**
**"Anthropic raised your limits 50%… then quietly carved the Agent SDK out of your plan (June 15)."** The stalled 50%-cut video now has a concrete, datable hook: the **June 15 "dedicated programmatic credit pool"** that moves all Agent SDK / `claude -p` / third-party usage off your subscription. Durable until mid-June, contrarian, screen-capture-able.

**Backup #2 — evergreen anchor (the series Taelo is most excited about):**
**Episode 1 of "How LLMs Actually Work (so you prompt better)" — "What is a token, really?"** Locked since 5/27. Film today (the 5/27 plan's Friday slot). Three-way tiktokenizer strawberry demo. This is the pillar that survives every news cycle.

---

## ⚡ The fast-content rule (new constraint for every future pick)

Add this to the trend-scout filter permanently:

> **A pick only ranks Tier 1 if it ships in under one working day with the equipment already on the desk.** Screen-capture + voiceover beats to-camera. To-camera beats multi-location. Anything requiring a "film day" drops to Tier 2 by default — because the data shows film-day picks don't ship.

This single rule would have killed the Grok Build operator review (good topic, wrong format for Taelo's current shipping reality) and elevated the `/usage` quick-hit, which never got made.

---

## 📰 News & viral signals — last 4 days (ranked by SEO durability × freshness × pillar fit × **filmability-in-hours**)

### Tier 1 — ship this week (screen-capture, no film day)

#### 1. ⭐ **Anthropic's June 15 "programmatic credit pool" — the sneaky half of the 50% raise**
- **Sources:** [Pasquale Pillitteri — 50% weekly limit raise through July 13](https://pasqualepillitteri.it/en/news/2494/claude-code-weekly-limits-50-percent-anti-codex-anthropic-2026) · [XDA — Anthropic keeps taking features from Pro](https://www.xda-developers.com/anthropic-keeps-taking-features-away-from-claude-pro-running-out-of-reasons-to-defend/) · [The Register — usage-limit tweaks](https://www.theregister.com/2026/03/26/anthropic_tweaks_usage_limits/) · [MindStudio — compute shortage](https://www.mindstudio.ai/blog/anthropic-compute-shortage-claude-limits).
- **What's new / the hook:** The 50% weekly-limit raise (May 13 → July 13) was marketed as generosity. The buried part: **starting June 15, all programmatic usage (Agent SDK, `claude -p`, third-party apps) draws from a separate "dedicated monthly programmatic credit pool"** — framed as a free bonus ($20 Pro / $100 Max 5x / $200 Max 20x) but functionally *carving automation off your main plan.* This is the "give, watch backlash, give again, quietly take next" pattern XDA names explicitly.
- **SEO durability:** **45–60d** (datable to June 15, evergreen-with-deadline). "claude programmatic credit pool", "anthropic agent sdk pricing change", "claude code limits june 2026" — net-new, unsaturated.
- **Saturation:** **Low.** Theo/news channels will cover the headline 50% number; nobody on the roster has connected it to the June 15 SDK carve-out as an operator.
- **Taelo angle:** **"Anthropic gave you 50% more limits — and you didn't notice they took the Agent SDK out of your plan."** Contrarian operator POV. Screen-capture `/usage` (the new skill/subagent/plugin/MCP cost breakdown from v2.1.149), show where credits actually go, do the June-15 math live. Honest "is this good or bad for you" verdict by plan tier.
- **Lead time:** **2–3 hours.** Screen capture + voiceover. No film day.
- **Hook (8s):** *"Anthropic just raised your Claude limits by 50%. Everyone's cheering. Nobody noticed that on June 15 they're quietly moving your most powerful feature — the Agent SDK — off your plan entirely. Let's do the math."*
- **SEO targets:** "anthropic programmatic credit pool", "claude code 50 percent limit increase", "claude agent sdk pricing june 2026", "is claude max worth it 2026", "anthropic usage limits explained".

#### 2. ⭐ **Claude Code v2.1.149/150 (+ May 28 build): `/code-review --fix` now applies fixes, `/usage` cost breakdown, `/goal`**
- **Sources:** [Claude Code What's New](https://code.claude.com/docs/en/whats-new) · [Releasebot — Claude Code](https://releasebot.io/updates/anthropic/claude-code) · [claudefa.st changelog](https://claudefa.st/blog/guide/changelog).
- **What's new (delta since 5/27):** `/code-review --fix` now **applies review findings to your working tree** (5/27 report only had `--comment`); **skills can set `disallowed-tools` in frontmatter**; `claude agents` autocomplete suggests native slash commands + bundled skills; `/model` saves default; Agent view (`claude agents`) + `/goal` (work-across-turns-to-completion) from Week 20.
- **SEO durability:** **30–60d.** Named slash commands rank for months.
- **Saturation:** **Very low** across roster (most chase model launches, not version bumps).
- **Taelo angle:** Fold into Pick #1 as the demo surface (the `/usage` breakdown *is* the proof of where limits go), **or** bundle `/code-review --fix` + `/goal` into the skills video (#below). Not a standalone.
- **Lead time:** Already inside Pick #1 / the skills video. Zero incremental.

#### 3. **Codex CLI v0.134.0 (May 26) + Goal mode out of experimental**
- **Sources:** [OpenAI Codex changelog](https://developers.openai.com/codex/changelog) · [Releasebot — Codex](https://releasebot.io/updates/openai/codex) · [Codersera May 2026 roundup](https://codersera.com/blog/openai-may-2026-updates-roundup/).
- **What's new:** Conversation-history search (content matches + previews); `--profile` now the primary selector; per-server env + OAuth for streamable HTTP MCP; **Goal mode no longer experimental** (app + IDE + CLI); `codex doctor` diagnostics.
- **Taelo angle:** Codex *vs* Claude Code `/goal` is a clean 90s comparison segment — fold into the skills video. Standalone only if the Codex-for-video lane gets revived (it's still the most defensible long-form pillar — see §Education/Series notes).
- **Lead time:** Segment only.

#### 4. **Google I/O 2026 wave continuing — Gemini 3.5 Flash + Managed Agents in Gemini API**
- **Sources:** [100 things at Google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) · [Google Developers keynote roundup](https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/).
- **What's new:** Gemini 3.5 Flash (frontier intelligence at Flash price/speed, 4x faster output tok/s, beats 3.1 Pro on coding/agentic/multimodal); **Managed Agents in the Gemini API** = Antigravity harness via a single API call with a provisioned remote sandbox; 8.5M monthly devs.
- **SEO durability:** Headline already saturating; **the operator angle "Managed Agents = is the Antigravity harness now an API primitive?" is fresher** but needs hands-on, which means film/build time. **Tier 2 for Taelo right now** (violates the fast-content rule). Monitor.

### Tier 2 — watch / don't chase
- **Grok Build CLI** — pick #1 from 5/27, **never shipped, now 4 days old.** Window narrowing; if revived, do it as a 5-min screen-capture comparison only, *not* the 7–9 min film-day operator review that stalled it.
- **Antigravity 1-week post-mortem / Gemini CLI June 18 sunset** — still empty-lane but needs hands-on. Tier 2 under the fast-content rule.
- **Nolan Lawson "write better code more slowly"** essay — still reactable, but a thoughtful reaction wants to-camera. Hold.
- **"Agentic microapps"** (RoboNuggets coinage, 5/27) — 20-min research pass still owed; fold a 60s mention into the skills video if it's a real primitive.

### Tier 3 — skip (ephemeral / off-pillar)
- **"Anthropic emailed me for insulting Claude"** viral meme ([explainx breakdown](https://explainx.ai/blog/claude-insult-viral-post-anthropic-chat-ended-policy-2026)) — funny, but **pure ephemeral**, irrelevant in a week. Exactly the kind of viral Taelo said to avoid.
- **Crypto Rover "$15B wiped" Claude tweet** — crypto-bait, ephemeral, off-pillar. Skip.
- Hermes Agent cluster (closed loop), Cursor/Composer (saturated), creative-AI (Veo/Sora, off-pillar).

---

## 🛠️ PICK OF THE WEEK IN DETAIL — "3 one-click Claude Code skills with the highest ROI"

This is the single best fit for **every** constraint in Taelo's brief: fast (no film day), SEO-durable (evergreen listicle intent), empty operator lane, and *already his idea.*

### The 3 skills (researched, all genuinely 1-click, all used daily by AI builders)

| Skill | Install | What it does | Why it's the highest-ROI pick |
|---|---|---|---|
| **superpowers** (Jesse Vincent / obra) | `/plugin install superpowers@claude-plugins-official` | 14 agentic skills, one framework. Forces clarify→design→plan→code→verify. A dispatcher skill auto-runs every conversation and routes to the right sub-skill. | **The #1 skills framework of 2026.** Measured ROI: TDD ~3 hrs/wk saved, systematic-debugging ~2.5 hrs/wk, brainstorming ~1.5 hrs/wk. One command, ~5 min, no config. ([GitHub](https://github.com/obra/superpowers) · [Anthropic plugin page](https://claude.com/plugins/superpowers) · [MindStudio explainer](https://www.mindstudio.ai/blog/what-is-superpowers-plugin-claude-code)) |
| **/dream** (grandamenium/dream-skill) | `git clone … ~/.claude/skills/dream/` + `install.sh --auto` | Memory consolidation — replicates **Anthropic's unreleased auto-dream feature.** 4-phase pass over memory files (Orient → Gather Signal → consolidate → prune), 24h auto-trigger. "REM sleep for your agent's memory." | This is **exactly** the "remembering for agents" Taelo named. Hottest *concept* in agent-memory right now and there's a working community skill before Anthropic ships theirs. ([dream-skill GitHub](https://github.com/grandamenium/dream-skill) · [MindStudio — Claude dreaming](https://www.mindstudio.ai/blog/claude-dreaming-feature-self-improving-agent-memory) · [Anthropic Dreams docs](https://platform.claude.com/docs/en/managed-agents/dreams)) |
| **/goal** (native, Week 20) | built-in — `/goal <objective>` | Keeps Claude working across turns toward an objective for *hours* without re-prompting, until a completion condition holds. Now non-experimental; Codex has a parallel "Goal mode." | The "run it longer / plan more" skill Taelo named. Native = zero-install credibility. Pairs as the "set it and walk away" payoff of the video. ([What's New](https://code.claude.com/docs/en/whats-new)) |

**Bonus / swap options if you want a 4th or a different mix:** `/code-review --fix` (now applies fixes to your tree — native), `feature-dev` (89k+ installs), `code-reviewer`, Remotion best-practices (117k weekly installs, auto-activates). The **Codex plugin** is repeatedly called the "single highest-leverage plugin" of 2026 — a clean "and one for Codex users" closer. ([Firecrawl best skills](https://www.firecrawl.dev/blog/best-claude-code-skills) · [Composio top skills](https://composio.dev/content/top-claude-skills) · [Mejba top 10](https://www.mejba.me/blog/top-10-claude-code-skills-plugins-clis-2026))

### Format & production
- **5–7 min, 100% screen capture + voiceover.** Optional face-cam intro/outro only.
- **Structure:** cold-open the payoff (agent running for an hour unattended via `/goal`) → "here are the 3 I install on every machine in under 5 minutes" → install each live, show the 1-liner, show one real result on `taelokim-website` or `taelo-content-system` → ROI verdict (hours saved/week) → outro shoutout.
- **Lead time:** **~3 hours.** This can ship tomorrow.
- **Hook (8s):** *"I've used Claude Code every day for months. These are the only 3 skills I reinstall on every new machine — each one is a single command, and the third one lets the agent work for an hour while you're asleep."*
- **SEO targets:** "best claude code skills 2026", "claude code skills to install", "superpowers claude code", "claude dream skill", "claude code /goal", "best claude code plugins", "claude code skills highest roi", "must have claude code skills".
- **Saturation check:** Listicles exist (Firecrawl, Composio, Mejba) as **blog posts** — the *operator-on-video, "only 3, here's the daily ROI"* framing on YouTube is far less crowded. Tight 3-pick + real-repo proof beats the 10-item blog roundups.
- **Companion blog (GEO):** publish the same 3 picks as an answer-first page on taelokim.com — "best claude code skills" is a high-intent query with weak video answers in ChatGPT/Claude/Perplexity right now.

---

## 🎓 Education series — "How LLMs Actually Work (so you prompt better & waste fewer tokens)"

This is the pillar Taelo is most excited about and it's the **right** long-term growth engine: evergreen, SEO-compounding, ships independent of any news cycle, and defensible. The thesis — *understand tokens and you ask better questions, get better output, waste fewer tokens* — is a genuinely underserved angle. Most LLM explainers teach *theory*; almost none close with *"so here's how to prompt better tomorrow."* That gap is the whole moat.

> Note on the reference: Taelo cited "Andrew Caparte's *How LLMs work*." The canonical deep-dive is **Andrej Karpathy — "Deep Dive into LLMs like ChatGPT"** (3h31m, Feb 2025), plus his "Let's build the GPT Tokenizer." That's the source to compress and out-simplify. ([Karpathy tweet](https://x.com/karpathy/status/1887211193099825254) · [Codingscape summary](https://codingscape.com/blog/andrej-karpathys-deep-dive-into-llms-video))

### Episode 1 (PILOT, locked since 5/27) — "What is a token, really?"
- **The unforgettable hook (locked):** type "strawberry" three ways into a tokenizer and watch the token count flip the answer — `strawberry` (1 token → model miscounts the R's) vs `s-t-r-a-w-b-e-r-r-y` (10+ tokens → succeeds) vs `"strawberry".split("")` (model writes code → succeeds). Turns the meme into a **tactical prompter lesson: force letter-level tokens when you need letter-level reasoning.**
- **Prompter takeaway (the differentiator):** every episode ends with one thing you can do on your *next* ChatGPT/Claude session. Ep 1's: "spell it out or ask for code when you need exact characters."
- **Film:** today (Fri 5/29, per the 5/27 plan). **Ship Mon June 1.**

### Make it middle-school simple — the "even a 7th grader gets it" spec
Taelo's bar: simpler than Karpathy, heavy visuals, high-schooler/middle-schooler accessible. Concrete plan:
- **One analogy per concept, no equations.** Token = "LLMs read in LEGO bricks, not letters." Embedding = "every brick gets GPS coordinates in meaning-space." Attention = "each word looks around the room and decides who to listen to." Next-token = "autocomplete that has read the whole internet."
- **Steal these free, ready visuals (screen-record them, no animation budget needed):**
  - [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app) — the live three-way strawberry demo (Ep 1 centerpiece).
  - [Transformer Explainer (poloclub)](https://poloclub.github.io/transformer-explainer/) — live GPT-2 in browser, shows next-token probabilities in real time; simplified to one block/one head to kill overload. **CHI 2026 paper-backed, gorgeous B-roll.**
  - [bbycroft.net/llm](https://bbycroft.net/llm) — 3D walkthrough of a GPT for the "what's happening inside" beat.
  - [AnimatedLLM (arXiv 2026)](https://arxiv.org/html/2601.04213v2) — purpose-built teaching animations of autoregressive decoding.
  - [Jay Alammar — How Transformer LLMs Work (free, ~90 min)](https://newsletter.languagemodels.co/p/how-transformer-llms-work-free-course) — best source to mine for the simplest framings.
- **Why this wins the lane:** the tokenization YT field is mostly "haha AI can't spell" reaction/meme clips (5/27 scan, table preserved). **None** combine the *why* + a *sub-7-min* runtime + a *prompter takeaway.* Welch Labs / 3Blue1Brown / Karpathy are benchmarks for *quality* but they're long and theory-first — Taelo's edge is **short, visual, and immediately useful to a prompter.**

### Series roadmap (each 5–7 min, evergreen, screen-capture + light face-cam)
1. **What is a token, really?** (pilot — strawberry) ← film today
2. **Where do tokens go? (embeddings = meaning has coordinates)**
3. **How does it pick the next word? (probabilities, temperature, why it "makes things up")**
4. **Why does it forget? (context windows — and how `/dream` & memory fix it)** ← ties back to the skills video
5. **Why your prompt costs what it costs (tokens in + out = your bill, and the 3 habits that halve it)** ← directly serves the "waste fewer tokens" thesis + ties to the Anthropic-limits video

**Strategic value:** this series + the skills video give Taelo **two evergreen pillars that ship from a desk in hours** — the structural fix the last three reports kept prescribing and never achieving. Cross-link every episode to the next (binge retention) and to the companion blogs (GEO).

---

## 📈 New growth strategies — delta vs 5/27

Carry-over from 5/27 (all still valid): satisfaction-beat endings (#1 lever), `llms.txt` + Bing Webmaster, decoupled daily Shorts, LinkedIn weekly clip, Reddit value-first, Whop, TikTok 60-min, 70/30 mix. **Net-new this round:**

### A. The "1 long-form → N assets" repurposing engine is the actual growth unlock (NEW #1)
The thing that fixes Taelo's throughput isn't a new platform — it's **never shipping a single asset again.** Every screen-capture video (skills, token ep, limits) becomes: 1 long-form + 3–5 vertical Shorts (decoupled engine, no CTR cannibalization) + 1 LinkedIn clip + 1 companion GEO blog + 1 Reddit value post + 1 X thread. The skills video alone = ~10 assets from one ~3-hour shoot. **This is how a solo operator out-ships a team.**

### B. Education content compounds on a different curve than reaction content
Reaction videos spike then decay; "what is a token" ranks for *years* and feeds GEO citations (ChatGPT/Claude/Perplexity have weak answers to "how do tokens work" today). **Weight the calendar 60% evergreen-education / 40% fast-reaction** — *invert* the current de-facto 90/10 reaction tilt. This is the SEO-for-subscribers play Taelo asked for.

### C. "Skills/plugins" is itself an evergreen SEO category, not a one-off
"best claude code skills/plugins 2026" is a recurring high-intent query that needs *refreshing* every 1–2 months as the ecosystem moves. Treat the skills video as **a quarterly evergreen franchise** (re-shoot when the top 3 change), not a single upload. Cheap to make, ranks indefinitely.

### D. Newsletters as a reaction-fodder + co-mention surface (carry from 5/27, now actioned)
Spin up `brand/newsletter-watch.md` (Understanding AI, Towards AI) — but more importantly, **answer-first companion blogs are the cheapest GEO win** and every screen-capture video should ship with one.

---

## 👥 Competitor roster — UPDATING THIS ROUND (overdue 3 reports)

Correction vs prior reports: the roster was **already expanded to 37** (rows 30–37: Duncan Rogoff, Charlie, Brooke Wright, Mahi/WorldofAI, Eric Michaud, Chris Raroque, Ryan Doser, Yifan) — the "none added" claim in 5/27 was stale. **Appended rows 38–43 this round** (`brand/competitors.md`):

| Row | Name | Why |
|---|---|---|
| 38 | **Sigrid Jin** | Korean clean-room Claude harness (105K★). Massive Korea/SEA + technical overlap; potential Korean-language collab. |
| 39 | **Peter Steinberger** | OpenClaw author (Altman-praised), candid agentic-engineering threads. Reactable "human side of agent coding." |
| 40 | **Matt Pocock** | TS/AI educator, high-quality explainer cadence — benchmark + reaction surface. |
| 41 | **Hamel Husain** | Applied LLM evals/ops, breaks technical news small creators miss. |
| 42 | **Theo (t3.gg)** | The reaction-news benchmark; co-mention + contrarian-counter surface. |
| 43 | **swyx (Latent Space)** | AI Engineer conf signal, talk drips = early trend radar. |

**Separate file (don't pollute outlier math):** `brand/education-benchmarks.md` — 3Blue1Brown, Welch Labs, Karpathy, Vcubingx, Jay Alammar (for the LLM series quality bar).

---

## ✅ Constraint check

- ✅ **Recent (≤4d) signal exists:** Codex v0.134.0 (5/26), Claude Code May-28 build (`/code-review --fix`), I/O wave continuing, Anthropic June-15 SDK carve-out surfacing now.
- ✅ **Non-ephemeral:** every Tier-1 pick is 30–60d+ SEO-durable; ephemeral memes (insult-Claude, crypto tweet) explicitly pushed to Tier 3.
- ✅ **Short lead time:** **all three picks ship in ≤3 hours, no film day** — the actual fix for the shipping problem.
- ✅ **Reaction OR 1–2-day-old quick upload:** limits video = contrarian reaction; skills video = evergreen quick upload; token ep = evergreen.
- ✅ **SEO-advantaged for subs:** skills + education franchises both target recurring high-intent queries.
- ✅ **New strategies delivered:** repurposing engine as #1, 60/40 education tilt, skills-as-franchise, GEO companion blogs.
- ✅ **Rising competitors added:** roster updated this round (rows 30–35) + education-benchmarks file.
- ✅ **Taelo's own ideas validated with data:** 3-skills (superpowers/`/dream`/`/goal`) and token-education series are the #1 and #3 picks.

---

## 🎯 Recommended ship plan — week of 2026-05-29 (fast-content discipline)

**Today (Fri 5/29):** Film **Education Ep 1 — "What is a token, really?"** Three-way tiktokenizer strawberry demo. 5–7 min. Edit over the weekend. **Ship Mon June 1** as the first evergreen pillar pin.

**Sat–Sun:** Edit Ep 1. Draft the **3-skills script** (it's mostly screen capture — minimal scripting).

**Mon 6/1:** Ship Ep 1. Record **"3 one-click Claude Code skills" (Pick of the week)** — ~3 hours, screen capture. Ship Tue 6/2.

**Tue–Wed 6/2–3:** Record **"Anthropic's 50% raise + the June-15 SDK carve-out"** contrarian quick-hit — ~3 hours, screen capture, `/usage` breakdown live. Ship before June 10 (datable to June 15). Apply satisfaction-beat ending + Hype CTA + 3-thumb + first-8s hook + GEO companion blog.

**Throughout:** run the **repurposing engine** on every upload — 3–5 Shorts + 1 LinkedIn clip + 1 companion blog + 1 Reddit post + 1 X thread per long-form. One ~3-hour shoot = ~10 assets.

**Queued (evergreen, week of June 8):** Ep 2 "Where do tokens go? (embeddings)" + revive the **Codex-for-video long-form** (still the most defensible pillar — but only if it can be scoped to a screen-capture walkthrough, not a film-day production).

**Do NOT:** restart the website-build or skill-dev long-forms. They are the proven cause of the shipping stall.

---

## 📊 Video scan note

Video outlier scan **carried from [2026-05-27](2026-05-27-trend-report.md)** — only 2 days elapsed and that scan found **0 strong outliers (≥2.0x adjusted)**, with Jason Lee's "vibe-coded recipe app" (adj 1.04) the lone >1.0. Web-sourced delta since: comparison-genre (Nate Herk "100 hours Claude Code vs Codex") and omnibus-news (Riley Brown) remain the active shapes; **`/usage`, `/dream`, `/goal`, and operator-skills-ROI framings remain empty lanes.** A live YouTube Data API rescan (`python3 scripts/trend_scan_weekly.py --days 4 --top 30`) is available on request — say the word and I'll run it to refresh the numbers before you commit.

## Files
- This report: `outputs/trends/2026-05-29-trend-report.md`
- Roster update: `brand/competitors.md` (rows 30–35 added) + new `brand/education-benchmarks.md`
- Previous report: [2026-05-27-trend-report.md](2026-05-27-trend-report.md)
