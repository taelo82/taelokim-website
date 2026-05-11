# Intro Draft — Warp Open-Source Reaction (2026-05-11)

**Working title (pick one):**
- *"Warp Just Went Open-Source. I'm Replacing My Whole Terminal."*
- *"Warp Is Free Now. Here's the Setup That Replaces Cursor."*
- *"The Best AI Terminal Just Went Open-Source (OpenAI Is Paying For It)"*

**Target length:** 8–11 min · **Format:** reaction + 10-min operator setup walkthrough · **Lead time:** today

**Why this pick:**
- 56K+ GitHub stars in days · Product Hunt #1 May 11 · HN front page May 10
- Fewer than 5 YouTube videos on the open-source release exist right now → SEO lane is wide open
- Evergreen install/setup keyword ("Warp open source", "Warp install Claude Code", "Warp vs iTerm")
- Visual identity for Claude Design: **purple/violet gradient + terminal-block UI** is iconic and instantly readable
- OpenAI as founding sponsor of a competitor's tool is a real drama beat — strong cold-open material

---

## 🎬 Cold open (0–8 seconds) — the hook

> **The most expensive AI terminal on the market just went free. And OpenAI is paying for it.**
>
> *[B-roll: Warp logo → GitHub star counter ticking from 0 to 56,000 → cut to Taelo's terminal already running Warp]*

Why this hook works: pattern interrupt (price collapse), surprise (OpenAI funding a non-OpenAI tool), and concrete number (56K stars) all in two sentences. No hedging, no "in this video we'll explore."

---

## 🪝 Setup (8–22 seconds) — the stakes

> Two days ago, Warp flipped their entire agentic terminal open-source under AGPL. That's the tool I've been paying $20 a month for. Same day, OpenAI announced they're the founding sponsor. So your terminal is now the cheapest, most capable AI surface you can install — and the company building it is being bankrolled by the model lab whose agent you're probably already running inside it.
>
> *[B-roll: split-screen — old "Pro tier" pricing page → strikethrough → GitHub repo "MIT/AGPL" banner]*

---

## 🎯 Promise (22–35 seconds) — what they'll get

> In the next 10 minutes I'm going to install it cold, wire up Claude Code as the agent, run it in parallel with Codex from the same terminal, and tell you the one AGPL gotcha most people are about to walk into. If you ship anything from a terminal, this changes your stack today.
>
> *[B-roll: hands typing `brew install warp` → terminal splits into two panes, one labeled Claude Code, one labeled Codex]*

---

## 🎨 Claude Design intro brief (paste this into Claude Design)

> **Brief:** Build an intro graphic and animated lower-third for a YouTube video titled *"Warp Just Went Open-Source. I'm Replacing My Whole Terminal."* The video is a reaction + operator-POV install walkthrough by Taelo Kim (small AI/Claude Code creator).
>
> **Visual identity:**
> - Background: Warp's signature deep-purple → violet → magenta vertical gradient (#1B1033 → #6B2EFF → #B05CFF), with a subtle film grain
> - Foreground center: stylized terminal "block" (Warp's signature UI element — rounded rectangle, monospace caret, faint glow). Inside the block: the text `> warp open-source` typing out
> - Floating around the terminal block: three small orbiting glyphs — Claude (Anthropic mark), OpenAI rosette, Gemini star — implying "any agent, one terminal"
> - Stamp overlay (top right, 15° rotation): red `OPEN SOURCE` distressed stamp
>
> **Animations needed:**
> 1. **0–3s open card:** background gradient resolves → terminal block fades in → caret blinks → `warp open-source` types in
> 2. **3–5s reveal:** red stamp slams in, orbiting agent glyphs spin into place
> 3. **Lower-third (reusable):** Warp-purple bar that slides in from the left with "Taelo Kim · /vibe-coding" in monospace
>
> **Style notes:**
> - Cinematic, not corporate. No stock-vector look.
> - Terminal monospace font (JetBrains Mono or Fira Code)
> - Title-card text is short ("Warp Goes Free"). Avoid full sentences in graphics — the voice carries the message
> - Match Warp's actual brand chroma, do not soften — the purple is the recognizable signature
>
> **Output formats requested:**
> - 16:9 intro card (3840×2160 PNG, static "title frame" version)
> - Animated MP4 (5 sec, 4K, transparent BG, 60fps) for opening sequence
> - Reusable lower-third PNG sequence (1080p, transparent)
> - One 1280×720 thumbnail variant: terminal block + giant `OPEN` text covering left half, OpenAI rosette in corner

---

## 📋 Shot list for the rest of the video (operator section)

For when you come back to the laptop after the intro is built:

1. **Install Warp from open-source build** (~90 sec) — `git clone`, build, first launch. Show the AGPL license screen.
2. **Wire up Claude Code** (~2 min) — paste your existing API key, point at Claude Code config, verify the agent appears in the command palette.
3. **Wire up Codex side-by-side** (~2 min) — second pane, second agent. Same prompt run in both panes — show the diff in approach.
4. **The "any agent, one terminal" demo** (~2 min) — one task, route to both agents, compare output side-by-side.
5. **The AGPL gotcha** (~90 sec) — AGPLv3 means if you fork and host as SaaS, you must open-source your fork. State it cleanly so viewers don't get burned.
6. **Beat 9 outro** (~45 sec) — shoutout to the byteiota writeup and Warp team (per reaction-video creator-mention rule, source creators land here, not in body).

**Note:** Do NOT name any AI YouTubers in the body of the script — Beat 9 outro shoutout only, per standing rule.

---

## Sources cited in the video

- [Warp is now open-source — official blog](https://www.warp.dev/blog/warp-is-now-open-source)
- [warpdotdev/warp on GitHub](https://github.com/warpdotdev/warp) — pin the repo URL
- [Hacker News thread](https://news.ycombinator.com/item?id=47937349) — for the AGPL discussion
- [byteiota writeup — 37K stars in days](https://byteiota.com/warp-terminal-open-source-agentic-dev-environment/)
- [Product Hunt May 11](https://www.producthunt.com/leaderboard/daily/2026/5/11/all)
