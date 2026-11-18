#!/usr/bin/env python3
"""Build the 1024x1024 front-page poster for 17 November 2026 world news.

All text is drawn with PIL (DejaVu) so every letter is crisp; the only
generated artwork is the hero photograph of the burning tanker, which
carries no text of its own. Output: entry.png, 1024x1024.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1024, 1024
HERO = "/home/hatch/workspace/makefun/entries-2026-11-18/news-image-20261117/assets/media-generation-hormuz-hero-0-ea9c8daa-d85f-4367-ac54-04cc43ded2be.webp"
OUT = "/home/hatch/workspace/makefun/entries-2026-11-18/news-image-20261117/repo/entry.png"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (20, 33, 61)
PAPER = (247, 243, 234)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 90, 88)
WHITE = (255, 255, 255)

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

canvas = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(canvas)

# ---- Masthead ----
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((W // 2, 16), "THE WORLD  •  ONE DAY IN THE NEWS",
       font=font(SANS_B, 21), fill=(212, 175, 105), anchor="ma")
d.text((W // 2, 44), "TUESDAY 17 NOVEMBER 2026",
       font=font(SERIF_B, 52), fill=WHITE, anchor="ma")

# ---- Hero photo ----
hero = Image.open(HERO).convert("RGB")
hw, hh = hero.size
target_ratio = 1024 / 352
src_ratio = hw / hh
if src_ratio > target_ratio:
    nw = int(hh * target_ratio)
    x0 = (hw - nw) // 2
    hero = hero.crop((x0, 0, x0 + nw, hh))
else:
    nh = int(hw / target_ratio)
    y0 = (hh - nh) // 2
    hero = hero.crop((0, y0, hw, y0 + nh))
hero = hero.resize((1024, 352), Image.LANCZOS)
canvas.paste(hero, (0, 118))
# bottom scrim for headline legibility
scrim = Image.new("RGBA", (1024, 170), (0, 0, 0, 0))
sd = ImageDraw.Draw(scrim)
for i in range(170):
    a = int(200 * (i / 170) ** 1.6)
    sd.line([(0, i), (1024, i)], fill=(0, 0, 0, a))
canvas.paste(Image.alpha_composite(canvas.crop((0, 300, 1024, 470)).convert("RGBA"), scrim),
             (0, 300))
d = ImageDraw.Draw(canvas)
d.text((28, 316), "U.S. STRIKES IRAN",
       font=font(SANS_B, 44), fill=WHITE)
d.text((28, 366), "Warplanes hit a missile site on Qeshm Island;",
       font=font(SANS_B, 27), fill=WHITE)
d.text((28, 398), "tanker Tara Gas burns in the Strait of Hormuz — 24 crew evacuated.",
       font=font(SANS, 24), fill=(235, 235, 235))
d.rectangle([0, 470, W, 478], fill=RED)

# ---- Story grid: 2 columns x 3 rows ----
stories = [
    ("UKRAINE", "Kerch Bridge hit again",
     "Road arch collapses into the strait after a Ukrainian drone and missile strike; Kyiv says it answers Russian attacks on its power grid."),
    ("ASIA", "Trump lands in Manila",
     "Quad summit opens his Asia trip; APEC in Shenzhen is next, with a planned three-way meeting with Xi Jinping and Vladimir Putin."),
    ("HEALTH", "U.S. loses measles-free status",
     "PAHO ends the designation held since 2000 after a year of uninterrupted transmission across the country."),
    ("TECH", "Nvidia beats forecasts",
     "Results top Wall Street estimates after the bell and shares rise about 4%, as the U.S. tightens AI-chip export rules."),
    ("JAPAN", "Japan scrambles jets",
     "Two suspected Russian aircraft enter airspace near Fukuoka; Tokyo lodges a strong protest."),
    ("GAZA", "Gaza shelters flooded",
     "The UN warns the shelter and food crisis is deepening, as Western states urge Israel to open aid crossings."),
]
col_x = [28, 532]
col_w = 464
row_y = [496, 656, 816]
row_h = 148
for i, (kicker, head, deck) in enumerate(stories):
    x = col_x[i % 2]
    y = row_y[i // 2]
    d.text((x, y), kicker, font=font(SANS_B, 17), fill=RED)
    d.text((x, y + 24), head, font=font(SANS_B, 25), fill=INK)
    lines = wrap(d, deck, font(SANS, 19), col_w)
    yy = y + 58
    for ln in lines[:3]:
        d.text((x, yy), ln, font=font(SANS, 19), fill=(60, 60, 60))
        yy += 25
    if i % 2 == 0:
        d.line([(512, y + 4), (512, y + row_h - 8)], fill=(210, 205, 190), width=2)
    if i // 2 < 2:
        d.line([(x, y + row_h + 2), (x + col_w, y + row_h + 2)], fill=(210, 205, 190), width=2)

# ---- Footer ----
d.rectangle([0, 978, W, H], fill=NAVY)
d.text((W // 2, 990), "All events of Tuesday 17 November 2026  •  Sources: Reuters, AP, PAHO, UN",
       font=font(SANS, 17), fill=(200, 205, 215), anchor="ma")

canvas.save(OUT, "PNG", optimize=True)
print("saved", OUT)
