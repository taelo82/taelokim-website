# Taelo Kim Website

Single-page personal site, live at `https://taeloai.com` (repo `taelo82/taelokim-website`; Vercel auto-deploys `main`). Also hosts the SEO blog at `/blog/` (see memory `project_taeloai_blog`). Built by Taelo Kim (X: @taelo_kim, YouTube: @TaeloKim, GitHub: taelo82) — VC-turned-operator, ships AI products across Korea, Japan, Southeast Asia.

## Architecture — read this first

**Stack:** Single-file vanilla HTML/CSS/JS. NO React, NO build step, NO npm. Everything lives in `index.html`. Open it in a browser, it works. This is intentional — the deploy target is a static host (Vercel) and the simplicity is a feature.

**Files:**
- `index.html` — the entire homepage (HTML + inline CSS + inline JS)
- `tokens.css` — design tokens (palette, type scale, spacing, easings)
- `spaceman.mp4` — the astronaut video, scrubbed by scroll position (`spaceman.old.mp4` kept as a revert)
- `hero-loop.mp4` / `hero-loop-2.mp4` — the two background videos in `#bg-stage`, cross-faded by scroll
- `blog/` — blog hub + one folder per post (`blog.css`, `blog.js`); `sitemap.xml`, `robots.txt` at root
- `SITE_HANDOFF.md` — June design handoff brief (older than this file; trust index.html over it)

**Run locally:** `cd` into this folder and `python3 -m http.server 8080`, then open `http://localhost:8080`.

## Section structure (verified against index.html 2026-10-22; conversion rewrite of 2026-08-30)

Order in DOM (`data-screen-label` in quotes):
1. `#hero` "01 Hero"
2. `#what-you-feel` "02 What You Get"
3. `#community` "03 Products"
4. `#writing` "04 Build Logs"
5. `#resources` "05 Classroom"
6. `#about` "06 About"
7. `#consult` "06b Consult"
8. `#join` "07 Join" — email capture, Formspree `xzdoepzz`
9. `<footer>` "08 Footer"

Sections 2–6 sit in `#slot-*` wrappers and use `class="scene"`.

**Fixed layers** (outside `<main>`): `#particle-canvas`, `#cursor-thread`, `#bg-stage` (two bg videos),
`#spaceman` (`<video>` scrubbed by scroll), `#thread-canvas` (verlet-rope SVG), and
`<nav class="glass">`: Home / Products / Build logs / Classroom / About / Blog (`/blog/`) / Get the stack.

## Mechanics that already work — DO NOT BREAK

- **Spaceman scrub** — page scroll % → `spaceman.currentTime`. Scroll down plays forward, scroll up plays reverse. Lerped 0.30, snapping at the end.
- **Verlet rope physics** — three threads from the spaceman's hands. Each is a 14-pt verlet chain with per-rope slack/gravity/damping/iter. Rendered as Catmull-Rom → cubic Bezier for silken smoothness. Routes BEHIND each section (z=1 < section z=2), peeking from the left edge as a visible "anchor."
- **`#dissolve` filter** — `feTurbulence` + `feDisplacementMap` (scale=26) for organic edge dissolve. (The bookshelf SVG it was built for is gone.)
- **Section reveal** — `.reveal` class + IntersectionObserver. Children stagger in via `nth-child(n)` transition-delay.
- **Card tilt + spotlight** — cards write `--mx/--my/--tx/--ty` CSS vars on mousemove; tilt capped at 5°.
- **All of the above respects `prefers-reduced-motion`** — kill switches in the CSS @media query at the bottom of the `<style>` block, plus `prefersReducedMotion` JS guard.

## Design rules (from `2026-04-26-claude-design-entry-kit.md`)

- **Palette:** void (`#0A0A11`), paper (`#E8E4DC`), thread/amber (`#FFB347`), dust (`#6B5B4F`), signal/cyan (sparingly).
- **Type:** Fraunces (display), Instrument Serif (italic emphasis on key words like "thread"), Inter Tight (body), JetBrains Mono (dates/numbers).
- **One signature interaction:** the spaceman threads. Everything else is passive (hover-only, cursor-only). Don't add a second scroll-bound mechanic.
- **Originally banned, now overridden by user request:** subtle hover-tilt on cards (≤5°), gradients (warm amber→transparent diagonals at low opacity).
- **Still banned:** purple-blue gradients, pink-purple gradients, generic AI-tutorial output (rounded rectangles + center-aligned everything + lucide icons).

## Pending tasks

Done since June: Formspree wired (`xzdoepzz`), real copy (2026-08-30 conversion rewrite), Vercel deploy.
- [ ] **Mobile QA**, **Lighthouse / a11y** — not confirmed done; check before claiming.

## Two-Mac workflow

Work syncs via GitHub, NOT iCloud. Repo: https://github.com/taelo82/taelokim-website

- Before closing on Mac A: `git add . && git commit -m "..." && git push`
- Opening on Mac B: `git pull`
- That's it.

## Behavior notes for Claude

- Bypass permission prompts; user has explicitly authorized this for this project.
- User prefers Opus for design work, Sonnet for routine edits (latest versions).
- When editing `index.html`, prefer `Edit` over `Write` — file is large, full rewrites burn tokens and risk breaking the rope physics / spaceman scrub blocks.
- Don't add comments narrating what code does. The existing comments explain non-obvious *why* — match that tone, don't add planning chatter.
- User wants to work fast and ship; don't ask permission for reasonable design choices, just make them and explain.
