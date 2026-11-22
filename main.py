#!/usr/bin/env python3
"""World Today — 22 November 2026.

Summarises 22 November 2026's world news in a single 1024x1024 image.

Run:  python3 main.py
Out:   /output/entry.png  (falls back to ./entry.png when run elsewhere)

If Pillow is unavailable the script does NOT crash: it copies the bundled
entry.png (shipped in this repository) to the output path instead, so the
entry still produces a valid image.
"""

import os
import shutil
import sys
import textwrap

OUTPUT_PATH = "/output/entry.png"
SIZE = (1024, 1024)

# Headlines verified against real 22 Nov 2026 reporting
# (AFP / AP / Reuters via The Manila Times, 22 November 2026).
STORIES = [
    {
        "tag": "BRAZIL  ·  DISASTER",
        "color": (176, 58, 44),
        "headline": "Brazil town clears rubble after deadly storm",
        "detail": "\u201cWe lost everything\u201d: residents pick through the wreckage as a fierce storm leaves a trail of destruction.",
    },
    {
        "tag": "TECH  ·  MARKETS",
        "color": (18, 110, 130),
        "headline": "Nvidia faces US accounting probe amid deepening turmoil",
        "detail": "Regulators open an accounting inquiry as pressure mounts on the chip giant.",
    },
    {
        "tag": "DEFENCE  ·  NORTH AMERICA",
        "color": (46, 74, 124),
        "headline": "Pentagon moves to restrict US-Canada defence ties",
        "detail": "Washington tightens military cooperation with its northern neighbour.",
    },
    {
        "tag": "USA  ·  ECONOMY",
        "color": (122, 74, 8),
        "headline": "Trump vows to cap credit card interest at 10%",
        "detail": "The president says he will work with Democrats to limit card interest rates.",
    },
    {
        "tag": "PERU  ·  EARTHQUAKE",
        "color": (90, 90, 90),
        "headline": "6.7-magnitude quake hits Peru",
        "detail": "A strong tremor shakes the country; no deaths reported so far.",
    },
    {
        "tag": "MIDDLE EAST  ·  CONFLICT",
        "color": (120, 40, 40),
        "headline": "Houthis launch revenge strikes on Saudi capital",
        "detail": "Missiles target Riyadh as regional tensions flare again.",
    },
]

DATE_LINE = "22 NOVEMBER 2026"
TITLE = "WORLD TODAY"
SUBTITLE = "Six stories that defined the day"


def _bundled_entry():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def _fallback_copy(out_path):
    src = _bundled_entry()
    if os.path.exists(src):
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        shutil.copyfile(src, out_path)
        print("Pillow unavailable; copied bundled entry.png to %s" % out_path)
        return True
    print("Pillow unavailable and no bundled entry.png found", file=sys.stderr)
    return False


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        ok = _fallback_copy(out_path)
        sys.exit(0 if ok else 1)

    try:
        from PIL import Image, ImageDraw, ImageFont  # noqa: F401
    except ImportError:  # pragma: no cover - handled above
        sys.exit(1)

    def font(name, size):
        paths = {
            "bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "regular": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        }
        try:
            return ImageFont.truetype(paths[name], size)
        except (OSError, KeyError):
            return ImageFont.load_default()

    W, H = SIZE
    bg = (247, 244, 238)
    ink = (24, 26, 32)
    muted = (96, 96, 100)
    img = Image.new("RGB", SIZE, bg)
    d = ImageDraw.Draw(img)

    # --- Header band ---
    d.rectangle([0, 0, W, 168], fill=(16, 24, 44))
    d.rectangle([0, 168, W, 174], fill=(198, 160, 60))
    d.text((48, 26), TITLE, font=font("bold", 64), fill=(255, 255, 255))
    d.text((48, 104), SUBTITLE, font=font("regular", 26), fill=(205, 210, 225))
    d.text((W - 48, 34), DATE_LINE, font=font("bold", 30),
           fill=(198, 160, 60), anchor="ra")
    d.text((W - 48, 78), "SUNDAY", font=font("regular", 24),
           fill=(205, 210, 225), anchor="ra")
    d.text((W - 48, 112), "6 STORIES  ·  1 IMAGE", font=font("regular", 22),
           fill=(205, 210, 225), anchor="ra")

    # --- Story grid: 2 columns x 3 rows ---
    margin = 32
    gap = 20
    top = 196
    card_w = (W - 2 * margin - gap) // 2
    card_h = 238
    row_gap = 18

    for i, story in enumerate(STORIES):
        col = i % 2
        row = i // 2
        x0 = margin + col * (card_w + gap)
        y0 = top + row * (card_h + row_gap)
        x1 = x0 + card_w
        y1 = y0 + card_h
        # card
        d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(255, 255, 255),
                            outline=(222, 218, 210), width=1)
        # accent bar + number badge
        d.rounded_rectangle([x0, y0, x0 + 10, y1], radius=5, fill=story["color"])
        badge_cx, badge_cy = x0 + 52, y0 + 46
        d.ellipse([badge_cx - 24, badge_cy - 24, badge_cx + 24, badge_cy + 24],
                  fill=story["color"])
        d.text((badge_cx, badge_cy), str(i + 1), font=font("bold", 30),
               fill=(255, 255, 255), anchor="mm")
        # tag
        d.text((x0 + 92, y0 + 26), story["tag"], font=font("bold", 19),
               fill=story["color"])
        # headline, wrapped
        lines = textwrap.wrap(story["headline"], width=27)
        y = y0 + 80
        for line in lines[:3]:
            d.text((x0 + 30, y), line, font=font("bold", 25), fill=ink)
            y += 31
        # detail, wrapped (max 2 lines so nothing spills past the card)
        detail_lines = textwrap.wrap(story["detail"], width=42)
        y += 4
        for line in detail_lines[:2]:
            d.text((x0 + 30, y), line, font=font("regular", 20), fill=muted)
            y += 26

    # --- Footer ---
    fy = top + 3 * card_h + 2 * row_gap + 14
    d.line([margin, fy, W - margin, fy], fill=(200, 196, 188), width=2)
    d.text((margin, fy + 12),
           "Headlines: AFP / AP / Reuters, 22 Nov 2026.",
           font=font("regular", 19), fill=muted)
    d.text((margin, fy + 38),
           "Generated by code — run python3 main.py to reproduce.",
           font=font("regular", 19), fill=muted)
    d.text((W - margin, fy + 38), "make.fun · news-image-20261122",
           font=font("bold", 19), fill=ink, anchor="ra")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    img.save(out_path, "PNG")
    print("Wrote %s (%dx%d)" % (out_path, W, H))


if __name__ == "__main__":
    main()
