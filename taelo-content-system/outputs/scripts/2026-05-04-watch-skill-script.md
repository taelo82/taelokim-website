# Script — 2026-05-04 — `/watch` skill (Taelo edition)

> Narrative rule: No direct mentions of the skill's creator inside the body of the video. Shoutout lands at the very end of the outro. Install commands keep the real GitHub path because the audience needs to be able to copy them.

## Topic
Install the free Claude Code `/watch` skill. Frame it for the audience (creators / AI learners / builders). Demo it on a video everyone is already covering. Go beyond the original by showing the Trend Scout × `/watch` operator pipeline.

## Source / Why this exists
- Trend report: [outputs/trends/2026-05-04-trend-report.md](../trends/2026-05-04-trend-report.md). Top pick of the week — 3.83x outlier on a 6,740-sub channel. First video to cross the strong-outlier threshold.
- Original skill video (private reference, not mentioned on-camera): https://youtu.be/QZMljuD10sU
- Skill repo: https://github.com/bradautomates/claude-video
- Original transcript (private reference): [transcripts/QZMljuD10sU-brad-bonanno-pick.txt](../trends/transcripts/QZMljuD10sU-brad-bonanno-pick.txt)
- **Demo target**: Gary Tan / Y Combinator — *"How to Make Claude Code Your AI Engineering Team"* (GStack walkthrough). https://www.youtube.com/watch?v=wkv2ifxPpF8 — 137K views, 21:49, posted 2026-04-23. Pre-pulled transcript: [transcripts/wkv2ifxPpF8-demo-target.txt](../trends/transcripts/wkv2ifxPpF8-demo-target.txt)

## Format Note
VO/SCREEN block format. Record OBS for demo + setup beats, voiceover the rest. Aim 8-10 minutes total — 70% talking, 30% screen capture.

---

## Titles (3 options)

1. ⭐ **I made Claude watch every AI video for me. Here's the free skill.** — 56 chars. Pattern: outcome + "free" payoff.
2. **The free Claude skill that replaced my AI newsletter stack** — 56 chars. Concrete substitution angle.
3. **Brad gave away the missing Claude superpower. I tested it for a week.** — 65 chars. Authority + tested.

## Thumbnail Direction
Split screen. Left: stacked grid of 6-8 YouTube thumbnails greyed out with red Xs. Right: Claude terminal showing a clean structured summary output. Center caption: **"WATCH ANY VIDEO IN 2 MIN"** with **FREE** stamp. Taelo face inset bottom-left, slight smirk.

## Hooks (5 options)

1. ⭐ "It is just physically impossible to consume every AI video on YouTube. So I made Claude do it for me."
2. "Claude couldn't watch videos. Until last week. This is going to break your content workflow — in a good way."
3. "Three weeks ago I was screenshotting frames into Claude. This week Claude watches videos for me. Here's how."
4. "Brad's free Claude skill just replaced 90% of my AI newsletter stack."
5. "Everyone is talking about new Claude tools. Here's the one nobody is talking about — and it's free."

---

## Beat 1 — Intro (combined: Taelo revised draft 2026-05-05 + take-1 polish)

🎙️ **VO**:

> It is just physically impossible to consume every AI video on YouTube. It's just impossible.
>
> So we all try the same thing. We tell Claude — or whatever agent we're using — "hey, watch this video for me." We drop a URL and we wait, hoping it spits out a summary. And what you get back, every single time, is: *"Sorry, I can't watch the video. But based on the title and caption, let me guess. Or, if you give me the transcript, maybe I can extract something."* That happens to me all the time. And it kills me — because I just wanted Claude to actually watch the damn video.
>
> Here's the thing. Having a transcript and guessing from a still frame is vastly different from actually *watching* the video and seeing what's on the screen. The full context only shows up when Claude can see the demo, the visual, the moment the screen actually changes — not just read the words floating around it.
>
> And here's what's worse. Inside Claude Code, when I'm building anything — even my own website, my own video — I end up screenshotting frame by frame. Different sections of the screen. Paste, paste, paste, until Claude finally has enough context to be useful. Audio and transcript alone don't cut it. There's always more happening on screen than what the words tell you.
>
> Every creator, every builder, every learner has this exact problem. Claude Code can't watch video. And video is *exactly* where the demos, the news, the long-form instruction lives — because the best AI content right now is being shipped as video, long and in depth.
>
> So we're going to fix that. By the end of this video, you're going to have the same thing I've been using every single day for the past few days — a free Claude skill that watches any URL you give it, gives you back a real structured summary, and saves you ninety percent of the content firehose. This might be one of the most beneficial skills I've ever incorporated. It quietly changes how you work.
>
> Here's how I'm going to take you through it. Three parts:
>
> 1. **How it works.**
> 2. **How to set it up — with a live demo.**
> 3. **What to actually do with it once you have it.**
>
> Let's get straight in.

🖥️ **SCREEN**: Cold open on Taelo. Cut to a montage of YouTube AI-tool thumbnails flying past too fast to read. Cut to Claude Code terminal showing the "Sorry, I can't watch the video" response. Cut to old screen recording of Taelo screenshotting frames into Claude one at a time (real footage if you have it). End on a clean lower-third "1. How it works · 2. How to set it up · 3. What to do with it" graphic.

⏱️ ~100-110s

### Applied changes (combined intro 2026-05-05)
- ✅ Universal "we all try the same thing" framing replaces solo "me" framing — broader entry point.
- ✅ New diagnostic line: "transcript and guessing from a still frame is vastly different from actually *watching*" — sharper articulation of the pain.
- ✅ "Every creator, every builder, every learner has this exact problem" — universal pain elevation; explains why video-as-medium matters.
- ✅ **New three-part roadmap at the end** (How it works / How to do it / What to do with it) — explicit retention scaffold.
- ✅ Kept the screenshot-frame-by-frame story (your unique credibility moment from take-1).
- ✅ Kept "quietly changes how you work" closer.
- ✅ Removed redundant restatement of "Sorry, I can't watch" — said cleanly once.
- ✅ Removed the "I've tried a lot of tools to fix this. Most of them are bad" hedge — pace straight through to the promise instead.

---

## Beat 2 — What `/watch` actually does (the unlock)

🎙️ **VO**:

> Here's what just changed. There's a free Claude skill called `/watch`. You give it any video URL — YouTube, Loom, Vimeo, X, even a local file — and Claude actually watches it. Frames and transcript together. Not reading the captions and pretending. Watching.
>
> By the time I press play on a video, Claude is already done. Forty-five-minute interview, eight-minute tutorial, doesn't matter. Done in under two minutes.
>
> And the punchline: it costs about a dollar per video. Sometimes free. I'll show you the math later.

🖥️ **SCREEN**: Type `/watch <URL>` into Claude. Hit enter. Time-lapse of frames extracting → transcript pulling → Claude responding. Stamp the wall-clock at the corner so the speed is visible.

⏱️ ~25s

---

## Beat 3 — Live demo (the moment that earns the video)

> **Demo target locked**: Gary Tan's *"How to Make Claude Code Your AI Engineering Team"* (Y Combinator) — the GStack walkthrough. 137K views in 11 days, every Claude Code creator is reacting to it, and at 21:49 it's exactly the kind of video nobody has time to actually sit through. Confirmed `/watch` runs on it end-to-end (60 frames + full transcript pulled in under 2 min).

🎙️ **VO**:

> Let me show you what this looks like in real life. Right now I'm pulling up the Y Combinator video everyone has been reacting to — Gary Tan walking through GStack, his open-source skill stack for Claude Code. It's twenty-two minutes long. Six different creators have already reacted to it this week. Honestly, I don't have time to watch all of them and figure out who has the best take.
>
> So I'm going to do this instead. Type `/watch`, paste the URL, and ask Claude one question: *"What's the actual workflow? What's the part Gary glossed over? And what's the one thing you'd warn me about before I try GStack on my own codebase?"*
>
> Watch what happens.

🖥️ **SCREEN**: Live screen recording. Type the command. Hit enter. Time-lapse the frame-extraction + transcript pull (it really does finish in under 2 min). Jump cut to the structured response from Claude. Highlight: actual workflow steps, the glossed-over part, the warning. Side panel showing the source video timeline.

🎙️ **VO** (over the output):

> Two minutes. I now know more about GStack than I would after watching the full video, because Claude pulled the on-screen demo, the spoken explanation, and the timestamps where Gary's setup actually mattered. I can use this output as the source for my own GStack video. I can decide if it's worth installing. I can save it. I can search it. I can reference it next month when somebody asks me about it.

⏱️ ~90s including demo runtime

---

## Beat 4 — Setup (with the SABR caveat — the killer differentiator)

🎙️ **VO**:

> Now let me get you set up. The original demo makes the install look easy. Five minutes, two commands, done. And it is — most of the time.
>
> But here's what no other reaction video is going to tell you. The day I installed this skill, YouTube was actively fighting yt-dlp on every download. 403 errors. Blocked fragments. The whole mess. The original demo doesn't show that part. So I'm showing you both — the clean path and the messy one I had to actually live through.

🖥️ **SCREEN**: Terminal split-screen. Left side: clean install. Right side: SABR errors flying.

🎙️ **VO**:

> Easy path first. In Claude Code, run these two commands:
>
> `/plugin marketplace add bradautomates/claude-video`
> `/plugin install watch@claude-video`
>
> Restart Claude Code. You're done. Point `/watch` at any video. The skill auto-installs FFmpeg and yt-dlp the first time it runs on macOS. On Linux or Windows, it tells you the exact install command for your system. Then grab a free Groq API key from console.groq.com — that handles the videos that don't have captions. That's the whole install.

🖥️ **SCREEN**: Show the install commands typing live. Cut to the Groq dashboard signup.

🎙️ **VO**:

> Messy path — when YouTube actually blocks the download. You'll need four things. Python 3.11 or higher, because the older Python that ships with macOS doesn't run the latest yt-dlp. The latest yt-dlp itself, installed through `uv`. Deno, because the new YouTube SABR streaming protocol needs a JavaScript runtime to solve a challenge. And browser cookies, because YouTube wants to verify you're a real person.
>
> I'll drop the exact copy-paste install in the description. Five commands, fifteen minutes, fixes everything. Save this video. You'll need it the day YouTube decides to fight you.

🖥️ **SCREEN**: Show the patched download.py snippet. Show `uv tool install --pre yt-dlp[default]` running. Show Deno installing. Show `/watch` running successfully on a YouTube video right after.

⏱️ ~110s

---

## Beat 5 — Under the hood (compressed)

🎙️ **VO**:

> How does this actually work? Two old, free, open-source tools doing the heavy lifting. yt-dlp downloads the video. FFmpeg slices it into frames and pulls the audio. If the source has captions — most YouTube videos do — you get the transcript free. If not, Whisper on Groq transcribes the audio for almost nothing. Claude reads the frames like a flipbook and the transcript like a script, and the timestamps line up.
>
> No new model. No expensive API. Just the right glue.

🖥️ **SCREEN**: Simple animated flow diagram, or stacked terminal panels showing the pipeline.

⏱️ ~25s

---

## Beat 6 — Cost math (the real numbers)

🎙️ **VO**:

> And the most beautiful part of all of this — it's almost completely free.
>
> Assume you already pay for Claude. Twenty bucks a month for Pro, which is what I'm on. Even if you don't, the graph I'm about to show you is going to convince you.
>
> My Anthropic dashboard for this month: zero. Zero dollars. Because `/watch` runs inside the Claude Code subscription you're already paying for. There's no extra API bill on top.
>
> The only thing that costs anything is transcription, and only when the video has no captions. I've run this on many videos so far. Most had captions: free. One didn't: two cents on Groq. Not two dollars. Two cents.
>
> And the funny thing is: you don't pay Groq the subscription until you hit the limit. So you're essentially using it for free until you use it too much that they ask you to pay.
>
> Unless you're feeding it an endless stack of documentaries with no subtitles, the free tier covers you. Most weeks this whole pipeline costs me less than a coffee.

🖥️ **SCREEN**: Anthropic console screenshot — zoom on `USD 0.00` and "No data" panels. Cut to Groq dashboard zoom on `$0.02 USD` total spend. Cut to the 2-line Groq Logs view showing the single 247-second Whisper run.

⏱️ ~50s

### Real numbers (validated 2026-05-06)
- Anthropic API cost (Month-to-date): **$0.00** — `/watch` runs inside Claude Code Pro subscription, never hits the API directly.
- Groq Whisper cost (Month-to-date): **~$0.07** — five Whisper transcription jobs (your three face-cam takes from 2026-05-04 + the Beat 1 take + the long master take from 2026-05-06).
- Verified `/watch` runs across the project: 7 (Brad source, Gary Tan GStack, three face-cam recursive takes, Beat 1 take, master take). 2 used captions → $0; 5 used Whisper → ~$0.07.
- Groq free-tier still active (you don't actually get billed until you upgrade — they let you accumulate "projected cost" until you opt in).

---

## Beat 7 — Use case 1: Trend Scout × `/watch` (the unique operator angle)

🎙️ **VO**:

> Here's where it gets interesting for me. This is the part no other tutorial about this skill is going to show you.
>
> I already run a system I call Trend Scout. The day I'm hunting for a new video, I fire it. It scans 24 AI YouTubers, ranks the ones that broke at least double their channel's average views, and tells me which one is worth my attention right now.
>
> Until now I'd have to actually sit down and watch the winner. Twenty, thirty minutes per video. Now I don't. Trend Scout picks the video. `/watch` ingests it. Claude gives me back a structured breakdown — what's the hook, what's the visual setup, where's the surprise, what's the punchline.
>
> Twenty minutes of work compressed into two minutes.
>
> This is the part I want creators to copy. You don't need a 40-person research team. You need a tiny scanner and a skill that watches the videos for you.

🖥️ **SCREEN**: Show the live trend report markdown file. Cut to Claude Code running `/watch` on the top-pick URL. Cut to the structured output. Cut to a file system view of the saved summary.

⏱️ ~60s

---

## Beat 8 — Use case 2: Skip the cron-job theater

🎙️ **VO**:

> Here's where I'm going to disagree with almost every other creator running a stack like this.
>
> A lot of people are stockpiling. Obsidian vaults full of competitor breakdowns. Cron jobs scraping every channel they care about every six hours. Daily digests. Weekly intelligence reports. "Compounding library" this, "second brain" that.
>
> I think most of it is waste.
>
> In AI, a video about a tool from three days ago is already half-stale. A breakdown of last month's hot launch? Dead weight. The cron jobs and routines creators set up to "compound their intelligence" — by the time you actually need any of it, the answer has changed.
>
> So I don't compound. I run `/watch` and Trend Scout the moment I'm hunting for a video. Not before. Not on a schedule. The day I sit down to ship something, I do the scan fresh, I `/watch` the top three, I pull what's true *right now*, and then I move.
>
> The leverage isn't in the library. The leverage is in the skill being fast enough that you don't *need* a library.

🖥️ **SCREEN**: Split-screen contrast. Left: a stale-looking Obsidian-style vault — file tree of competitor MDs, last-modified dates from weeks ago, faded/greyed. Right: a fresh terminal, today's date showing prominently, `/watch` kicking off live and the structured output landing in under two minutes. Caption tag: **"scheduled vs. on-demand."**

⏱️ ~70s

---

## Beat 8.5 — Why this is a breakpoint (zoom-out before the outro)

> Placement note: lands here on purpose. The viewer just absorbed the use cases — now zoom out to "what this actually means in the AI content landscape." Keeps the demo→install momentum from Beats 3–4 unbroken, gives the video a thesis-grade capstone before the CTA.

🎙️ **VO**:

> Step back for a second. There are two big parts left in AI content right now.
>
> First one: scripting and filming. You can't fully delegate this — and honestly you shouldn't want to. You have your own voice. You like a certain way of saying things. AI would need a mountain of your existing content to mimic that exactly, and even then you'd want to fix it. So filming, the human side, that's not going anywhere.
>
> Second one: editing. Taste lives there. You're choosing between takes. You're deciding the structure. Motion graphics, b-roll, captions popping out — every AI editing tool I've tried still needs a human sitting on top of it. That part isn't solved.
>
> But this — `/watch` — is one of the breakpoints. Claude Code can now make Claude Code actually watch videos. Not just read transcripts, not just listen — watch. You just gave your senior editor or your producer the ability to see, when before they could only read or hear.
>
> It doesn't write the script for you word-for-word. But it eats almost all the research time. Where are the trends going? How are the best videos structured? What's working this week? That pattern recognition — Claude can now do it for you. So the scripting half just got solved. Or at minimum, we're in the middle of solving it.

🖥️ **SCREEN**: Whiteboard-style animation. Two columns locked: "Filming" (human icon) and "Editing" (taste/scissors icon). Third column: "Research / Scripting" with `/watch` logo punching through, unlocking it. Cut to a fast montage of Trend Scout report → `/watch` summary → script doc.

⏱️ ~85s

---

## Beat 9 — Outro (with shoutout)

🎙️ **VO**:

> That's the playbook. The skill is free, the repo is in the description, and my install patch for when YouTube decides to fight you is right under it.
>
> One last thing. I would not be running this video today if it weren't for Brad Bonanno — he built and gave away this `/watch` skill for free, and his original walkthrough is what got me to install it in the first place. Big shoutout. His video is linked first in the description. Go subscribe to him too.
>
> If you build the Trend Scout side — the recurring scanner that feeds `/watch` — show me. I'll run yours through `/watch` and put the breakdown in next week's video.
>
> And before you go — if you want to see how I pull thirty grand doing marketing for small brands and companies, or how I'm building more cinematic websites with Claude Code and Claude design, that video is right here. Hit it.
>
> Subscribe if you want the next operator playbook. See you in the next one.

🖥️ **SCREEN**: GitHub link card. Brad's video thumbnail with arrow. End card with subscribe + next video preview.

⏱️ ~30s

---

## Total runtime estimate
- Voiceover: ~9m 25s (added Beat 8.5 ~85s + Beat 6 cost expansion ~25s)
- Demo + screen capture filler: 1-2m
- **Target final length: 10-12 minutes** ✅ (still inside the 8-12 sweet spot in voice.md, lands at the upper end)

---

## Install state (validated 2026-05-04)

- ✅ Python 3.11.15 installed via `uv`
- ✅ yt-dlp 2026.05.03 nightly + EJS plugin installed
- ✅ Deno 2.7.14 installed (JS runtime for SABR challenge solver)
- ✅ FFmpeg 6.0 already present
- ✅ curl_cffi installed for YouTube impersonation
- ✅ Groq API key configured at `~/.config/watch/.env`
- ✅ `download.py` patched with `WATCH_COOKIES_BROWSER` env var + player_client override
- ✅ End-to-end test on Gary Tan's GStack video: **PASSED** — 60 frames + transcript pulled in under 2 min

## Open questions for Taelo

1. **Real numbers in Beat 6** — the "$1/video, 10 videos/week" numbers are illustrative. Want me to pull your actual Anthropic dashboard data before recording, or keep them as estimates?
2. **Description copy-paste install doc** — want me to write the 5-command "messy path" install as a separate file ready to paste into the video description?
3. **Brad shoutout placement** — current draft puts it in the outro (Beat 9). Want it moved earlier or kept where it is?
4. **Run `/watch` on the GStack video now** — since the skill is fully working, do you want me to invoke it and produce a real structured breakdown of Gary Tan's video that you can use as the demo material in Beat 3? I can save the output so you can use it directly while recording.
