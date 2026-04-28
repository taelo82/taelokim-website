# Claude Design Entry Kit — taelokim.com
## Date: 2026-04-26

> Single document to paste into Claude Design at session start.
> Front-loads the 7 overrides + brand spec + assets so the first generation
> lands close to final, minimizing iteration burn on weekly quota.

---

## How to use this file

1. Open Claude Design → New Prototype → **Wireframe** first (saves tokens; convert to Hi-Fi after composition is locked)
2. Sketch the hero on the canvas (boxes labeled: hero video, hero text, spaceman, navbar, CTA)
3. Drag in: `hero-loop.mp4`, `spaceman.png` (transparent), `tokens.css` (as artifact)
4. Paste **the kickoff prompt** at the bottom of this file as your first message
5. Let it build, then iterate via Comment / Inline Edit / Tweaks Panel — do NOT rewrite full prompts

---

## SECTION 1 — Banned Defaults (Override 2)

Paste this near top of kickoff prompt. **Negatives are stronger than positives** for these models.

```
BANNED — do not use under any condition:

Typography:
- Inter, Roboto, Geist, Söhne (current SaaS sans-serifs)
- Default serif headlines paired with sans body

Components:
- Pills / pill-shaped buttons / pill-shaped nav
- Glassmorphism / frosted glass / blur backgrounds
- Container cards with rounded corners + subtle borders
- Blinking status dots / "live" indicators

Color:
- Purple-to-blue gradients
- Pink-to-purple gradients
- Cool blue accents
- Multi-color rainbow gradients

Layout:
- Hero with centered title + 2 CTAs (left-right symmetric)
- Three-column "feature grid" with icons
- Logo cloud / "trusted by" strip near top
- Sticky cookie banners, sticky hover popovers

Copy:
- "AI-powered", "AI-native", "intelligent", "supercharge"
- "Built for teams", "designed for modern teams"
- "Reimagining workflows"
- "Get started in seconds"
- "No credit card required"

Motion:
- More than ONE primary signature interaction per page
- Hover-tilt on every card
- Parallax on every section
```

---

## SECTION 2 — Reference Dictionary (Override 3)

```
TASTE COORDINATES (match this taste, not exact copy):

- Composition / spacing rhythm: Linear (linear.app, 2023 redesign)
- Section pacing: Apple product pages (long-scroll cinema)
- Color discipline: Vercel — neutral 95% / one warm accent
- Typography pairing: serif display + neo-grotesque body, not the inverse
- Density: tight, deliberate, no wide hero whitespace fluff
- Microcopy tone: Arc Browser — playful but precise
- Hero treatment: Anthropic.com homepage (cinematic + minimal text)
- Footer style: Stripe — quiet, confident, under-designed
```

---

## SECTION 3 — Design Tokens (Override 5)

Paste as separate `tokens.css` artifact in Claude Design.

```css
:root {
  /* PALETTE — 5 colors max */
  --void:    #050510;        /* hero background, page bg */
  --paper:   #E8E4DC;        /* primary text on void */
  --thread:  #FFB347;        /* signature warm amber, the light */
  --dust:    #6B5B4F;        /* secondary text, muted UI */
  --signal:  #00C2FF;        /* used ONCE — the email CTA only */

  /* TYPOGRAPHY — display serif + neo-grotesque body */
  --font-display: "Migra", "GT Sectra", Georgia, serif;
  --font-body:    "Inter Tight", "Söhne", system-ui, sans-serif;
  --font-mono:    "JetBrains Mono", "Berkeley Mono", monospace;

  /* TYPE SCALE */
  --type-hero:     clamp(64px, 9vw, 120px);
  --type-h1:       clamp(40px, 5vw, 64px);
  --type-h2:       clamp(28px, 3vw, 40px);
  --type-body:     17px;
  --type-small:    14px;
  --type-mono:     13px;

  /* SPACING — 4px base */
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  16px;
  --space-4:  24px;
  --space-5:  40px;
  --space-6:  64px;
  --space-7:  96px;
  --space-8:  160px;

  /* RADIUS — almost none */
  --radius-sm:  2px;
  --radius-md:  4px;
  --radius-lg:  8px;
  /* NO pill / fully-rounded by default */

  /* MOTION */
  --ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-slow: 1200ms;
  --duration-med:  600ms;
}
```

**Rules for Claude:** Reject any color, type, or spacing value not in this file.
Do not introduce hover-glow, neon, or animated gradients.
The only color that is allowed to draw the eye is `--thread` (#FFB347) and `--signal` used exactly once.

---

## SECTION 4 — Voice Spec (Override 7)

```
VOICE INSTRUCTIONS for all copy:

The site speaks as Taelo Kim — a builder/operator based in Korea.
Reviewed 150+ startup pitches as a VC. Shipped real products in
e-commerce (FBA), K-beauty marketing, K-hair, K-supplements
across Korea and Southeast Asia. Currently building in public
on AI tools.

Tone:
- Direct. Says what others dance around.
- Skeptical of hype. Backs claims with numbers.
- Conversational, like talking to a smart friend at a coffee shop.
- Korean phrases when more precise than English (sparingly).

Yes:
- "Here's what actually happened"
- "I tested this so you don't have to"
- "The real numbers"
- "No BS"
- Concrete numbers, dates, dollar amounts

No:
- "AI-powered", "leverage", "synergy", "ecosystem"
- "Side hustle", "passive income", "game-changer"
- "Smash that like button", "in today's video"
- Generic startup-speak from US/SF SaaS
- Fake urgency: "You NEED this NOW"

When in doubt, write less. A 4-word headline beats an 11-word one.
```

---

## SECTION 5 — Site Spec (IA + sections)

```
SITE: taelokim.com

PURPOSE:
Personal hub for Taelo Kim — operator/builder content + free resources
for Global AI builders. The site is BOTH a portfolio and a
lead magnet (free prompt packs, frameworks, build logs).

TARGET VISITOR:
Builder/operator landing here from a YouTube video about AI tools or
Claude Design. They want: the resources mentioned in the video,
proof that Taelo is the real deal, and a way to follow more.

PAGE STRUCTURE (single-page, scroll-driven):

1. HERO
   - Looping video background (hero-loop.mp4, single warm light shaft, dust)
   - Spaceman PNG layered (transparent, positioned center-right ~60% scale)
   - Hero text LEFT side (void area)
   - Headline: short, declarative. Operator-voice. e.g.
     "I build with AI in Seoul. Here's what's working."
     (or Taelo's preferred wording — Claude, draft 3 options)
   - Sub: one sentence, max 14 words
   - One primary CTA (text link, no button-pill): "See the resources →"
   - Pill nav at top: HOME · BUILDS · RESOURCES · WRITING · CONTACT

2. INTRO STRIP
   - Quiet, 1-paragraph "who is Taelo" beneath hero
   - Three small stats (real numbers — placeholder for now: pitches reviewed,
     products shipped, something Korea/SEA specific)

3. RESOURCES
   - Featured: Claude Design overrides pack (free download — links to the
     7-overrides resource, the deliverable for the YouTube video CTA)
   - 2-3 other free resources in a tight grid (cards but NOT rounded —
     hard edges, no shadows, just typographic cards)

4. BUILDS
   - Current builds in public — what Taelo is shipping right now
   - Honest status (working / paused / shipped) per item
   - Real metrics where available
   - Linked out to deeper write-ups

5. WRITING / NOTES
   - 3-5 most recent essays or notes
   - Minimal — title + 1-line description + date
   - No featured image clutter

6. ABOUT (compressed)
   - One paragraph, third-person feel even though it's Taelo
   - VC + operator + Korea/SEA framing
   - Headshot OR no photo at all (decide live)

7. EMAIL CAPTURE
   - Single signal-color CTA (#00C2FF — the only place this color appears)
   - "Get new resources first." 6 words.
   - Email field + submit. No "we won't spam" disclaimer (treat reader as adult).

8. FOOTER
   - Quiet. Channel link, email, X handle. Year. That's it.

INTERACTION SIGNATURE:
The hero spaceman pulls luminous threads as the user scrolls.
Each thread, when fully extended, triggers the next section to slide in
from below with a cinematic cubic-bezier ease.
This is the ONLY signature interaction on the page.
All other transitions are clean opacity fades.
(Note for Claude Design: render the hero with spaceman + placeholder
threads as static SVG. The scroll-bound thread mechanic will be
implemented in Claude Code after export — not here.)
```

---

## SECTION 6 — Asset Inventory

Drag/drop all of these into Claude Design canvas before writing the kickoff prompt:

| Asset | File | Role |
|---|---|---|
| Hero background loop | `hero-loop.mp4` | Loops as hero `<video>` background |
| Spaceman | `spaceman.png` (transparent BG) | Layered over hero, center-right |
| Design tokens | `tokens.css` (this file's Section 3) | Paste as artifact |
| Site sketch | hand-drawn or Excalidraw | Pasted into canvas before kickoff |

---

## SECTION 7 — Kickoff Prompt (paste this as first message)

```
You are designing taelokim.com — a personal site for Taelo Kim, a builder/operator based in Seoul who reviewed 150+ pitches as a VC and ships products in AI / e-commerce / K-beauty across Korea and SEA.

This is NOT a generic SaaS landing page. It must feel cinematic, restrained, and clearly NOT AI-generated. Every default Claude Design reaches for must be aggressively overridden.

I am giving you the following artifacts:
1. tokens.css (use these tokens exclusively — reject any color, font, or spacing not in this file)
2. hero-loop.mp4 (loops as the hero <video> background)
3. spaceman.png (transparent — layer over hero video, positioned center-right, ~60% viewport height)
4. Sketch on the canvas (hero composition + section order)
5. The voice / banned / reference / site spec below

Build the FIRST PASS now — wireframe fidelity, focus on layout, type hierarchy, section rhythm. We will go to high-fidelity AFTER the structure is locked.

[PASTE Banned Defaults here — Section 1]

[PASTE Reference Dictionary here — Section 2]

[PASTE Voice Spec here — Section 4]

[PASTE Site Spec here — Section 5]

Critical guardrails (repeat these to yourself before each decision):
- ONE signature mechanic per page. The hero spaceman pulls threads. Everything else is clean fade. No scroll-jacking, no parallax sprinkled, no hover-tilt cards.
- Negatives override positives. If something feels "AI-default", reject it.
- Tight density. No wide whitespace fluff. No "breathing room" excuses for empty layouts.
- The hero text lives LEFT of the spaceman, in the dark void region of the video. Do not center the headline.

Begin with a brief plan (5 lines max), then start building wireframe-fidelity.
```

---

## After first generation lands

**If first pass is close to right (~70% there):**
- Iterate via Comment, Inline Edit, Tweaks Panel — NEVER rewrite the kickoff prompt
- One visual dimension per follow-up prompt (typography OR color OR layout, not all three)

**If first pass is way off:**
- Stop generation immediately (don't waste tokens letting it finish)
- Identify which override was ignored most heavily
- Re-prompt with ONLY that override re-emphasized
- Do NOT re-paste everything

**When wireframe is locked:**
- "Convert to high-fidelity. Maintain all current proportions, typography, and spacing. Apply the warm-amber + void palette per tokens.css."

**When ready to export:**
- Click Share → Download as ZIP
- Open in Claude Code
- Tell Claude Code: "Push to private GitHub repo named `taelokim-site`"
- The spaceman thread mechanic gets built here (NOT in Claude Design)

---

## Spaceman thread mechanic (post-export, in Claude Code)

This is what makes the site uniquely Taelo's. Reference for the developer prompt:

```
Implement the hero scroll-bound thread mechanic.

The spaceman PNG is positioned absolute, center-right, 60vh tall, z-index 2,
on top of the looping hero-loop.mp4 (z-index 1).

Three SVG paths originate from the spaceman's hand positions
(approx coordinates: hand-left ~58%, 52%; hand-right ~62%, 48%; helmet-top ~60%, 30%)
and extend down-left toward where the next section will reveal.

Each path is drawn with stroke #FFB347, stroke-width 1px, and stroke-dasharray
set to its full length. As window.scrollY progresses from 0 to (windowHeight),
each thread's stroke-dashoffset interpolates from path-length to 0
(thread "draws" from the spaceman's hand to its end point).

When the user has scrolled past the hero, the next section
(INTRO STRIP) slides up from y: 100px to y: 0 with opacity 0 to 1,
duration 1200ms, ease cubic-bezier(0.16, 1, 0.3, 1).

Use GSAP ScrollTrigger with `scrub: true`. No additional libraries.
Respect `prefers-reduced-motion: reduce` — for those users, skip the
thread animation and reveal sections with simple fade.

Mobile: scale spaceman to 40vh, threads simplified to a single path,
reveal animation simplified to fade only.
```

---

## Final checklist before going live

- [ ] First pass wireframe locked
- [ ] Hi-fi conversion done, palette + tokens applied correctly
- [ ] Hero video plays, autoplay, muted, loop, playsinline
- [ ] Spaceman positioned correctly over video
- [ ] Mobile view checked (F12, mobile toggle) — no broken sections
- [ ] All copy passes the Voice Spec (no banned phrases)
- [ ] Email capture works (form posts somewhere or at minimum captures via formspree/getform free tier)
- [ ] Resources section links to actual downloadable file (the 7-overrides pack)
- [ ] No Gemini watermark visible anywhere
- [ ] No console errors
- [ ] Lighthouse score reasonable (>85 perf, >90 a11y)
- [ ] Live URL: taelokim.vercel.app (then point taelokim.com domain)
