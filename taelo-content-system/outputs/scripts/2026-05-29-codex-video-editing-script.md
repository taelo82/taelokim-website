# Script — "I Edit Every YouTube Video With a Terminal Command (Codex CLI)"

**Date:** 2026-05-29
**Format:** Operator tutorial / quick-hit. Screen-capture-first + light face-cam.
**Target length:** 8–10 min.
**Style ref:** Nate Herk (high-energy, straight-to-the-point, "let me show you exactly", honest caveats, recap takeaways) × Eric Michaud (practical, grounded, operator POV, "here's why this matters for you").
**Pillar:** AI tools / operator workflow. **Lane:** near-empty (every "AI video editing" video is Runway/Descript/CapCut — CLI-driven editing via a coding agent does not exist as a tutorial genre).
**Brand rules applied:** first-8s hard hook · satisfaction-beat ending (no filler outro) · solo-editor (all cues addressed to Taelo) · creator shoutouts in outro only · clean native English for VO, keep rough energy on face-cam takes.

---

## Working titles (pick at thumbnail stage — Test & Compare 3)
1. **I Edit Every YouTube Video With ONE Terminal Command (Codex CLI)**
2. **I Stopped Using Premiere. Now I Edit Videos With Codex.**
3. **This Coding Tool Edits My Videos Faster Than CapCut (Codex + FFmpeg)**

**SEO targets:** "codex video editing", "edit video with ai cli", "claude code video editing", "openai codex ffmpeg", "ai video editor workflow 2026", "automate video editing with ai", "best ai video editor for creators 2026".

## Thumbnails (3 for Test & Compare)
- (a) Split screen: Premiere timeline (red X) vs a terminal window (green check). Overlay: **"NO PREMIERE."**
- (b) Face-cam, skeptical-to-grinning, terminal behind. Overlay: **"40 MIN → 9 MIN. ONE COMMAND."**
- (c) Big text **"I EDIT IN THE TERMINAL"** + small Codex + FFmpeg logos.

---

# THE SCRIPT

> VO = clean voiceover (polished English). FACE = to-camera, keep the rough energy. [SCREEN] = screen recording. [B-ROLL] = overlay. **Taelo:** = note to you, the editor/operator, not spoken.

---

## BEAT 1 — HOOK (0:00–0:12) — hard, first 8 seconds

**FACE (fast, no intro):**
"I just recorded 41 minutes of me rambling at this camera. In about 9 minutes, this gets cut down, captioned, and B-rolled into the video you're watching right now — and I didn't open Premiere, CapCut, or DaVinci once."

[SCREEN: a terminal. Taelo types/pastes one command, hits enter. Cut to the progress bars flying.]

**FACE:**
"I edit every video on this channel with a terminal command. Today I'm showing you the exact workflow — what it does, what it can't do, and how to set it up yourself. Let's go."

**Taelo:** No logo sting, no "hey guys welcome back." First frame is the 41:00 timeline. Hook ends by 0:12 max.

---

## BEAT 2 — THE PROBLEM / WHY YOU SHOULD CARE (0:12–1:10)

**VO:**
"Here's the thing about editing. The actual creative part — choosing the story, the order, the punchlines — that's the fun 20%. The other 80% is mechanical: cutting dead air, deleting the takes where I fumbled, syncing captions, dropping B-roll on the right words. That 80% is what eats your whole weekend."

[B-ROLL: clock spinning, a Premiere timeline being scrubbed back and forth, Taelo looking tired.]

**VO:**
"So I asked a simple question: that mechanical 80% — it's just file operations and pattern matching. Why am I doing it by hand with a mouse, when I have an AI agent that lives in my terminal and is really good at exactly that?"

**FACE:**
"That agent is Codex — OpenAI's command-line coding tool. And no, you don't need to be a programmer. I'll show you. By the end you'll get why coders quietly have the best video-editing setup right now and nobody's talking about it."

**Taelo:** This is the Eric-Michaud "here's why it matters to YOU" beat. Keep it 60s. Don't over-explain Codex yet.

---

## BEAT 3 — THE 30-SECOND MENTAL MODEL (1:10–2:00)

**VO:**
"One thing before the demo, so this isn't magic. Codex doesn't 'understand video.' It orchestrates three free, open-source tools that do the actual work:"

[SCREEN: three cards animate in]
- **auto-editor** — detects silence and dead air, cuts it automatically.
- **Whisper** — turns my audio into a perfect transcript and captions. (FFmpeg 8.0 now has this built in.)
- **FFmpeg** — the engine that actually trims, stitches, and renders the video.

**VO:**
"Each of those is a tool a human would normally run one command at a time, reading the manual for each. What Codex does is chain them together, in order, off a single plain-English instruction — and fix the errors in between without me babysitting it."

**FACE:**
"That's the whole trick. Codex is the brain. These three are the hands. Now watch it work."

**Taelo:** Say the names on screen as text so the SEO + the comments pick them up. This is the "easy-to-understand explanation" beat the audience came for — keep it concrete, no jargon.

---

## BEAT 4 — THE DEMO, STEP BY STEP (2:00–6:00) — the meat

**Taelo:** Screen-record the real run on a real raw take. Talk over it. Show the actual prompt and the actual output. Don't fake it.

### Step 1 — Strip the silence automatically (2:00–2:50)
[SCREEN: Codex prompt typed in plain English:]
> "Take `raw-take.mp4`, cut all silences and pauses longer than 0.4s with auto-editor, keep a little margin so it doesn't sound choppy, save as `cut1.mp4`."

[SCREEN: Codex writes + runs the auto-editor command, progress bar.]

**VO:**
"First pass: dead air. I talk slow, I pause, I think out loud. auto-editor rips every gap out. Watch the runtime — 41 minutes drops to about 24. That's a third of the video gone, and I didn't touch a single clip."

[B-ROLL: timeline before/after, the gaps visibly collapsing.]

### Step 2 — Transcribe + find the bad takes (2:50–4:00)
[SCREEN: prompt:]
> "Transcribe `cut1.mp4` with Whisper. I do retakes — when I say the same line twice, keep the last clean one and cut the earlier attempts. Give me the cut list before you apply it."

**VO:**
"This is the part that actually saves my weekend. Codex reads the full transcript, finds every spot where I flubbed a line and said it again, and proposes cuts. And notice — it shows me the list first. I'm still the director. I skim it, I veto two cuts I want to keep, it applies the rest."

[SCREEN: the cut list — timestamps + the duplicated lines. Taelo types "remove cut #3 and #7, apply the rest."]

**FACE (honest caveat — Nate Herk move):**
"Real talk: it's not perfect. Maybe one in ten cuts I override. But reviewing a list takes two minutes. Scrubbing for those moments by hand takes an hour. That's the trade."

### Step 3 — Captions (4:00–4:40)
[SCREEN: prompt:]
> "Burn word-level captions from the transcript, my channel style — bottom third, bold, highlight the active word."

**VO:**
"The transcript already exists from step two, so captions are basically free. Whisper's accurate enough that I fix maybe one word a video. The captions that are on this sentence right now? Made here."

[B-ROLL: the captions appearing on the actual footage.]

### Step 4 — B-roll on the right words (4:40–5:30)
[SCREEN: prompt:]
> "I have a `broll/` folder, filenames describe each clip. Read my transcript, and wherever I mention something I have B-roll for, overlay it for 2–3 seconds at that timestamp."

**VO:**
"This one feels like cheating. Codex matches what I'm *saying* to my B-roll filenames and drops the clip in at the exact word. I say 'terminal,' a terminal clip appears. I say 'Premiere,' the Premiere shot appears. It's pattern matching — which is the one thing these models are unbelievable at."

**Taelo:** Name your B-roll files in plain English (`terminal-typing.mp4`, `premiere-timeline.mp4`) — the whole match depends on it. Show your folder on screen so people copy the habit.

### Step 5 — Render, and the "one command" reveal (5:30–6:00)
**VO:**
"Now — I showed you those as five separate steps so you'd understand what's happening. But once it works, you save the whole chain as one instruction. So my actual edit is this:"

[SCREEN: a single command / a saved Codex prompt. Enter. Everything runs end to end.]

**FACE:**
"That's it. That's the edit. Raw take in, finished cut out, while I go make coffee."

---

## BEAT 5 — CODEX vs CLAUDE CODE (the comparison the audience wants) (6:00–7:00)

**VO:**
"Quick one, because I know the comment's coming: 'can Claude Code do this too?' Yes. It's the same idea — agent in the terminal driving FFmpeg. I've run both."

[SCREEN: side-by-side, two terminals.]

**VO:**
- "**Codex** wins on the long, chained renders — it just grinds through a 12-step FFmpeg job and recovers from errors without stopping to ask me. Goal mode lets it run for an hour unattended."
- "**Claude Code** wins on the *setup* — when I'm building the workflow the first time and need it explained, the skills and the plugin ecosystem are ahead. I built my first version of this in Claude Code."

**FACE:**
"So: build it in Claude Code, run it in Codex. Or just pick whichever you already pay for — the workflow is the same. Don't let the tool war stop you from trying it."

**Taelo:** This beat is doing double SEO duty — "codex video editing" AND "claude code video editing" both rank. Worth the 60 seconds.

---

## BEAT 6 — WHAT IT CAN'T DO (honesty beat — builds trust) (7:00–7:45)

**FACE:**
"Let me save you the disappointment, because every AI video on YouTube skips this part."

**VO:**
- "It won't find your story. You still decide what the video *is*. The agent cuts; it doesn't direct."
- "Music, color, and the emotional pacing of a punchline — still me, by hand. For now."
- "And the first setup is an afternoon. Installing the tools, getting one clean run. After that it's minutes per video — but day one is real work."

**FACE:**
"If you want zero-effort one-click magic, this isn't it. If you want to delete the boring 80% forever, it absolutely is."

---

## BEAT 7 — TAKEAWAYS (Nate Herk recap) (7:45–8:30)

**FACE:**
"So, three takeaways before you go build this."

[SCREEN: three text cards]
1. **"The boring 80% of editing is just file operations — and agents are great at file operations."** That's the whole insight. Stop doing it by hand.
2. **"You stay the director."** The agent proposes, you approve. Always make it show the cut list first.
3. **"Name everything in plain English."** Your B-roll, your folders, your files. The transcript-to-clip matching lives or dies on good filenames.

---

## BEAT 8 — SETUP / RESOURCE CTA (8:30–9:00)

**FACE:**
"I wrote up the exact commands, the install steps for all three tools, and the prompt I use — it's a free page, link in the description. Steal the whole thing."

**VO:**
"If you want me to go deeper — full long-form build where we set this up from an empty terminal — tell me in the comments and hit the like button so I know to make it."

**Taelo:** Companion blog = the GEO play. "How do I edit video with an LLM" has near-zero good answers in ChatGPT/Claude/Perplexity right now — this page can own it. Publish with the video. Add `llms.txt` + Bing submit.

---

## BEAT 9 — SATISFACTION-BEAT CLOSE + SHOUTOUT (9:00–9:15)

**FACE:**
"That's the workflow. If you came here wondering whether you can really edit video from a terminal — now you know exactly how, and exactly what it costs you. That was the goal."

**VO (shoutout — outro only, per brand rule):**
"Tools shown: Codex, Whisper, auto-editor by WyattBlue, and FFmpeg — all free, all open source. Go build it."

[END on the finished video frame. No long outro, no end-card filler. Cut.]

---

## YouTube description block (draft)

> I edit every video on this channel with a terminal command instead of Premiere or CapCut. In this video I show the exact workflow: how Codex (OpenAI's CLI coding agent) chains auto-editor, Whisper, and FFmpeg to cut silence, remove bad takes, caption, and drop B-roll — from one plain-English instruction.
>
> 🔗 Full setup + commands (free): [taelokim.com link]
>
> Tools: Codex · Whisper · auto-editor (github.com/WyattBlue/auto-editor) · FFmpeg 8.0 (built-in Whisper filter)
>
> Chapters:
> 0:00 41 minutes → 9 minutes, one command
> 0:12 Why the boring 80% of editing is automatable
> 1:10 The 30-second mental model (Codex = brain, 3 tools = hands)
> 2:00 Live demo: silence → transcript → bad takes → captions → B-roll → render
> 6:00 Codex vs Claude Code for editing
> 7:00 What it can't do (the honest part)
> 7:45 3 takeaways
>
> #codex #aivideoediting #ffmpeg #claudecode #contentcreation

---

## Production notes (Taelo)
- **Equipment:** one camera + screen capture. No film day. This is the fast-content pick — ship in ~4–5 hours including the live demo recording.
- **The demo must be real.** Record an actual raw take (even this script's intro), run the actual chain on screen. The credibility — and the comment-section defensibility — is that you genuinely edit this way.
- **Repurposing engine:** the 5-step demo = 5 vertical Shorts (one per step, "I caption videos with one command" etc.) + 1 LinkedIn clip (Beat 5 comparison) + the companion blog + an X thread of the prompts. ~8 assets from this one shoot.
- **Apply:** first-8s hook ✓, satisfaction-beat ending ✓, Hype CTA ✓, 3-thumbnail Test & Compare ✓, Ask-YouTube description block ✓, GEO companion blog + `llms.txt`/Bing ✓.
