# Taelo Kim — AI Content System

## Overview
A 5-agent content pipeline for the Taelo Kim YouTube channel (@TaeloKim).
Run agents **on demand** — whenever Taelo is actively hunting for a topic, angle, script, title, or thumbnail. No daily/weekly schedule. Each agent is invoked only when needed for the moment.

## Channel Context
- **Channel:** Taelo Kim (@TaeloKim)
- **Niche:** AI tools, tech, building in public, making money online
- **Audience:** Builders, operators, and indie makers in Korea and Southeast Asia
- **Voice:** Raw, direct, unpolished. No corporate fluff. Real numbers, real experience.
- **Languages:** English primary, Korean secondary

## Agents (run on demand)
1. **Channel Analyst** (`agents/01-channel-analyst.md`) — Refresh brand voice + competitor analysis
2. **Trend Scout** (`agents/02-trend-scout.md`) — Find a content opportunity right now
3. **Script Writer** (`agents/03-script-writer.md`) — Write a ready-to-record script
4. **Thumbnail Designer** (`agents/04-thumbnail-designer.md`) — Generate 3 thumbnail concepts
5. **Daily Reporter** (`agents/05-daily-reporter.md`) — Compile a brief summary of the session

## How to invoke
Run individual agents as needed:
- "Run Trend Scout" — when looking for a topic
- "Write a script for [topic]" — when ready to produce
- "Give me 3 thumbnail concepts for [script]" — when finalizing the package
- Chain them only if Taelo asks for the full flow in one go

## Brand Context Files
- `brand/voice.md` — Brand voice document (output of Channel Analyst)
- `brand/competitors.md` — Competitor tracking

## Output Locations
- `outputs/scripts/` — Scripts (markdown)
- `outputs/thumbnails/` — Thumbnail concept briefs
- `outputs/reports/` — Reporter summaries
- `outputs/trends/` — Trend scout findings

## Raw takes (gitignored)
- `raw-takes/` — drop folder for raw `.mov` / `.mp4` recordings (OBS, QuickTime, Opus Clip exports). Files here are excluded from git via root `.gitignore`. When asked to "review the latest takes", `ls -lt raw-takes/` and pick by recency.

## Rules
- Skip script if no outliers found
- Skip thumbnails if no script produced
- All outputs include date in filename: `YYYY-MM-DD-title.md`

## Migration Notes
- **Current (Option B):** Agent prompts as .md files → Claude Code generates Python wrappers → Anthropic API
- **Future (Option A):** Same .md prompts → swap Anthropic API for OpenRouter → on-demand API calls
- The .md agent files are the core IP. They stay the same regardless of execution layer.
