# Credit Pool Video — Animated Graphics

Animated B-roll for the **Anthropic Same-Day Switch** video (2026-05-15 / 2026-05-16).

## File layout

| Beat | HTML source (editable) | Opaque mp4 (B-roll cut) | Transparent mov (PIP overlay) |
|---|---|---|---|
| 1A · 0:14–0:24 — split-screen reveal | `01-cold-open-split-screen.html` | `.mp4` | `.mov` |
| 1A · 0:24–0:30 — 40× stamp | `02-forty-x-stamp.html` | `.mp4` | `.mov` |
| 1B · 0:35–0:50 — why you care · tool grid | `03-why-you-care-tools.html` | `.mp4` | `.mov` |
| 1B / 3 · $5K → $200 drop | `04-5k-to-200-drop.html` | `.mp4` | `.mov` |
| 3 · 3:30–3:50 — Extra Usage toggle off | `05-extra-usage-toggle.html` | `.mp4` | `.mov` |
| 4 · 4:00–4:30 — Community Note | `06-community-note.html` | (skipped — use real tweet screenshot) | — |
| 5 · 4:50–6:10 — 5 personas | `07-five-personas.html` | `.mp4` | `.mov` |
| 6 · 6:10–7:40 — 3 moves | `08-three-moves.html` | `.mp4` | `.mov` |
| 9 · 9:10–10:30 — Friday reset closer | `09-friday-reset.html` | `.mp4` | `.mov` |
| 2 · ~2:00 — help-center receipt (covered vs not) | `12-covered-vs-not.html` | `.mp4` | `.mov` |
| 1B · ~0:50 — June 15 banner + branding clause | `13-june15-banner.html` | `.mp4` | `.mov` |
| 3 · ~3:00 — spectrum grid (which tool, which pool) | `10-spectrum-grid.html` | `.mp4` | `.mov` |
| 4 · ~4:10 — Matt Pocock "frustrating lack of clarity" | `11-pocock-tweet.html` | `.mp4` | `.mov` |

**Pick the right format:**
- `.mp4` (opaque, cream paper bg) → drop in as full-screen B-roll cut. Cut from face-cam to graphic and back.
- `.mov` (transparent, ProRes 4444 alpha) → drop on top of face-cam as picture-in-picture overlay. Works in Premiere / FCP / DaVinci. About 10× larger than the mp4.

## Manual reveal keys (live recording mode)

Some graphics have multi-step reveals. Open the `.html` in Chrome fullscreen and tap a key to advance on Taelo's cue (the recorded `.mp4`/`.mov` use auto-play timing — use manual mode if you want different pacing):

- **`07-five-personas.html`** — press `1` / `2` / `3` / `4` / `5` to reveal each persona; `0` or `space` for the footer prompt; `r` to reset.
- **`08-three-moves.html`** — press `1` / `2` / `3` to reveal each move; `r` to reset.
- All others auto-play on load. Press `r` in any to replay.

## Style baseline

Locked palette — no other colors:
- `--paper: #F1E9D6` (sandpaper-grain cream)
- `--ink: #1E2832` (primary text / borders)
- `--ink-soft: #7A8590` (secondary)
- `--red: #C8463C` (critical · cut · deadline only)
- `--highlight: #F4E04D` (yellow marker stripe, one phrase per graphic)

Type: Inter for headings · JetBrains Mono for data/dates · Source Serif Pro italic for captions. Texture: animated SVG turbulence noise overlay drifting every 14s. Layout: 1.5px dashed borders, ±0.8°–2° card tilts, line-art SVG icons (no fills) with one red accent stroke per icon. No emoji. No gradients. No multi-color cards.

## Re-render after edits

If you edit any HTML and want to re-render its mp4 + mov:

```bash
cd taelo-content-system/outputs/graphics/2026-05-15-credit-pool
python3 render.py            # renders all (skips 06)
python3 render.py 04 07      # renders only graphics with prefix 04 and 07
```

Each HTML's `<body data-duration="N">` attribute is how the script knows when to stop capturing. If you add new animation that runs past the existing duration, bump that number first.

### One-time setup

```bash
pip3 install --user playwright
python3 -m playwright install chromium
# also requires ffmpeg in PATH (already installed: /Users/ek/.local/bin/ffmpeg)
```

## Why HTML as the source

- Iterate in seconds — edit text/timing, refresh Chrome, see the change instantly.
- Re-renders are deterministic: same HTML → same MP4 + MOV.
- Version-control friendly (the source is a few KB of text, not a 50 MB binary).
- The MP4/MOV are derived artifacts. The HTML is the source of truth.

## Notes

- `06-community-note.html` is intentionally not rendered — Taelo is dropping a real screenshot of the Lydia Hallie tweet + Community Note in that beat instead.
- All graphics designed to be cut into the video as B-roll, not as picture-in-picture (face-cam stays full-frame between graphic cuts). The `.mov` files are provided in case you want to PIP-overlay them on a future video edit.
- Total folder size after render: ~500 MB (mostly the .mov files). If you want to gitignore the rendered binaries, add `*.mp4` and `*.mov` to a folder-scoped `.gitignore` — the HTML source files alone reproduce the videos.
