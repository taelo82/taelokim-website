# Brand Spec — taelokim.com

> Use this spec + the attached `tokens.css` + the hero/section screenshots
> to design any piece of collateral (PDF, slide deck, social card, etc.) so
> it shares the same visual and verbal language as the site.

## Identity

**Name:** Taelo Kim
**Site:** taelokim.com
**Discipline:** Builder / operator. Reviewed 150+ pitches as a VC, then crossed
the table — shipped products in K-beauty, AI tooling, e-commerce across Korea,
Japan, and Southeast Asia.

## What this brand IS

- Direct. Skeptical of hype. Real numbers over adjectives.
- Cinematic restraint. Most of every page is dark void. The amber light is a
  rare event, not a decoration.
- Operator perspective. Korea / Southeast Asia builders, not US/SF SaaS.
- One signature gesture per page. Nothing is sprinkled.

## What this brand is NOT

- AI-fantasy aesthetics (no purple-to-blue gradients, no neon, no nebulae)
- SaaS landing-page conventions (no pills, no glassmorphism, no "AI-powered" copy)
- Soft, friendly, approachable startup tone
- Containers, cards-with-rounded-corners, "trusted by" logo strips
- Stock photography or AI-generated art that looks AI-generated

## Visual primitives (from tokens.css)

| Token | Value | Use |
|---|---|---|
| `--void` | `#050510` | Page background. Default state. |
| `--paper` | `#E8E4DC` | Primary text on void. |
| `--thread` | `#FFB347` | Warm amber. The "light" — the signature accent. |
| `--dust` | `#6B5B4F` | Secondary text, muted UI. |
| `--signal` | `#00C2FF` | Reserved. Used ONCE per page (the email CTA). |

**Typography:**
- **Display:** Fraunces (free, serif). Italic for emphasis (e.g. *thread.*).
  Used at clamp(64px, 9vw, 120px) for hero, smaller for section headlines.
- **Body:** Inter Tight (free, neo-grotesque). 17px standard, 14px small,
  uppercase + 0.18em letter-spacing for section labels.
- **Mono:** JetBrains Mono. Dates, build metrics.

**Spacing scale:** 4px base. `4 / 8 / 16 / 24 / 40 / 64 / 96 / 160`.

**Motion:** cubic-bezier(0.16, 1, 0.3, 1). Slow ~1200ms. Single signature
mechanic per page (the spaceman pulling threads, on the site). Everything
else is clean opacity fade.

## Banned defaults

- Inter, Roboto, Geist, Söhne (SaaS sans-serifs)
- Pills / pill buttons / pill nav
- Glassmorphism / frosted blur
- Purple-blue or pink-purple gradients
- Container cards with rounded corners + subtle borders
- Blinking status dots / "live" indicators
- Three-column feature grids with icons
- Logo cloud / "trusted by"
- Cookie banners, sticky popovers
- Hover-tilt on every card; parallax on every section

## Voice

**Tone:** Direct. Operator. Skeptical. Says what others dance around.
Backs claims with numbers. Korean phrases when more precise than English
(sparingly).

**Yes:** "Here's what actually happened" · "I tested this so you don't have to"
· "The real numbers" · "No BS" · concrete numbers, dates, dollar amounts

**No:** "AI-powered" · "leverage" · "synergy" · "ecosystem" · "side hustle"
· "passive income" · "game-changer" · "smash that like button" · fake
urgency · generic SaaS speak

## Layout primitives

- **Hero:** full-viewport. Looping background video (warm amber light shaft +
  dust on void). Spaceman PNG/video layered over right side. Headline left,
  in display serif, with one italic word in amber.
- **Sections:** max-width 860px, generous vertical padding (var(--space-8)).
  Tight typography. No hero whitespace fluff.
- **Cards:** hard edges (radius 2-8px), no shadows, no rounded corners by
  default. Typographic, not container-y.
- **Section labels:** uppercase, 11px, 0.18em letter-spacing, dust color,
  followed by a thin horizontal rule.

## Composition cues for collateral (PDF / slides / cards)

- Most of the page is `--void`. Negative space is the design.
- One amber accent per spread (a rule, a callout, an italic word).
- Headlines big serif with one italic + amber word. Body small + tight.
- Hard horizontal rules instead of card borders.
- No drop shadows, no gradients on text, no glow effects.
- One light element per spread — never a whole color field.

## Reference inspiration (taste coordinates)

- **Composition / spacing rhythm:** Linear (linear.app, 2023 redesign)
- **Section pacing:** Apple product pages (long-scroll cinema)
- **Color discipline:** Vercel — neutral 95% / one warm accent
- **Typography pairing:** serif display + neo-grotesque body
- **Density:** tight, deliberate, no whitespace fluff
- **Microcopy tone:** Arc Browser — playful but precise
- **Hero treatment:** Anthropic.com homepage — cinematic + minimal text
- **Footer style:** Stripe — quiet, confident, under-designed
