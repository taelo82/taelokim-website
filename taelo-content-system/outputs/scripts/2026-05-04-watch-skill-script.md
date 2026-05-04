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

## Beat 1 — Intro (polished from Taelo draft 1)

🎙️ **VO**:

> It is just physically impossible to consume every AI video on YouTube. It's just impossible.
>
> Honestly, this is the part that broke me. Every time I drop a URL into Claude and ask for a summary, it tells me, "Sorry, I can't watch the video — but based on the title and caption, let me guess." That happens to me all the time. And it kills me, because I just wanted Claude to watch the damn video and give me a summary.
>
> Here's what's worse. In Claude Code, when I'm building anything — even my own website or my own video — I end up screenshotting frame by frame. Different sections of the screen. Paste, paste, paste, until Claude finally has enough context to actually be useful. Audio and transcript alone don't cut it. There's always more happening on screen than what the words tell you.
>
> I've tried a lot of tools to fix this. Most of them are bad.
>
> So if you're a creator, someone learning AI, or someone building with AI — by the end of this video I'll show you the free Claude skill I'm now using every single day. You give it any URL. You get a real structured summary you can use for your next video, use to learn faster, or use to skip 90% of the content firehose. This is one of those skills that quietly changes how you work.

🖥️ **SCREEN**: Cold open on Taelo. Cut to a montage of YouTube AI-tool thumbnails flying past too fast to read. Cut to Claude Code terminal showing the "Sorry, I can't watch the video" response. Cut to old screen recording of Taelo screenshotting frames into Claude one at a time (real footage if you have it).

⏱️ ~80s

### Applied changes (Taelo's notes)
- ✅ "Just another revolution of surpassing" → swapped for "This is one of those skills that quietly changes how you work."
- ✅ Screenshot frame-by-frame story moved up — now sits right after the "watch the damn video" line. It's the strongest credibility beat in the intro and lands harder there.
- ✅ Cleaned to native-English cadence while keeping the direct, raw, conversational tone (per voice.md).
- ✅ Removed forbidden phrases (no "in today's video", "without further ado", etc.).

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

> The real numbers, since I always promise that. Per video, around one dollar in Claude tokens. I watch about ten competitor videos a week — that's ten dollars. I was paying more than that for AI newsletters that gave me less.
>
> Whisper on Groq's free tier covers basically every video without captions. I haven't been charged for transcription once.
>
> Most weeks, this whole pipeline costs me less than a coffee.

🖥️ **SCREEN**: Anthropic dashboard usage screenshot. Highlight the per-video cost. Cut to Groq dashboard showing free-tier remaining.

⏱️ ~25s

---

## Beat 7 — Use case 1: Trend Scout × `/watch` (the unique operator angle)

🎙️ **VO**:

> Here's where it gets interesting for me. This is the part no other tutorial about this skill is going to show you.
>
> I already run a system I call Trend Scout. Every Monday, it scans 24 AI YouTubers, ranks the videos that broke at least double their channel's average views, and tells me which one is worth my attention this week.
>
> Until now I'd have to actually sit down and watch the winner. Twenty, thirty minutes per video. Now I don't. Trend Scout picks the video. `/watch` ingests it. Claude gives me back a structured breakdown — what's the hook, what's the visual setup, where's the surprise, what's the punchline.
>
> Twenty minutes of work compressed into two minutes.
>
> This is the part I want creators to copy. You don't need a 40-person research team. You need a tiny scanner and a skill that watches the videos for you.

🖥️ **SCREEN**: Show the live trend report markdown file. Cut to Claude Code running `/watch` on the top-pick URL. Cut to the structured output. Cut to a file system view of the saved summary.

⏱️ ~60s

---

## Beat 8 — Use case 2: Solo operator competitive intelligence

🎙️ **VO**:

> The second use case is where the leverage really compounds.
>
> I'm building in public, alone, against teams that have copywriters, editors, researchers on payroll. I don't have a 40-person team. I have one Claude Code subscription and this `/watch` skill.
>
> Here's what I'm doing. Every video that scores above a 2x outlier in my Trend Scout, `/watch` grabs the structured summary and saves it into a single file. Searchable. Tagged by topic. Linked back to the source. After a month I have a competitive intelligence layer that took the agencies a whole department to build.
>
> The leverage isn't the skill. The leverage is the skill stacked into a recurring pipeline that runs every week without me touching it.

🖥️ **SCREEN**: Show the markdown library file growing — entries with topic tags, source links, summaries. Scroll through. Pull up search. Show how fast you can find a specific competitor's hook breakdown from three weeks ago.

⏱️ ~55s

---

## Beat 9 — Outro (with shoutout)

🎙️ **VO**:

> That's the playbook. The skill is free, the repo is in the description, and my install patch for when YouTube decides to fight you is right under it.
>
> One last thing. I would not be running this video today if it weren't for Brad Bonanno — he built and gave away this `/watch` skill for free, and his original walkthrough is what got me to install it in the first place. Big shoutout. His video is linked first in the description. Go subscribe to him too.
>
> If you build the Trend Scout side — the recurring scanner that feeds `/watch` — show me. I'll run yours through `/watch` and put the breakdown in next week's video.
>
> Subscribe if you want the next operator playbook. See you in the next one.

🖥️ **SCREEN**: GitHub link card. Brad's video thumbnail with arrow. End card with subscribe + next video preview.

⏱️ ~30s

---

## Total runtime estimate
- Voiceover: ~7m 35s
- Demo + screen capture filler: 1-2m
- **Target final length: 8-10 minutes** ✅ (matches your 8-12 sweet spot in voice.md)

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
