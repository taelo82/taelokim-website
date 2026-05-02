# Taelo Kim — Personal Site Handoff Brief

**One-file import for any cloud design tool, AI project, or human collaborator.**
Drop this into Claude Projects, Notion, a Framer brief, a Figma cover doc — it is self-contained.

- **Owner:** Taelo Kim (@taelo82) — VC-turned-operator, ships AI products across Korea, Japan, Southeast Asia
- **Domain:** `taelokim.com` (not yet pointed at deploy)
- **Status:** Layout + interactions complete. Awaiting real copy, real links, deploy.
- **Repo:** `https://github.com/taelo82/taelokim-website`

---

## 1 — Project at a glance

Single-page, single-file vanilla site. **No React, no build step, no npm.** Open `index.html` in a browser, it works.

- One signature interaction: a **scroll-scrubbed astronaut** (`spaceman.mp4`) whose `currentTime` is driven by `window.scrollY / scrollHeight`.
- Three **verlet-rope threads** trail from the spaceman's hands toward the active section's left edge.
- Two **looping background videos** layered behind everything; scroll position drives a cross-fade so the upper page reads as video 1 and the bottom (incl. CTA) as video 2.
- Section panels **slide up** as their slot enters the viewport; cards have ±5° **mouse-tilt + spotlight**.
- Pill-nav at top with **circle-fill ink hover** and active-section lighting.

Aesthetic target: editorial cinematic, dark mint-teal, warm cream typography. Anti-AI-tutorial: no rounded-rectangle stacks, no centered-everything, no lucide icons.

---

## 2 — File inventory

**Required (ship):**
| File | Size | Purpose |
|---|---|---|
| `index.html` | ~75 KB | Entire site — markup + inline CSS + inline JS |
| `tokens.css` | ~1.3 KB | Design tokens (palette, type scale, spacing, motion) |
| `spaceman.mp4` | 4.6 MB | Scroll-scrubbed astronaut foreground video |
| `hero-loop.mp4` | 1.8 MB | Background video #1 (upper page) |
| `hero-loop-2.mp4` | 3.8 MB | Background video #2 (lower page, mirrored via CSS) |

**Unused (safe to delete):**
- `bookshelf-cathedral.jpg`, `bookshelf-portal-arch.jpg`, `bookshelf-portal-closeup.jpg`, `bookshelf-rosewindow.jpg`, `bookshelf-scene.jpg` — bookshelf fragments were ripped out; videos cover that role now
- `tesseract-bg.svg` — unused
- `spaceman-16x9-starter.png`, `spaceman-9x16-clean.png`, `spaceman.png`, `spaceman-original-backup.png` — pre-video stills, kept as backup
- `spaceman.old.mp4` — previous astronaut animation, kept as a one-command revert

**Local run:** `cd` into project folder, `python3 -m http.server 8080`, open `http://localhost:8080`.

---

## 3 — Design system

### Palette (`tokens.css`)
```css
--void:    #050510;   /* page background, deep blue-black */
--paper:   #E8E4DC;   /* primary text — warm cream */
--thread:  #7AB5B0;   /* signature mint-teal accent */
--dust:    #FFFFFF;   /* secondary text + nav (white for now) */
--signal:  #7AB5B0;   /* unified with --thread */
```

Light gradient highlight (used in rope strokes and glows): `#C5E8DE`.
RGB equivalents for `rgba()` usage: `rgba(122, 181, 176, X)` for accent, `rgba(197, 232, 222, X)` for highlight.

**Banned:** purple-blue gradients, pink-purple gradients, generic AI-tutorial output (rounded rectangles + center-aligned everything + lucide icons), warm amber gradients (the gold theme was replaced).

**Allowed (overrides):** subtle hover-tilt on cards (≤5°), low-opacity mint→transparent diagonals.

### Typography
- Display: `Fraunces` (serif, all hero/section headlines)
- Italic emphasis: `Instrument Serif` (used inside `<em>` on hero word "thread.", section pull-quotes)
- Body: `Inter Tight`
- Mono (dates, numbers): `JetBrains Mono`

### Type scale
- `--type-hero`: `clamp(64px, 9vw, 120px)`
- `--type-h1`: `clamp(40px, 5vw, 64px)`
- `--type-h2`: `clamp(28px, 3vw, 40px)`
- `--type-body`: `17px`
- `--type-small`: `14px`
- `--type-mono`: `13px`

### Spacing scale (4 px base)
`4 / 8 / 16 / 24 / 40 / 64 / 96 / 160 px` exposed as `--space-1` through `--space-8`.

### Radius
`2 / 4 / 8 px`. Pill (`999px`) only on the nav, the CTA pill, and the email pill — nowhere else.

### Motion
- Easing: `--ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1)`
- Durations: `--duration-med: 600ms`, `--duration-slow: 1200ms`
- All scroll-driven mechanics respect `prefers-reduced-motion`.

---

## 4 — Page architecture (DOM map)

```
<body>
├── <div class="bg-stage">                  z=0  ── fixed full-bleed
│   ├── <video id="bg-video-1">                 (hero-loop.mp4)
│   └── <video id="bg-video-2">                 (hero-loop-2.mp4, mirrored)
│   └── ::after watermark mask                  (bottom-right Veo cover)
│
├── <svg id="luma-key SVG defs>                 (filters for spaceman)
├── <video id="spaceman">                   z=50 ── fixed
├── <svg id="thread-canvas">                z=1  ── fixed
├── <nav class="pill-nav">                  z=100── fixed
│
└── <main class="scenes">                   z=2
    ├── <section id="hero">
    ├── <div class="panel-slot"><section id="value"></section></div>
    ├── <div class="panel-slot"><section id="resources"></section></div>
    ├── <div class="panel-slot"><section id="writing"></section></div>
    ├── <section id="stats">
    ├── <div id="email-capture" class="final-cta">
    └── <footer>
```

**z-index legend (left → right = back → front):**
`bg-stage(0) → thread-canvas(1) → sections(2) → spaceman(50) → pill-nav(100)`

---

## 5 — Section structure & copy slots

> **All `[REPLACE: ...]` markers below are placeholders. Replace before deploy.**

### 5.1 Hero (`#hero`)
- Eyebrow: `Taelo Kim · Seoul · 2026`
- Headline (ScrollFloat, char-by-char fade): `Pull the / thread.` (italic on "thread.")
- Sub: `[REPLACE: 1-line value prop, ~20 words, direct]`
- CTA: text `See what's inside` → `#resources`

### 5.2 Section One — `#value`
- Section label: `[REPLACE: "What you get" or similar — 2 words]`
- Intro paragraph: `[REPLACE: 1 sentence framing]`
- Three blocks. Each: short label + 2-3 sentences.
  - Block 1 label + body
  - Block 2 label + body
  - Block 3 label + body

### 5.3 Section Two — `#resources`
- Section label: `[REPLACE: "Resources" / "Library" / etc.]`
- Featured card: `[REPLACE: title, description, link to asset/lead-magnet]`
- Three resource cards: each = tag + title + 1-2-sentence description + link

### 5.4 Section Three — `#writing`
- Section label: `[REPLACE: "Writing" / "Notes" / "Field reports"]`
- Four row entries: `title + 1-line subtitle + ISO date + link`

### 5.5 Stats (`#stats`)
- Three numbers + labels: `[REPLACE: 10K+ / 500+ / #1 — needs real metrics]`

### 5.6 Final CTA (`#email-capture`)
- Headline: `[REPLACE: "Get Started" → real climax line]`
- Sub: `[REPLACE: 1-sentence closer]`
- Email pill: `your@email.com` + `Join` button
- **Formspree:** sign up at `https://formspree.io`, replace `REPLACE_WITH_FORMSPREE_ID` in the form `action` URL

### 5.7 Footer
- Copy: `© 2026 Taelo Kim`
- Three links: `[REPLACE: YouTube / X / Email — real URLs]`

### 5.8 Pill nav
Items currently: `Home / Inside / Resources / Reads / Join`. Verify labels match real section names once copy is filled.

---

## 6 — Interactive mechanics (don't break)

### 6.1 Spaceman scroll-scrub
- `spaceman.currentTime = (scrollY / scrollHeight) * spaceman.duration`, lerped at 0.20 to avoid stutter.
- Sizing: `70vh → 56vh` over 1.5 viewports of scroll (gentle shrink). Stays big throughout — it's the signature element.
- Position: `top: 50% → 42%`, `right: 4%` (constant), opacity `1 → 0.92`.
- **Drift right at end of scroll:** `translateX(${18 * ease}%)` so the character clears the CTA's center column.
- Body tilt: `Math.sin(pullProg * π) * 13deg` — leans into the pull at peak.

### 6.2 Verlet rope threads
Three filaments from the spaceman's hands to the active section's left edge.
- 14-point chain, per-rope slack/gravity/damping/iter.
- Rendered as Catmull-Rom → cubic Bezier.
- Routed BEHIND each section (z=1 < section z=2), peeking from left edge as a visible "anchor."
- Origin halos at hands; gradient fades to transparent at section end.

### 6.3 Background video cross-fade
Both videos are fixed full-bleed in `.bg-stage`. JS drives opacity by scroll progress:
- `BG_FADE_START = 0.55` — video 2 begins to appear
- `BG_FADE_END   = 0.80` — video 2 has fully taken over
- `BG_MAX_OPACITY = 0.55`
- Smoothstep easing between the two.
- Video 2 is mirrored (`scaleX(-1)`) so its character sits LEFT — avoids head-on collision with video 1's right-side character during the fade.
- A radial gradient at bottom-right of `.bg-stage` (`::after`) masks the Veo watermark baked into video 1.

### 6.4 Slide panels
Each `.panel-slot` is `100vh` tall. As the slot crosses the viewport, JS sets `--panel-y` (translateY 100% → 0%). Mousemove tilts ±4° at the panel level.

### 6.5 Card tilt + spotlight
Each card writes `--mx/--my/--tx/--ty` CSS vars on mousemove. Tilt capped at 5°; ::before paints a mint radial gradient at cursor position.

### 6.6 PillNav circle-fill
`--pill-r` precomputed per pill on load + resize from each pill's bounding rect. Circle scales 0 → 1 on hover.

### 6.7 ScrollFloat hero
JS splits each line of `.hero-headline` into per-character `<span class="char">`. Scroll progress (0..1 over the first 0.9 viewport) drives each char's opacity + Y-translate in stagger.

### 6.8 Section reveal
`.reveal` class + IntersectionObserver. Children stagger in via `nth-child(n)` transition-delay.

---

## 7 — Recent design decisions (don't re-litigate)

These were debated and resolved — keep them unless explicitly asked to revisit.

1. **Bookshelf fragments removed.** The bg videos cover that visual role. 5 bookshelf JPGs are now unused; safe to delete.
2. **Spaceman stays big.** Earlier version shrank to 36vh — too small. Current `70vh → 56vh` is locked.
3. **Background = two cross-fading videos**, not one. The crossfade is **late** (55% → 80% scroll) so the upper page reads as one bg and the bottom as another bookend.
4. **Bottom dead space** (`32vh padding-bottom` on `.final-cta`) — extends page so video 2 has room to fully bookend without rushing.
5. **Mint-teal accent**, not gold. Replaced amber `#FFB347` with `#7AB5B0` based on user reference thumbnail. Don't bring gold back.
6. **Nav + subtext white** (`--dust: #FFFFFF`). Earlier was warm brown `#6B5B4F` which read as gold-ish.
7. **Veo watermark masked** at bottom-right of bg-stage with a soft radial-gradient void patch.
8. **Scroll hint (↓ scroll) removed** from the hero.

---

## 8 — Pending work (the punch list)

**Content:**
- [ ] Replace every `[REPLACE: ...]` slot in §5 with real copy
- [ ] Real links for resource cards, writing rows, footer socials
- [ ] Confirm pill-nav labels match final section names
- [ ] Voice pass on copy — direct, operator-tone, no marketing fluff

**Forms:**
- [ ] Sign up at `https://formspree.io`, replace `REPLACE_WITH_FORMSPREE_ID` in `index.html`

**QA:**
- [ ] Mobile pass — has been deferred; test on iPhone, fix breaks
- [ ] Lighthouse / a11y check
- [ ] Run with `prefers-reduced-motion` enabled — confirm static fallback reads cleanly

**Cleanup (optional):**
- [ ] Delete unused bookshelf JPGs + `tesseract-bg.svg` + spaceman PNGs
- [ ] Decide if `spaceman.old.mp4` revert artifact stays

**Deploy:**
- [ ] Push final state to `https://github.com/taelo82/taelokim-website`
- [ ] Deploy to Vercel as `taelokim.vercel.app`
- [ ] Point `taelokim.com` DNS at the Vercel project

---

## 9 — Working with this codebase

**Editing rules (carried over from CLAUDE.md):**
- The whole site is **one HTML file** (~75 KB). Prefer `Edit` over `Write` — full rewrites burn tokens and risk breaking the rope physics or spaceman scrub.
- Don't add comments narrating *what* code does. Existing comments explain the non-obvious *why* — match that tone.
- Don't add features beyond the task. Three similar lines is better than a premature abstraction.
- User wants to ship fast; make reasonable design choices and explain — don't ask permission for every tweak.

**Two-Mac sync:**
- GitHub-only, NOT iCloud.
- Before closing on Mac A: `git add . && git commit -m "..." && git push`
- Opening on Mac B: `git pull`

---

## 10 — Reference: full color values for cross-tool import

If your design tool needs hex codes elsewhere:
- Background `#050510`
- Primary text `#E8E4DC`
- Accent / signature `#7AB5B0` — RGB(122, 181, 176)
- Accent highlight (gradient lift) `#C5E8DE` — RGB(197, 232, 222)
- Secondary / nav text `#FFFFFF`
- (Originally muted dust, now retired) `#6B5B4F`

Source reference for accent: bright/mint-leaning area near subject's face in a reference podcast thumbnail (`#5B8288` slate-teal base, lifted toward `#7AB5B0` for more glow / less stale-blue).

---

*Generated for cloud-design import. Self-contained — no external links required to reproduce the site brief.*
