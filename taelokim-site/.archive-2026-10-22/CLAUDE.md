# Taelo Kim Website

Single-page personal site at `taelokim.com` (deployed at `taelokim.vercel.app`). Built by Taelo Kim (X: @taelo_kim, YouTube: @TaeloKim, GitHub: taelo82) — VC-turned-operator, ships AI products across Korea, Japan, Southeast Asia.

## Architecture — read this first

**Stack:** Single-file vanilla HTML/CSS/JS. NO React, NO build step, NO npm. Everything lives in `index.html`. Open it in a browser, it works. This is intentional — the deploy target is a static host (Vercel) and the simplicity is a feature.

**Files:**
- `index.html` — the entire site (HTML + inline CSS + inline JS)
- `tokens.css` — design tokens (palette, type scale, spacing, easings)
- `spaceman.mp4` — the astronaut video, scrubbed by scroll position
- `spaceman.old.mp4` — previous astronaut (back-and-forth pull animation), kept as a one-command revert
- `hero-loop.mp4` — looping background in the hero section
- `bookshelf.svg` — referenced by `#shelves` for the floating bookshelf fragments

**Run locally:** `cd` into this folder and `python3 -m http.server 8080`, then open `http://localhost:8080`.

## Section structure (current — applied from the AIS student-template)

Order in DOM:
1. **Hero** (`#hero`) — full-bleed video bg + ScrollFloat char-fade headline ("Pull the / *thread.*"). Each char's opacity + Y-translate is scrubbed by scroll over the first ~0.9 viewport.
2. **Section One** (`#value` inside `.panel-slot`) — SlidePanel: slides up from `translateY(100%)` → `0%` driven by its slot's scroll progress; mousemove tilts the whole panel ±4°. Three text blocks ("First/Second/Third block").
3. **Section Two** (`#resources` inside `.panel-slot`) — SlidePanel. Featured card + 3-card grid. Cards have their own ±5° tilt (composes with panel tilt).
4. **Section Three** (`#writing` inside `.panel-slot`) — SlidePanel. 4 row-style entries.
5. **Stats** (`#stats`) — 3-number band, no slide-up (single row, doesn't earn a full panel).
6. **Final CTA** (`#email-capture`) — centered "Get Started" headline + email pill (input + amber Join button fused into one rounded glass surface).
7. **Footer** — copy + 3 social links.

**Floating layers** (siblings of `<main class="scenes">`, not inside any section):
- `#shelves` — bookshelf SVG fragments along left edge (z=0)
- `#thread-canvas` — verlet-rope SVG paths from spaceman's hand to active section's left edge (z=1)
- `#spaceman` — `<video>` element scrubbed by `window.scrollY / scrollHeight` (z=50)
- `<nav class="pill-nav">` — fixed top, paper-fill on hover, lit when its section is active (z=100)

## Mechanics that already work — DO NOT BREAK

- **Spaceman scrub** — page scroll % → `spaceman.currentTime`. Scroll down plays forward, scroll up plays reverse. Lerped 0.20 to avoid stutter.
- **Verlet rope physics** — three threads from the spaceman's hands. Each is a 14-pt verlet chain with per-rope slack/gravity/damping/iter. Rendered as Catmull-Rom → cubic Bezier for silken smoothness. Routes BEHIND each section (z=1 < section z=2), peeking from the left edge as a visible "anchor."
- **Bookshelf SVG** — `feTurbulence` + `feDisplacementMap` (scale=10) for organic edge dissolve. `mix-blend-mode: screen`. Scale=22 was too distorted — locked at 10.
- **Section reveal** — `.reveal` class + IntersectionObserver. Children stagger in via `nth-child(n)` transition-delay.
- **Card tilt + spotlight** — cards write `--mx/--my/--tx/--ty` CSS vars on mousemove; tilt capped at 5°.
- **PillNav circle-fill** — `--pill-r` is precomputed per pill on load + resize from each pill's bounding rect.
- **All of the above respects `prefers-reduced-motion`** — kill switches in the CSS @media query at the bottom of the `<style>` block, plus `prefersReducedMotion` JS guard.

## Design rules (from `2026-04-26-claude-design-entry-kit.md`)

- **Palette:** void (`#0A0A11`), paper (`#E8E4DC`), thread/amber (`#FFB347`), dust (`#6B5B4F`), signal/cyan (sparingly).
- **Type:** Fraunces (display), Instrument Serif (italic emphasis on key words like "thread"), Inter Tight (body), JetBrains Mono (dates/numbers).
- **One signature interaction:** the spaceman threads. Everything else is passive (hover-only, cursor-only). Don't add a second scroll-bound mechanic.
- **Originally banned, now overridden by user request:** subtle hover-tilt on cards (≤5°), gradients (warm amber→transparent diagonals at low opacity).
- **Still banned:** purple-blue gradients, pink-purple gradients, generic AI-tutorial output (rounded rectangles + center-aligned everything + lucide icons).

## Pending tasks

- [ ] **Formspree ID** — sign up at https://formspree.io, get form ID, replace `REPLACE_WITH_FORMSPREE_ID` in `index.html` (currently in `final-cta__form action`).
- [ ] **Real copy** — every section has placeholder text ("Section One/Two/Three", "First/Second/Third block", "Card title one", etc). Section labels, card titles + descriptions, featured resource title, writing entries, stats numbers, final CTA headline.
- [ ] **Real links** — resource cards (`href="#email-capture"` placeholder), writing rows (`href="#"`), footer socials (`href="#"`).
- [ ] **Pill nav labels** — currently Home / Inside / Resources / Reads / Join. Verify these match real section names once copy is filled.
- [ ] **Mobile QA** — has been deferred. Test on iPhone, fix any breaks.
- [ ] **Voice pass** on copy — when filled, run it past the voice spec.
- [ ] **Lighthouse / a11y check.**
- [ ] **Deploy to Vercel** at `taelokim.vercel.app`, then point `taelokim.com` at it.

## Two-Mac workflow

Work syncs via GitHub, NOT iCloud. Repo: https://github.com/taelo82/taelokim-website

- Before closing on Mac A: `git add . && git commit -m "..." && git push`
- Opening on Mac B: `git pull`
- That's it.

## Behavior notes for Claude

- Bypass permission prompts; user has explicitly authorized this for this project.
- User prefers Opus 4.7 for design work, Sonnet 4.6 for routine edits.
- When editing `index.html`, prefer `Edit` over `Write` — file is large, full rewrites burn tokens and risk breaking the rope physics / spaceman scrub blocks.
- Don't add comments narrating what code does. The existing comments explain non-obvious *why* — match that tone, don't add planning chatter.
- User wants to work fast and ship; don't ask permission for reasonable design choices, just make them and explain.
