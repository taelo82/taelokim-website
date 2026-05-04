# `/watch` install — copy-paste for video description

## Easy path (works most of the time)

In Claude Code, run:

```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

Restart Claude Code. Get a free Groq API key at https://console.groq.com/keys and paste it into `~/.config/watch/.env` on the `GROQ_API_KEY=` line. Done. Try it: `/watch <any video URL>`.

## Messy path — when YouTube blocks the download (5 commands)

If `/watch` fails with HTTP 403 or "fragment not found" errors, YouTube is in active war with yt-dlp. Run these in your terminal:

```bash
# 1. Install uv (no sudo needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install Python 3.11 + yt-dlp nightly with EJS support
~/.local/bin/uv python install 3.11
~/.local/bin/uv tool install --python 3.11 --force --pre "yt-dlp[default]"

# 3. Install Deno (JS runtime needed for SABR challenge solving)
curl -fsSL https://deno.land/install.sh | sh
ln -sf ~/.deno/bin/deno ~/.local/bin/deno

# 4. Patch the skill to use cookies + player_client override
# Open ~/.claude/skills/watch/scripts/download.py and add this near the top:
#   import os
# Then in the cmd list add:
#   "--extractor-args", "youtube:player_client=tv,web_safari,mweb",
# And after the cmd list:
#   if os.environ.get("WATCH_COOKIES_BROWSER"):
#       cmd.extend(["--cookies-from-browser", os.environ["WATCH_COOKIES_BROWSER"]])
#   cmd.append(url)

# 5. Run /watch with cookies enabled
WATCH_COOKIES_BROWSER=chrome /watch <video-url>
```

If you're on a different browser (Safari, Firefox, Edge, Brave), swap `chrome` for the browser name. Keep YouTube logged in there — yt-dlp uses your session cookies to authenticate the download.

---

## Source skill (huge respect)
Built and given away free by Brad Bonanno: https://github.com/bradautomates/claude-video
Original walkthrough: https://youtu.be/QZMljuD10sU
