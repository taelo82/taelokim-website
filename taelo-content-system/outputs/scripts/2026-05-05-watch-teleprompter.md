TELEPROMPTER — /watch reaction video — face-cam VO only
========================================================

How to use:
  - The HEADER lines in ALL CAPS are your shoot cues. Skim them, do NOT read them aloud.
  - Read everything below the header until the next ============ separator.
  - Beat 3 is already shot (3 takes). Skip it.
  - Beat 8.5 is OPTIONAL — see note in its block.

================================================================
BEAT 1  —  INTRO
ORDER 1 of 9   |   ~110 sec   |   shoot while voice and energy are freshest
================================================================

It is just physically impossible to consume every AI video on YouTube. It's just impossible.

So we all try the same thing. We tell Claude — or whatever agent we're using — "hey, watch this video for me." We drop a URL and we wait, hoping it spits out a summary. And what you get back, every single time, is: "Sorry, I can't watch the video. But based on the title and caption, let me guess. Or, if you give me the transcript, maybe I can extract something." That happens to me all the time. And it kills me — because I just wanted Claude to actually watch the damn video.

Here's the thing. Having a transcript and guessing from a still frame is vastly different from actually watching the video and seeing what's on the screen. The full context only shows up when Claude can see the demo, the visual, the moment the screen actually changes — not just read the words floating around it.

And here's what's worse. Inside Claude Code, when I'm building anything — even my own website, my own video — I end up screenshotting frame by frame. Different sections of the screen. Paste, paste, paste, until Claude finally has enough context to be useful. Audio and transcript alone don't cut it. There's always more happening on screen than what the words tell you.

Every creator, every builder, every learner has this exact problem. Claude Code can't watch video. And video is exactly where the demos, the news, the long-form instruction lives — because the best AI content right now is being shipped as video, long and in depth.

So we're going to fix that. By the end of this video, you're going to have the same thing I've been using every single day for the past few days — a free Claude skill that watches any URL you give it, gives you back a real structured summary, and saves you ninety percent of the content firehose. This might be one of the most beneficial skills I've ever incorporated. It quietly changes how you work.

Here's how I'm going to take you through it. Three parts.

One. How it works.
Two. How to set it up — with a live demo.
Three. What to actually do with it once you have it.

Let's get straight in.


================================================================
BEAT 2  —  WHAT /WATCH ACTUALLY DOES
ORDER 2 of 9   |   ~25 sec   |   stay in flow, short and punchy
================================================================

Here's what just changed. There's a free Claude skill called slash-watch. You give it any video URL — YouTube, Loom, Vimeo, X, even a local file — and Claude actually watches it. Frames and transcript together. Not reading the captions and pretending. Watching.

By the time I press play on a video, Claude is already done. Forty-five-minute interview, eight-minute tutorial, doesn't matter. Done in under two minutes.

And the punchline: it costs about a dollar per video. Sometimes free. I'll show you the math later.


================================================================
BEAT 3  —  LIVE DEMO  (ALREADY SHOT — SKIP)
================================================================

Skip. Already shot in 3 takes. Edited in post per the cut & shoot guide.


================================================================
BEAT 4  —  SETUP  (with the SABR caveat)
ORDER 3 of 9   |   ~110 sec   |   the longest beat — get it in while warm
================================================================

Now let me get you set up. The original demo makes the install look easy. Five minutes, two commands, done. And it is — most of the time.

But here's what no other reaction video is going to tell you. The day I installed this skill, YouTube was actively fighting yt-dlp on every download. Four-oh-three errors. Blocked fragments. The whole mess. The original demo doesn't show that part. So I'm showing you both — the clean path, and the messy one I had to actually live through.

Easy path first. In Claude Code, run these two commands.

Slash plugin marketplace add brad-automates slash claude-video.
Slash plugin install watch at claude-video.

Restart Claude Code. You're done. Point slash-watch at any video. The skill auto-installs FFmpeg and yt-dlp the first time it runs on macOS. On Linux or Windows, it tells you the exact install command for your system. Then grab a free Groq API key from console dot groq dot com — that handles the videos that don't have captions. That's the whole install.

Messy path — when YouTube actually blocks the download. You'll need four things. Python three-eleven or higher, because the older Python that ships with macOS doesn't run the latest yt-dlp. The latest yt-dlp itself, installed through u-v. Deno, because the new YouTube SABR streaming protocol needs a JavaScript runtime to solve a challenge. And browser cookies, because YouTube wants to verify you're a real person.

I'll drop the exact copy-paste install in the description. Five commands, fifteen minutes, fixes everything. Save this video. You'll need it the day YouTube decides to fight you.


================================================================
BEAT 5  —  UNDER THE HOOD
ORDER 4 of 9   |   ~25 sec   |   short
================================================================

How does this actually work? Two old, free, open-source tools doing the heavy lifting. yt-dlp downloads the video. FFmpeg slices it into frames and pulls the audio. If the source has captions — most YouTube videos do — you get the transcript free. If not, Whisper on Groq transcribes the audio for almost nothing. Claude reads the frames like a flipbook and the transcript like a script, and the timestamps line up.

No new model. No expensive API. Just the right glue.


================================================================
BEAT 6  —  COST MATH  (the real numbers)
ORDER 5 of 9   |   ~50 sec
================================================================

And the most beautiful part of all of this — it's almost completely free.

Assume you already pay for Claude. Twenty bucks a month for Pro, which is what I'm on. Even if you don't, the graph I'm about to show you is going to convince you.

My Anthropic dashboard for this month: zero. Zero dollars. Because slash-watch runs inside the Claude Code subscription you're already paying for. There's no extra API bill on top.

The only thing that costs anything is transcription, and only when the video has no captions. I've run this on three videos so far. Two had captions: free. One didn't: two cents on Groq. Not two dollars. Two cents.

Unless you're feeding it an endless stack of documentaries with no subtitles, the free tier covers you. Most weeks this whole pipeline costs me less than a coffee.


================================================================
BEAT 7  —  USE CASE 1  (Trend Scout × /watch)
ORDER 6 of 9   |   ~60 sec
================================================================

Here's where it gets interesting for me. This is the part no other tutorial about this skill is going to show you.

I already run a system I call Trend Scout. The day I'm hunting for a new video, I fire it. It scans twenty-four AI YouTubers, ranks the ones that broke at least double their channel's average views, and tells me which one is worth my attention right now.

Until now I'd have to actually sit down and watch the winner. Twenty, thirty minutes per video. Now I don't. Trend Scout picks the video. Slash-watch ingests it. Claude gives me back a structured breakdown — what's the hook, what's the visual setup, where's the surprise, what's the punchline.

Twenty minutes of work compressed into two minutes.

This is the part I want creators to copy. You don't need a forty-person research team. You need a tiny scanner and a skill that watches the videos for you.


================================================================
BEAT 8  —  USE CASE 2  (skip the cron-job theater)
ORDER 7 of 9   |   ~70 sec   |   needs conviction — do it while energy's up
================================================================

Here's where I'm going to disagree with almost every other creator running a stack like this.

A lot of people are stockpiling. Obsidian vaults full of competitor breakdowns. Cron jobs scraping every channel they care about every six hours. Daily digests. Weekly intelligence reports. "Compounding library" this, "second brain" that.

I think most of it is waste.

In AI, a video about a tool from three days ago is already half-stale. A breakdown of last month's hot launch? Dead weight. The cron jobs and routines creators set up to "compound their intelligence" — by the time you actually need any of it, the answer has changed.

So I don't compound. I run slash-watch and Trend Scout the moment I'm hunting for a video. Not before. Not on a schedule. The day I sit down to ship something, I do the scan fresh, I slash-watch the top three, I pull what's true right now, and then I move.

The leverage isn't in the library. The leverage is in the skill being fast enough that you don't need a library.


================================================================
BEAT 8.5  —  WHY THIS IS A BREAKPOINT  (zoom-out)
ORDER 8 of 9   |   ~85 sec   |   OPTIONAL
================================================================

OPTIONAL — Skip this whole beat if you're going with the live-take splice from
2026-05-04 19-32-59.mov (the flywheel + executive-producer quotes). That is the
recommended path per the take-2 review. Read this only if you want a polished
re-take instead.

Step back for a second. There are two big parts left in AI content right now.

First one: scripting and filming. You can't fully delegate this — and honestly you shouldn't want to. You have your own voice. You like a certain way of saying things. AI would need a mountain of your existing content to mimic that exactly, and even then you'd want to fix it. So filming, the human side, that's not going anywhere.

Second one: editing. Taste lives there. You're choosing between takes. You're deciding the structure. Motion graphics, b-roll, captions popping out — every AI editing tool I've tried still needs a human sitting on top of it. That part isn't solved.

But this — slash-watch — is one of the breakpoints. Claude Code can now make Claude Code actually watch videos. Not just read transcripts, not just listen — watch. You just gave your senior editor or your producer the ability to see, when before they could only read or hear.

It doesn't write the script for you word-for-word. But it eats almost all the research time. Where are the trends going? How are the best videos structured? What's working this week? That pattern recognition — Claude can now do it for you. So the scripting half just got solved. Or at minimum, we're in the middle of solving it.


================================================================
BEAT 9  —  OUTRO  (with shoutout + cross-promo)
ORDER 9 of 9   |   ~45 sec   |   easy closer
================================================================

That's the playbook. The skill is free, the repo is in the description, and my install patch for when YouTube decides to fight you is right under it.

One last thing. I would not be running this video today if it weren't for Brad Bonanno — he built and gave away this slash-watch skill for free, and his original walkthrough is what got me to install it in the first place. Big shoutout. His video is linked first in the description. Go subscribe to him too.

If you build the Trend Scout side — the recurring scanner that feeds slash-watch — show me. I'll run yours through slash-watch and put the breakdown in next week's video.

And before you go — if you want to see how I pull thirty grand doing marketing for small brands and companies, or how I'm building more cinematic websites with Claude Code and Claude design, that video is right here. Hit it.

Subscribe if you want the next operator playbook. See you in the next one.


================================================================
END OF TELEPROMPTER
================================================================
