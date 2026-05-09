# 1st draft → 2nd draft trim guide

> Premiere-ready punch list. Open `1st draft for slash watch.mp4` (13:17), scrub to each timecode below, apply the cut. All timecodes are from the **1st draft timeline**, not the original face-cam takes.
>
> Outcome: trims 1:47 of VO. Lands the 2nd draft at **~11:30**. No new shoots required for this pass.

Source video: `taelo-content-system/1st draft video/1st draft for slash watch.mp4`
Plan reference: `~/.claude/plans/let-s-resume-our-watch-majestic-reddy.md`

---

## Cut 1 — Beat 3 demo: tighten the VO meander (saves ~38s)

The OBS footage is fine. Three VO meanders to drop without removing any visual.

| In | Out | Drop this VO | Why |
|---|---|---|---|
| **01:25** | **01:46** | "he is a legit CEO of one of the biggest… his stack will be less relevant to a lot of users… I was still curious but I didn't want to watch the whole thing" | Spectator critique of Gary Tan. Viewer wants to see `/watch` work, not a take on the source. |
| **02:08** | **02:24** | "this saved me tons of time because whatever he's demonstrating here is a little bit irrelevant unless you're CEO… he's not doing side hustle building… he's not trying to build cool project… maybe he is but like there's a lot of eyeballs on him" | Same critique extended. Tangential. |
| **02:46** | **03:10** | "we promised to ourselves hey let's spend like a minute actually listening to him all the sudden five to ten minutes gone by… that happens all the time in YouTube especially AI content where contents are long and comprehensive…" | This is the Beat 1 pain story sneaking in late. Beat 1 already established it. |

**Keep intact:** the magic-moment arc. "I just typed Claude Code… g-stack… 21 minutes long… two minutes, how are you doing this in less than two minutes… it gave me this in less than two minutes."

---

## Cut 2 — Collapse the stranded Beat 1 reprise + tighten Beat 2 (saves ~45s)

After the demo lands at ~03:24, the cut goes back to "having a transcript and guessing from a still frame is vastly different…" — that's Beat 1B leaking in late. Then a "limitless pill / even this recording / flywheel" passage at 04:25 says "Claude can now watch" for the third time.

### 2a — Collapse 03:24–04:25 reprise into a 15-second bridge

| In | Out | Action |
|---|---|---|
| **03:24** | **04:25** | Razor + ripple-delete this whole 1:01 stretch, then drop a single ~15s VO line back in (record fresh face-cam if no take has it cleanly): |

> *"And here's the kicker — having a transcript and guessing from a still frame is nothing like actually watching. The full context only shows up when Claude can see what's on screen."*

Drop entirely: the screenshot-frame-by-frame story (Beat 1's pain setup already implied it), the "real person, producer of your content can only hear" analogy, the "every creator, every builder, every learner" elevation.

### 2b — Tighten Beat 2 (limitless pill / flywheel)

| In | Out | Drop this VO | Why |
|---|---|---|---|
| **05:13** | **05:35** | "It's like giving a limitless pill to Claude Code because I can just give Claude a file path. Even this recording, I'm going to say here's the location and it just watches it… upward flywheel is possible because Claude Code can now literally watch any video, any location." | Cute meta-callback but it's the third "Claude can now watch" in 30 seconds. Save the recursive recording moment for Beat 9 instead, where it lands harder. |

Keep: "There's a free Claude skill called slash watch. You give it any video link… frames and transcript together. Not reading the captions and pretending. Watching." That's all Beat 2 needs.

---

## Cut 3 — Trim Beat 8 to its kernel (saves ~50s)

Beat 8 currently runs 09:30–11:15 (1:45). Trim to ~50s by dropping the examples-list and the agent-fooled-by-views tangent. Beat 8.5 stays full.

| In | Out | Drop this VO | Why |
|---|---|---|---|
| **09:55** | **10:50** | "It's cool but it's kind of wasting your energy… The breakdown of last month hot launch is not really useful… these agents don't know what's relevant after a few days… for example if some video goes viral and has 1 million, 2 million views, but we know after a few days as a human that it's irrelevant, but these agents, they might be searching and if there's high views, it can still give you false insight that it's still trending…" | Two stacked tangents. The agent-fooled-by-views point is interesting but kills the pace right before the punchline. |

Keep the kernel: "people are stockpiling… second brain is hype… in AI a video about a tool from three days ago is already half stale… run `/watch` the moment I'm hunting, not before, not on a schedule… the leverage isn't in the library, the leverage is the skill being fast enough that you don't need a library."

---

## Cut 4 — Optional micro-trim on Beat 4 install (saves ~12s)

The read-aloud of the install commands at **05:24–05:36** is unintelligible as audio (slash-command syntax doesn't parse spoken). Two options:

- **Best:** keep the VO ducked under, lay the typed-live OBS A3 capture (when shot) over top, let the visual carry it.
- **Quickest now:** trim the spoken command read by ~12s — viewers will get the commands from the description and the on-screen text once A3 is laid in.

Skip this cut on the first VO-only pass; revisit when A3 OBS capture exists.

---

## Final runtime check

| Beat | Before | After |
|---|---|---|
| Beat 1A (00:00–01:11) | 1:11 | 1:11 |
| Beat 3 demo (01:11–03:24) | 2:13 | ~1:35 |
| Beat 1B reprise + Beat 2 (03:24–04:55) | 1:31 | ~0:45 |
| Beat 4 install (04:55–07:27) | 2:32 | 2:20 |
| Beat 5 (07:27–07:55) | 0:28 | 0:28 |
| Beat 6 cost (07:55–08:50) | 0:55 | 0:55 |
| Beat 7 Trend Scout (08:50–09:30) | 0:40 | 0:40 |
| Beat 8 (09:30–11:15) | 1:45 | ~0:55 |
| Beat 8.5 (11:15–12:40) | 1:25 | 1:25 |
| Beat 9 outro (12:40–13:16) | 0:36 | 0:36 |
| **Total** | **13:17** | **~11:30** |

---

## What to do after this trim pass

1. Re-export as `2nd draft for slash watch.mp4` into the same folder.
2. Run `/watch` on the 2nd draft. Ask: *"What are the 3–4 key takeaways?"* They should match the Beat 1 promise (how it works / how to set up / what to do with it). If the summary still feels meandering, there's a stranded passage left — flag the timestamp.
3. Then move to Step 2 of the plan: build X1 (Beat 5 pipeline diagram), X2 (Beat 8.5 whiteboard), X5 (Beat 8 split-screen).
4. Then run OBS Sessions A–D per [obs-shoot-list.md](2026-05-05-watch-obs-shoot-list.md), Priority 1 → 2 → 3.
