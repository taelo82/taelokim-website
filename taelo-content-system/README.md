# Taelo Kim — AI Content System

## What This Is
A 5-agent AI content pipeline that finds trends, writes scripts, designs thumbnails, and delivers a daily brief. Built to run with Claude Code (Option B) with a clear migration path to full automation (Option A).

## Quick Start

### 1. Copy this entire folder into your Claude Code project
```
taelo-content-system/
  CLAUDE.md              ← Master instructions (Claude Code reads this)
  agents/
    01-channel-analyst.md
    02-trend-scout.md
    03-script-writer.md
    04-thumbnail-designer.md
    05-daily-reporter.md
  brand/
    voice.md             ← Your brand voice (pre-filled, refine after Agent 01)
    competitors.md       ← Fill in your competitor channels
  outputs/
    scripts/
    thumbnails/
    reports/
    trends/
```

### 2. Fill in your competitor channels
Edit `brand/competitors.md` with 10-15 YouTube channels in your niche.

### 3. Run the Channel Analyst first
In Claude Code:
```
"Run Agent 01 (Channel Analyst). My channel is @TaeloKim. 
Competitor channels are listed in brand/competitors.md. 
Update brand/voice.md and brand/competitors.md with your findings."
```

### 4. Run the daily pipeline
Each morning in Claude Code:
```
"Run today's content pipeline. Follow the order in CLAUDE.md. 
Start with Trend Scout, then Script Writer, then Thumbnail Designer, then Daily Reporter.
Save all outputs with today's date."
```

Or run individual agents:
```
"Run the Trend Scout agent for today."
"Write a script based on today's trend report."
```

## Migration Path

### Current: Option B (Hybrid)
- Agent prompts live as .md files
- You run them manually through Claude Code
- Claude Code can generate Python wrappers when you're ready

### Future: Option A (Full Auto)
- Same .md prompts become system prompts in Python scripts
- Python scripts call Anthropic API (or swap to OpenRouter for cheaper tokens)
- Cron job or n8n runs the pipeline daily at 6am
- You wake up to an email with the daily brief

### What changes in migration:
- `.md` files → embedded as system prompts in Python
- Manual Claude Code invocation → `python run_daily_pipeline.py`
- Add `.env` file with API keys
- Add Google Sheets integration (optional — or keep everything in local markdown files)

### What stays the same:
- The agent prompts (core IP)
- The pipeline order
- The output format
- The brand voice document

## Costs

### Option B (Current)
- Claude Pro subscription: included (you already have it)
- YouTube Data API: Free
- Total: $0 additional

### Option A (Future)
- Anthropic API or OpenRouter: ~$15-40/month
- YouTube Data API: Free
- Twitter API (optional): $20-40/month
- n8n (optional): Free-$20/month
- Total: ~$35-100/month
