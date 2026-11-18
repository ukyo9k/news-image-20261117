#!/usr/bin/env python3
"""Build v2 of the 1024x1024 front-page poster for 17 November 2026 world news.

Denser broadsheet: masthead with story count, hero lead, three top stories
with small schematic panels drawn in code, a six-story grid, and a compact
'ALSO ON TUESDAY 17 NOVEMBER' list in three columns — 22 verified stories
across 6 continents. All text is drawn with PIL (DejaVu) so every letter is
crisp; the only generated artwork is the hero photograph of the burning
tanker, which carries no text of its own. Output: entry.png, 1024x1024.

Layout budget (heights add up, no overlap): masthead 104, hero 180,
top-3 strip ~180, grid 3 rows x 78, also-on header + 4 rows x 40, footer 46.
"""
from PIL import Image, ImageDraw, ImageFont

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
GREY = (88, 88, 86)
WHITE = (255, 255, 255)
GOLD = (212, 175, 105)
RULE = (210, 205, 190)
PURPLE = (88, 58, 138)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for w in text.split():
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


def draw_wrapped(draw, x, y, text, fnt, max_w, fill, max_lines, leading):
    yy = y
    for ln in wrap(draw, text, fnt, max_w)[:max_lines]:
        draw.text((x, yy), ln, font=fnt, fill=fill)
        yy += leading
    return yy


canvas = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(canvas)

# ---- Masthead (0-104) ----
d.rectangle([0, 0, W, 104], fill=NAVY)
d.text((W // 2, 8), "THE WORLD'S NEWS IN ONE PICTURE",
       font=font(SANS_B, 18), fill=GOLD, anchor="ma")
d.text((W // 2, 30), "Tuesday 17 November 2026",
       font=font(SERIF_B, 48), fill=WHITE, anchor="ma")
d.text((W // 2, 82), "22 STORIES  •  6 CONTINENTS  •  ALL FROM TUESDAY",
       font=font(SANS_B, 14), fill=GOLD, anchor="ma")

# ---- Hero photo (104-284) ----
hero = Image.open(HERO).convert("RGB")
hw, hh = hero.size
target_ratio = 1024 / 180
src_ratio = hw / hh
if src_ratio > target_ratio:
    nw = int(hh * target_ratio)
    x0 = (hw - nw) // 2
    hero = hero.crop((x0, 0, x0 + nw, hh))
else:
    nh = int(hw / target_ratio)
    y0 = (hh - nh) // 2
    hero = hero.crop((0, y0, hw, y0 + nh))
hero = hero.resize((1024, 180), Image.LANCZOS)
canvas.paste(hero, (0, 104))
scrim = Image.new("RGBA", (1024, 96), (0, 0, 0, 0))
sd = ImageDraw.Draw(scrim)
for i in range(96):
    a = int(205 * (i / 96) ** 1.6)
    sd.line([(0, i), (1024, i)], fill=(0, 0, 0, a))
canvas.paste(Image.alpha_composite(canvas.crop((0, 188, 1024, 284)).convert("RGBA"), scrim),
             (0, 188))
d = ImageDraw.Draw(canvas)
d.text((28, 190), "U.S. STRIKES IRAN",
       font=font(SANS_B, 36), fill=WHITE)
d.text((28, 232), "Warplanes hit a missile site on Qeshm Island; tanker Tara Gas",
       font=font(SANS_B, 21), fill=WHITE)
d.text((28, 257), "burns in the Strait of Hormuz — 24 crew evacuated.",
       font=font(SANS, 19), fill=(235, 235, 235))
d.rectangle([0, 284, W, 290], fill=RED)

# ---- Top 3 stories with schematic panels (300-470) ----
top_x = [28, 356, 684]
top_w = 312
py = 300

# Panel A: Kerch bridge, broken span
px = top_x[0]
d.rectangle([px, py, px + top_w, py + 56], fill=(178, 205, 224))
d.rectangle([px, py + 34, px + top_w, py + 56], fill=(96, 140, 175))
d.polygon([(px, py + 34), (px + 70, py + 8), (px + 150, py + 34)], fill=(214, 205, 178))
d.polygon([(px + top_w, py + 34), (px + top_w - 60, py + 10), (px + 170, py + 34)], fill=(214, 205, 178))
d.rectangle([px, py + 27, px + 128, py + 33], fill=(90, 90, 90))
d.rectangle([px + 184, py + 27, px + top_w, py + 33], fill=(90, 90, 90))
d.polygon([(px + 140, py + 31), (px + 156, py + 48), (px + 172, py + 31)], fill=(70, 70, 70))
for cx, cy in [(px + 150, py + 16), (px + 168, py + 10)]:
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(255, 120, 0))
d.text((px + 6, py + 40), "CRIMEA", font=font(SANS_B, 10), fill=WHITE)
d.text((px + top_w - 52, py + 40), "RUSSIA", font=font(SANS_B, 10), fill=WHITE)

# Panel B: Strait of Hormuz schematic
px = top_x[1]
d.rectangle([px, py, px + top_w, py + 56], fill=(150, 190, 215))
d.polygon([(px, py), (px + 200, py), (px + 150, py + 24), (px, py + 20)], fill=(216, 200, 158))
d.polygon([(px, py + 56), (px + 120, py + 56), (px + 90, py + 36), (px, py + 40)], fill=(216, 200, 158))
d.text((px + 8, py + 3), "IRAN", font=font(SANS_B, 10), fill=(90, 70, 40))
d.text((px + 8, py + 42), "OMAN", font=font(SANS_B, 10), fill=(90, 70, 40))
for i in range(0, 9):
    x0 = px + 130 + i * 18
    d.line([(x0, py + 31), (x0 + 10, py + 31)], fill=RED, width=2)
d.rectangle([px + 218, py + 23, px + 252, py + 33], fill=(40, 40, 40))
d.line([(px + 232, py + 23), (px + 232, py + 15)], fill=(40, 40, 40), width=2)
d.ellipse([px + 258, py + 19, px + 270, py + 31], fill=RED)
d.text((px + 246, py + 35), "QESHM", font=font(SANS_B, 10), fill=RED)

# Panel C: Quad summit flags
px = top_x[2]
d.rectangle([px, py, px + top_w, py + 56], fill=(235, 232, 240))
d.rectangle([px, py, px + top_w, py + 19], fill=PURPLE)
d.text((px + top_w // 2, py + 2), "QUAD LEADERS' SUMMIT • MANILA",
       font=font(SANS_B, 12), fill=WHITE, anchor="ma")
flag_w, flag_h, gap = 64, 26, 14
fx = px + 8
for kind, label in [("us", "US"), ("in", "INDIA"), ("jp", "JAPAN"), ("au", "AUSTRALIA")]:
    if kind == "us":
        for s in range(4):
            d.rectangle([fx, py + 22 + s * 7, fx + flag_w, py + 22 + s * 7 + 4],
                        fill=RED if s % 2 == 0 else WHITE)
        d.rectangle([fx, py + 22, fx + 26, py + 22 + 14], fill=(40, 60, 130))
    elif kind == "in":
        d.rectangle([fx, py + 22, fx + flag_w, py + 22 + 9], fill=(255, 153, 51))
        d.rectangle([fx, py + 22 + 9, fx + flag_w, py + 22 + 18], fill=WHITE)
        d.rectangle([fx, py + 22 + 18, fx + flag_w, py + 22 + 27], fill=(19, 136, 8))
    elif kind == "jp":
        d.rectangle([fx, py + 22, fx + flag_w, py + 22 + 27], fill=WHITE)
        d.ellipse([fx + 24, py + 27, fx + 40, py + 43], fill=RED)
    else:
        d.rectangle([fx, py + 22, fx + flag_w, py + 22 + 27], fill=(0, 40, 120))
        d.ellipse([fx + 8, py + 26, fx + 14, py + 32], fill=WHITE)
        d.ellipse([fx + 48, py + 26, fx + 54, py + 32], fill=WHITE)
        d.ellipse([fx + 28, py + 38, fx + 34, py + 44], fill=WHITE)
    d.text((fx + flag_w // 2, py + 50), label,
           font=font(SANS_B, 8), fill=INK, anchor="ma")
    fx += flag_w + gap

top_stories = [
    ("EUROPE • UKRAINE WAR", "Crimean Bridge road span falls into the sea",
     "Second strike in two days; Kyiv says it answers attacks on its power grid."),
    ("MIDDLE EAST • IRAN WAR", "Iran sends drones at a US radar in Bahrain",
     "Bahrain and the US say all were downed; US jets then strike Qeshm."),
    ("ASIA • DIPLOMACY", "Trump holds first Quad summit in Manila",
     "Four unveil minerals deals; Putin heads to Shenzhen for talks with Trump and Xi."),
]
for i, (kicker, head, deck) in enumerate(top_stories):
    x = top_x[i]
    y = py + 64
    d.text((x, y), kicker, font=font(SANS_B, 12), fill=RED)
    y = draw_wrapped(d, x, y + 17, head, font(SANS_B, 21), top_w, INK, 2, 25)
    draw_wrapped(d, x, y + 2, deck, font(SANS, 14), top_w, (60, 60, 60), 2, 18)
    if i < 2:
        d.line([(x + top_w + 8, py + 4), (x + top_w + 8, py + 166)],
               fill=RULE, width=2)
d.line([(28, 478), (996, 478)], fill=RULE, width=2)

# ---- Grid: 6 stories, 2 cols x 3 rows, pitch 78 (488-722) ----
grid = [
    ("AFRICA • HEALTH", "Ebola cases pass 11,000 in DR Congo",
     "WHO: about 5,400 dead; cases doubled in three months."),
    ("GLOBAL • CLIMATE", "COP31 split over fossil fuels",
     "Nations weigh the draft; EU urges a clean-energy signal."),
    ("AMERICAS • HEALTH", "US loses measles-free status",
     "PAHO ends the status held since 2000; a year of spread."),
    ("US • BUSINESS", "Nvidia tops forecasts again",
     "Record revenue after the bell; shares rise about 4%."),
    ("MIDDLE EAST • GAZA", "Gaza truce at risk, UN told",
     "Board of Peace warns truce could fail; rains flood shelters."),
    ("ASIA • POLITICS", "Mongolia leader says he will quit",
     "Khurelsukh denies $25m bribe claim; MPs must accept it."),
]
col_x = [28, 532]
col_w = 464
row_y = [490, 568, 646]
for i, (kicker, head, deck) in enumerate(grid):
    x = col_x[i % 2]
    y = row_y[i // 2]
    d.text((x, y), kicker, font=font(SANS_B, 13), fill=RED)
    d.text((x, y + 17), head, font=font(SANS_B, 20), fill=INK)
    draw_wrapped(d, x, y + 42, deck, font(SANS, 15), col_w, (60, 60, 60), 2, 19)
    if i % 2 == 0:
        d.line([(512, y + 2), (512, y + 70)], fill=RULE, width=2)
    if i // 2 < 2:
        d.line([(x, y + 74), (x + col_w, y + 74)], fill=RULE, width=2)

# ---- Also on Tuesday 17 November (736-962), 3 cols x 4 rows ----
d.text((28, 736), "ALSO ON TUESDAY 17 NOVEMBER",
       font=font(SANS_B, 16), fill=RED)
d.line([(28, 758), (996, 758)], fill=RED, width=2)
also = [
    ("Serbia", "Student List sworn in, 140 of 250 seats."),
    ("Bangladesh", "Police tear-gas garment workers."),
    ("An-12 crash", "All 19 aboard killed in Siberia."),
    ("Mozambique", "Mondlane on trial; faces 24 years."),
    ("Moldova", "Airspace shut as drones fly over capital."),
    ("Japan", "Jets scrambled near Fukuoka."),
    ("Prague", "Two trains collide; 46 hurt."),
    ("Quake", "M6.6 off Indonesia felt in Darwin."),
    ("Yemen", "Houthis advance toward Aden."),
    ("Depardieu", "Admits sex-assault charge."),
    ("Apple", "iCloud and App Store outage."),
    ("Israel", "Eisenkot ally elected Knesset speaker."),
]
col3_x = [28, 356, 684]
col3_w = 300
for i, (lead, text) in enumerate(also):
    col = i // 4
    row = i % 4
    x = col3_x[col]
    yy = 770 + row * 48
    d.ellipse([x, yy + 2, x + 17, yy + 19], fill=RED)
    d.text((x + 8, yy + 1), str(i + 1), font=font(SANS_B, 12),
           fill=WHITE, anchor="ma")
    draw_wrapped(d, x + 24, yy, lead + ": " + text,
                 font(SANS, 15), col3_w - 24, INK, 2, 19)

# ---- Footer (978-1024) ----
d.rectangle([0, 978, W, H], fill=NAVY)
d.text((W // 2, 990),
       "Every story here happened or was first reported on Tuesday 17 November 2026  •  Sources: Reuters, AP, PAHO, WHO, UN",
       font=font(SANS, 15), fill=(200, 205, 215), anchor="ma")

canvas.save(OUT, "PNG", optimize=True)
print("saved", OUT)
