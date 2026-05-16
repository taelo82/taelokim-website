#!/usr/bin/env python3
"""
render.py — Render each .html graphic in this folder to two video formats:

    foo.html  →  foo.mp4   (1920x1080 H.264, opaque cream paper bg, B-roll cuts)
                 foo.mov   (1920x1080 ProRes 4444, transparent bg, PIP overlays)

Animation duration is read from <body data-duration="MS">. We capture PNG
frames at 30 fps for (duration + 800 ms tail), then ffmpeg encodes each pass.

Skips 06-community-note.html per user direction.

Usage:
    python3 render.py                # render every HTML except 06
    python3 render.py 02 04          # render only 02 and 04 (number prefix match)
"""

import asyncio
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from playwright.async_api import async_playwright

HERE = Path(__file__).parent
FPS = 30
WIDTH, HEIGHT = 1920, 1080
SKIP_STEMS = {"06-community-note"}  # User is providing a real screenshot for this one

# CSS injected for the transparent pass — kills the paper background + grain
# overlay + vignette so the recording captures only the foreground elements
# with alpha preserved.
TRANSPARENT_CSS = """
  html, body { background: transparent !important; background-color: rgba(0, 0, 0, 0) !important; }
  body::before, body::after { display: none !important; }
"""


def find_html_files(filter_prefixes=None):
    files = sorted(p for p in HERE.glob("*.html"))
    out = []
    for p in files:
        stem = p.stem
        if stem in SKIP_STEMS:
            print(f"  · skip {p.name} (in SKIP list)")
            continue
        if filter_prefixes:
            prefix = p.name.split("-", 1)[0]
            if prefix not in filter_prefixes and stem not in filter_prefixes:
                continue
        out.append(p)
    return out


def read_duration_ms(html_path):
    """Pull data-duration="NNNN" from <body> tag; default 8000 ms."""
    text = html_path.read_text()
    m = re.search(r'<body[^>]*\bdata-duration\s*=\s*"(\d+)"', text)
    if not m:
        print(f"  ⚠ {html_path.name} has no data-duration; defaulting to 8000 ms")
        return 8000
    return int(m.group(1))


async def capture_frames(html_path, frames_dir, total_ms, transparent=False):
    frames_dir.mkdir(parents=True, exist_ok=True)
    # Wipe any previous frames
    for f in frames_dir.glob("frame_*.png"):
        f.unlink()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            args=["--disable-web-security", "--allow-file-access-from-files"]
        )
        context_kwargs = {
            "viewport": {"width": WIDTH, "height": HEIGHT},
            "device_scale_factor": 1,
        }
        context = await browser.new_context(**context_kwargs)
        page = await context.new_page()

        # Navigate to the file
        await page.goto(html_path.as_uri())

        # If transparent pass, inject CSS BEFORE the animation kicks in
        # (autoplay is on a 500 ms setTimeout — we have time)
        if transparent:
            await page.add_style_tag(content=TRANSPARENT_CSS)

        # Wait for the page's auto-play to start (500 ms internal delay)
        await page.wait_for_timeout(100)

        # Capture frames for total_ms + 800 ms tail
        end_ms = total_ms + 800
        frame_interval_ms = int(1000 / FPS)
        n_frames = int(end_ms / frame_interval_ms)
        for i in range(n_frames):
            target_ms = i * frame_interval_ms
            now = await page.evaluate("performance.now()")
            wait = target_ms - now
            if wait > 0:
                await page.wait_for_timeout(int(wait))
            screenshot_kwargs = {
                "path": str(frames_dir / f"frame_{i:04d}.png"),
                "omit_background": transparent,
            }
            await page.screenshot(**screenshot_kwargs)

        await context.close()
        await browser.close()
    return n_frames


def encode_h264(frames_dir, out_path):
    """Opaque H.264 .mp4 for B-roll cuts."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-framerate", str(FPS),
        "-i", str(frames_dir / "frame_%04d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "slow",
        "-crf", "18",
        "-movflags", "+faststart",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)


def encode_prores4444(frames_dir, out_path):
    """ProRes 4444 .mov with alpha for PIP overlays."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-framerate", str(FPS),
        "-i", str(frames_dir / "frame_%04d.png"),
        "-c:v", "prores_ks",
        "-profile:v", "4",  # 4 = ProRes 4444
        "-pix_fmt", "yuva444p10le",  # 10-bit with alpha
        "-vendor", "apl0",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)


async def render_one(html_path):
    name = html_path.stem
    duration_ms = read_duration_ms(html_path)
    print(f"\n→ {html_path.name}  (duration {duration_ms} ms)")

    work = HERE / ".render-tmp" / name
    work.mkdir(parents=True, exist_ok=True)

    # PASS A: opaque H.264
    print("  · capturing opaque frames…")
    frames_opaque = work / "opaque"
    n = await capture_frames(html_path, frames_opaque, duration_ms, transparent=False)
    print(f"  · {n} frames captured; encoding H.264 …")
    encode_h264(frames_opaque, HERE / f"{name}.mp4")
    print(f"    ✓ {name}.mp4")

    # PASS B: transparent ProRes 4444
    print("  · capturing transparent frames…")
    frames_alpha = work / "alpha"
    n = await capture_frames(html_path, frames_alpha, duration_ms, transparent=True)
    print(f"  · {n} frames captured; encoding ProRes 4444 …")
    encode_prores4444(frames_alpha, HERE / f"{name}.mov")
    print(f"    ✓ {name}.mov")

    # Cleanup PNGs (keep working dir if you want to inspect)
    shutil.rmtree(work, ignore_errors=True)


async def main():
    filter_prefixes = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    targets = find_html_files(filter_prefixes)
    if not targets:
        print("No HTML files matched.")
        sys.exit(1)
    print(f"Rendering {len(targets)} file(s) to MP4 + MOV at {WIDTH}×{HEIGHT}@{FPS}fps")
    for html in targets:
        try:
            await render_one(html)
        except Exception as e:
            print(f"  ✗ {html.name} failed: {e}")
    # Final cleanup of empty tmp dir
    tmp = HERE / ".render-tmp"
    if tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
