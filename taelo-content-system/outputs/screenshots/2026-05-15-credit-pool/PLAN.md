# B-Roll & Visual Asset Plan — Anthropic Same-Day Switch Video

_Generated 2026-05-17. Master face-cam at `~/Downloads/Anthropic's Secret Cloud Cut_ The Truth Revealed!.mp4`. Script at `../trends/2026-05-15-teleprompter.md`. Existing cream HTML graphics at `../graphics/2026-05-15-credit-pool/`._

## 1. Diagnosis

13 cream-paper HTML graphics already cover abstract data beats. They're doing their job. But cream is also carrying receipt beats (tweets, help center, console UI, news pages, timeline) where the actual artifact exists — that's where "generic" creeps in.

Rule going forward: **real artifact > cream rendition of the artifact**. Cream is for things that don't exist (math, taxonomy, framing). Real is for things that do.

## 2. Folder convention

```
outputs/screenshots/2026-05-15-credit-pool/
  tweets/        # static tweet/community-note PNGs
  ui/            # console, help center, code.claude.com captures
  news/          # headline screenshots, article hero crops
  timeline/      # April 4 / April 21 / May 13 source captures
  recordings/    # screen recordings (terminal, scroll-throughs)
  raw/           # untrimmed source before crop
```

Naming: `NN-beat-source.png` (e.g. `04-lydia-tweet.png`).

## 3. Beat-by-beat shot list

| Beat | Time | Current | Action | Source |
|---|---|---|---|---|
| Cold open | 0:00–0:30 | `01-cold-open-split-screen` + `02-forty-x-stamp` | **Keep both** — abstract framing | existing |
| Why you care | 0:35–0:50 | `03-why-you-care-tools` | **Keep**, shorten | existing |
| PR/agent stretch | 0:50–1:30 | bare face-cam | **ADD**: terminal screen recording of `claude -p` running + a GitHub PR with a Claude review comment | new recording (§4-A) |
| $5K→$200 | 1:30–2:00 | `04-5k-to-200-drop` | **Keep** — pure data viz | existing |
| Theo / Pocock weasel | 1:30–2:00 | `11-pocock-tweet` (cream) | **REPLACE**: real Pocock tweet (your conversation screenshot) + Theo's actual cancellation tweet | conversation screenshot + URL needed |
| Announcement one | 2:30–3:00 | `13-june15-banner` | **REPLACE primary**: Anthropic news page screenshot + headlines collage (9to5Google / Business Standard / AndroidHeadlines / Pulse2). Cream banner becomes 2-sec sting | new captures (§4-B) |
| Help-center receipt | ~3:00 | `12-covered-vs-not` | **REPLACE primary**: real support.claude.com/15036540 scrolled to "claim a dedicated monthly credit" line. Cream `12` becomes wrap-up cut | screen recording |
| Spectrum | 3:00–3:30 | `10-spectrum-grid` | **Keep** — abstract taxonomy | existing |
| Math beat | 3:00–3:30 | bare face-cam | **ADD**: whiteboard sketch (your conversation screenshot 2) intercut at 25×/40×/175× line | conversation screenshot |
| Extra Usage toggle | 3:30–3:50 | `05-extra-usage-toggle` (cream) | **REPLACE**: real console Usage page + real Extra Usage toggle screenshot | new capture (§4-C) |
| ClaudeDevs framing | 4:00 | bare | **ADD**: real ClaudeDevs tweet screenshot | URL needed |
| Lydia + Community Note | 4:00–4:30 | `06-community-note` (unrendered) + `06-lydia-diagram-annotated` (cream) | **REPLACE primary**: real Lydia tweet with Community Note. Cream diagram becomes 3-sec callout for technical detail | URL needed |
| Channels split | 4:30–4:50 | bare face-cam | **ADD**: side-by-side of @AnthropicAI header vs @ClaudeDevs header | new capture |
| 5 personas | 4:50–6:10 | `07-five-personas` | **Keep** — abstract taxonomy | existing |
| 3 moves | 6:10–7:40 | `08-three-moves` | **Keep abstract**, **ADD inside Move 1**: real console → Usage screen recording showing bookmark moment | new recording (§4-C) |
| Zoom-out timeline | 7:40–8:30 | bare face-cam | **ADD: timeline strip** — April 4 ban / April 21 walkback / May 13 split with real source headlines | new asset (§4-D) |
| My take | 8:30–9:10 | bare face-cam | Leave on face-cam — earned monologue | — |
| Friday reset | 9:10–10:30 | `09-friday-reset` | **Keep as anchor**, **ADD**: real Noah Zweben replies + real Axios headline intercut twice | URLs needed |

## 4. New visual treatments

**A. Terminal screen recording (0:50–1:30 stretch).** iTerm full-screen, dark + JetBrains Mono. Capture: `claude -p "review this PR"` running, output streaming, then cmd-tab to a real GitHub PR with a Claude bot comment. ~20s raw → edit to 8–10s. Capture: macOS `Cmd+Shift+5`. Time: 15 min.

**B. Headlines collage (announcement-one beat).** Four browser tabs, each cropped to headline + outlet logo, animated as a stack-drop with the red underline from cream style. Outlets: 9to5Google, Business Standard, AndroidHeadlines, Pulse2. Capture: Chrome MCP. Time: 20 min.

**C. UI screen recording (Extra Usage + Move 1).** Single ~30s recording — log in to console.anthropic.com, click Usage, hover Extra Usage toggle (off state), zoom into the toggle. Cut into two clips. Capture: QuickTime (your signed-in session, not MCP). Time: 10 min.

**D. Timeline strip (zoom-out beat).** Horizontal scroll: April 4 / April 21 / May 13, each card a real news headline screenshot. Build in HTML in `outputs/graphics/` for determinism, or layer in NLE. Time: 30 min HTML, 15 min NLE.

## 5. Capture workflow

| Asset class | Tool | Why |
|---|---|---|
| Public tweets (Lydia, ClaudeDevs, Theo, Pocock, Noah Zweben) | Chrome MCP | DOM-aware, can grab Community Note expanded |
| Anthropic news, headlines, Axios | Chrome MCP | same |
| support.claude.com/15036540 | Chrome MCP recording → ffmpeg trim | needs scroll motion |
| console.anthropic.com Usage + Extra Usage toggle | **You, QuickTime, signed-in session** | MCP shouldn't touch billing console |
| code.claude.com Agent SDK page | Chrome MCP | public |
| Terminal `claude -p` demo | **You, QuickTime + iTerm** | needs your env |
| Pocock + whiteboard (already shared) | save from chat to `tweets/` and `raw/` | — |

## 6. URLs needed from Taelo

1. Lydia Hallie tweet URL (Community Noted)
2. ClaudeDevs tweet URL (Agent SDK credit announcement)
3. Theo Browne cancellation tweet URL (or T3 video timestamp if it's in video)
4. Anthropic news page URL — May 13 "Higher usage limits for Claude"
5. Axios article URL — "Anthropic tightens Claude limits as OpenAI courts agent users"
6. Noah Zweben reply thread URL (gaslighting replies)
7. Confirm support article ID = 15036540 + code.claude.com path

## 7. Sequenced work order

**Phase 1 — today, cheap wins (~90 min):**
1. ✅ Create `outputs/screenshots/2026-05-15-credit-pool/` tree
2. ⏳ Save the 2 conversation screenshots (Pocock + whiteboard) into `tweets/` and `raw/`
3. ⏳ Capture all public tweets + news pages via Chrome MCP (needs URLs from §6)
4. ⏳ Capture support.claude.com article scroll
5. ⏳ Capture code.claude.com Agent SDK page

**Phase 2 — needs Taelo at the keyboard (~60 min):**
6. Taelo records console.anthropic.com Usage + Extra Usage toggle (QuickTime, ~30s)
7. Taelo records `claude -p` terminal demo (~20s)
8. Build timeline strip (Treatment D) once three source URLs for April 4 / April 21 / May 13 confirmed

**Phase 3 — in the NLE:**
9. Swap real artifacts in for cream renditions per §3
10. Demote cream 06, 11, 12, 05, partially 13 to ≤2-sec stings or cut entirely
11. Drop four new B-roll inserts at 0:50, math beat, channel-split, zoom-out timeline

## 8. Fair use

Tweets, headlines, support docs, console UI — editorial commentary, transformative, short duration. Standard creator fair-use posture. **Theo's video** is the careful one: if clipping his actual T3 video frames, ≤7 sec, on-screen credit, link in description. Safer path — screenshot his cancellation tweet, not the video. Pocock and Lydia: static screenshots with handles visible. Axios: headline + dek only, not body.

## 9. Permissions

- Chrome MCP for all public-web captures
- ffmpeg for trim/crop into `screenshots/`
- Auto-push the new screenshots folder after batch (per standing rule)
