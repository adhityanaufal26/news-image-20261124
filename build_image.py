#!/usr/bin/env python3
"""Build entry.png for news-image-20261124: Tuesday 24 November 2026 world news.

Draws a 1024x1024 newspaper front page with Pillow. Fully deterministic:
no timestamps, no randomness, fixed compile-time string. Run twice and the
bytes must be identical.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 233)
INK = (20, 24, 31)
NAVY = (14, 42, 71)
NAVY2 = (22, 58, 94)
GOLD = (200, 162, 74)
RED = (179, 38, 30)
TEAL = (14, 107, 107)
GREEN = (30, 122, 52)
GREY = (110, 112, 116)
SKY = (214, 232, 240)
SEA = (196, 222, 232)

FD = "/usr/share/fonts/truetype/dejavu/"
F_SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
F_SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")
F_SANS = os.path.join(FD, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill, leading=None, max_lines=None):
    lines = wrap(draw, text, fnt, max_w)
    if max_lines:
        lines = lines[:max_lines]
    lh = leading or int(fnt.size * 1.28)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def rrect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 86], fill=NAVY)
d.rectangle([0, 86, W, 90], fill=GOLD)
d.text((18, 12), "T H E   W O R L D   I N   O N E   I M A G E", font=font(F_SANS_B, 13), fill=GOLD)
d.text((18, 30), "Tuesday 24 November 2026", font=font(F_SERIF_B, 40), fill=(255, 255, 255))
d.text((700, 16), "Compiled 02:45 UTC", font=font(F_SANS_B, 13), fill=(255, 255, 255))
d.text((700, 34), "Tuesday 24 November 2026", font=font(F_SANS, 13), fill=(190, 200, 214))
d.text((700, 52), "All times UTC unless stated", font=font(F_SANS, 12), fill=(150, 164, 184))
d.text((18, 72), "The day's world news, drawn as one front page  |  $100 prize  |  Top 50 paid",
       font=font(F_SANS, 11), fill=(150, 164, 184))


def section_label(y, text):
    d.text((18, y), text, font=font(F_SANS_B, 14), fill=NAVY)
    d.line([(18, y + 22), (1006, y + 22)], fill=GOLD, width=2)


# ------------------------------------------------------- leads: y 98 – 430
section_label(98, "THE DAY'S THREE BIG STORIES")
LEADS = [
    dict(tag="TECH  ·  MON 23 NOV", tag_bg=GREEN,
         head="Huang is back at Nvidia — shares soar 31%",
         body=("Nvidia's board unanimously reinstates Jensen Huang as chief "
               "executive, 11 days after he resigned. Shares jump 31% in a "
               "day as markets cheer; Trump says he pressed the board himself."),
         art="chip"),
    dict(tag="SECURITY  ·  TUE 24 NOV", tag_bg=RED,
         head="Russian jets set off island alert in South Korea",
         body=("Jets scrambled after Russian military planes enter Korea's air "
               "defence zone near Ulleung Island. A shelter warning sounds at "
               "07:52 and is lifted three minutes later; no airspace breach."),
         art="jets"),
    dict(tag="CLIMATE  ·  SUN 22 NOV", tag_bg=TEAL,
         head="COP31 collapses — no climate deal in Antalya",
         body=("The longest climate talks ever end with no overarching deal "
              "after the EU rejects a pact that omits fossil fuels. Pacific "
              "nations voice despair and vow to go it alone."),
         art="globe"),
]
LX, LY, LW, LG = 18, 126, 322, 11
for i, lead in enumerate(LEADS):
    x = LX + i * (LW + LG)
    d.rectangle([x, LY, x + LW, LY + 150], fill=NAVY2 if lead["art"] != "globe" else (16, 74, 74))
    if lead["art"] == "chip":
        for cx in range(x + 14, x + LW - 10, 26):
            d.line([(cx, LY + 8), (cx, LY + 142)], fill=(38, 84, 128), width=1)
        for cy in range(LY + 14, LY + 142, 26):
            d.line([(x + 8, cy), (x + LW - 8, cy)], fill=(38, 84, 128), width=1)
        cx0, cy0 = x + 24, LY + 22
        d.rectangle([cx0, cy0, cx0 + 150, cy0 + 84], fill=(20, 40, 30), outline=GOLD, width=3)
        for px in range(cx0 + 14, cx0 + 140, 18):
            d.line([(px, cy0 - 9), (px, cy0)], fill=GOLD, width=3)
            d.line([(px, cy0 + 84), (px, cy0 + 93)], fill=GOLD, width=3)
        d.text((cx0 + 34, cy0 + 12), "NVDA", font=font(F_SANS_B, 30), fill=(255, 255, 255))
        d.text((cx0 + 42, cy0 + 50), "AI CHIP", font=font(F_SANS_B, 15), fill=GOLD)
        d.line([(x + 196, LY + 134), (x + 240, LY + 108), (x + 272, LY + 116), (x + 308, LY + 88)],
               fill=(74, 222, 128), width=5)
        d.polygon([(x + 308, LY + 88), (x + 290, LY + 86), (x + 304, LY + 106)], fill=(74, 222, 128))
        d.text((x + 196, LY + 62), "+31%", font=font(F_SANS_B, 26), fill=(74, 222, 128))
    elif lead["art"] == "jets":
        d.rectangle([x, LY, x + LW, LY + 150], fill=SKY)
        d.rectangle([x, LY + 104, x + LW, LY + 150], fill=(64, 120, 150))
        for r in (16, 30, 44):
            d.ellipse([x + LW - 72 - r, LY + 12 - r, x + LW - 72 + r, LY + 12 + r],
                      outline=(255, 255, 255), width=2)
        d.polygon([(x + 60, LY + 114), (x + 110, LY + 82), (x + 170, LY + 94),
                   (x + 210, LY + 114), (x + 150, LY + 128)], fill=(52, 130, 80))
        d.polygon([(x + 118, LY + 86), (x + 132, LY + 64), (x + 146, LY + 86)], fill=(52, 130, 80))
        for jx, jy in ((x + 40, LY + 32), (x + 120, LY + 16)):
            d.polygon([(jx, jy), (jx + 46, jy + 8), (jx + 58, jy + 4), (jx + 46, jy + 14),
                       (jx + 10, jy + 12)], fill=(40, 44, 52))
            d.polygon([(jx + 12, jy + 2), (jx + 22, jy - 8), (jx + 28, jy + 2)], fill=(40, 44, 52))
        tx, ty = x + LW - 62, LY + 92
        d.polygon([(tx, ty), (tx + 52, ty), (tx + 26, ty + 46)], fill=(255, 196, 0),
                  outline=RED, width=3)
        d.text((tx + 19, ty + 10), "!", font=font(F_SANS_B, 26), fill=RED)
        d.text((x + 14, LY + 124), "07:52  SHELTER WARNING", font=font(F_SANS_B, 13), fill=(255, 255, 255))
    else:  # globe
        gx, gy, gr = x + LW // 2, LY + 78, 58
        d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(46, 130, 160), outline=(255, 255, 255), width=3)
        d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 200, 330, fill=(52, 130, 80), width=15)
        d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 20, 110, fill=(52, 130, 80), width=11)
        d.line([(gx - 8, gy - 54), (gx + 6, gy - 28), (gx - 6, gy - 4), (gx + 10, gy + 20),
                (gx - 2, gy + 44), (gx + 8, gy + 56)], fill=(255, 255, 255), width=4)
        d.text((x + 16, LY + 8), "ANTALYA, TURKEY", font=font(F_SANS_B, 13), fill=(255, 255, 255))
        d.rectangle([x + 16, LY + 116, x + LW - 16, LY + 142], fill=RED)
        d.text((x + 30, LY + 121), "NO DEAL", font=font(F_SANS_B, 19), fill=(255, 255, 255))
    ty = LY + 158
    tag = lead["tag"]
    tw = d.textlength(tag, font=font(F_SANS_B, 11)) + 16
    rrect(d, [x, ty, x + tw, ty + 20], 10, fill=lead["tag_bg"])
    d.text((x + 8, ty + 4), tag, font=font(F_SANS_B, 11), fill=(255, 255, 255))
    hy = draw_wrapped(d, x, ty + 26, lead["head"], font(F_SANS_B, 19), LW, INK, leading=22, max_lines=2)
    draw_wrapped(d, x, hy + 4, lead["body"], font(F_SANS, 13), LW, (52, 56, 64), leading=16, max_lines=4)

# -------------------------------------------------------- map strip: 436–584
section_label(436, "WHERE IT HAPPENED")
MX0, MY0, MW, MH = 18, 464, 988, 92
d.rectangle([MX0, MY0, MX0 + MW, MY0 + MH], fill=SEA)


def mxy(lon, lat):
    return (MX0 + (lon + 180) / 360.0 * MW, MY0 + (80 - lat) / 140.0 * MH)


CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70), (-75, 62),
     (-60, 55), (-55, 47), (-65, 45), (-75, 38), (-80, 32), (-90, 21), (-97, 16),
     (-105, 20), (-115, 28), (-125, 40), (-125, 49), (-140, 60), (-158, 58)],
    [(-58, 64), (-45, 60), (-30, 68), (-22, 70), (-35, 76), (-55, 74)],
    [(-80, 10), (-75, 12), (-62, 10), (-52, 5), (-35, -6), (-40, -20), (-48, -28),
     (-58, -35), (-65, -45), (-70, -54), (-73, -40), (-72, -20), (-80, -5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59), (18, 56),
     (21, 55), (28, 60), (30, 62), (25, 65), (20, 70), (15, 68), (10, 64), (5, 60),
     (-5, 58), (-10, 50)],
    [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32), (32, 31), (35, 28), (43, 12),
     (51, 11), (48, 0), (40, -15), (35, -25), (28, -33), (20, -35), (15, -27),
     (12, -18), (9, -1), (9, 4), (-8, 5)],
    [(30, 62), (40, 68), (55, 70), (70, 72), (90, 75), (110, 76), (130, 72), (160, 70),
     (178, 66), (170, 60), (160, 55), (142, 50), (140, 40), (130, 35), (127, 35),
     (120, 30), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (80, 10),
     (77, 8), (72, 20), (66, 25), (60, 25), (55, 26), (50, 29), (48, 30), (43, 12),
     (40, 20), (35, 28), (30, 36)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32), (137, -35), (140, -38),
     (147, -39), (150, -37), (153, -27), (146, -19), (142, -11), (135, -12), (130, -13),
     (126, -14), (122, -17)],
]
for poly in CONTINENTS:
    d.polygon([mxy(lon, lat) for lon, lat in poly], fill=(226, 220, 198),
              outline=(160, 152, 132))
PINS = [
    (1, 127, 37), (2, 32, 36), (3, 20, 32), (4, 34, 31),
    (5, -122, 37), (6, 116, 40), (7, -99, 19), (8, 178, -18),
]
for num, lon, lat in PINS:
    px, py = mxy(lon, lat)
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=(255, 255, 255), width=2)
    d.text((px - 3, py - 7), str(num), font=font(F_SANS_B, 11), fill=(255, 255, 255))
d.text((18, 562),
       "1  Ulleung Island, Korea    2  Antalya, Turkey    3  Benghazi, Libya    4  Gaza    "
       "5  Santa Clara, USA    6  Beijing    7  Mexico City    8  Fiji",
       font=font(F_SANS_B, 12), fill=NAVY)

# ----------------------------------------------------- numbers strip: 592–700
section_label(592, "THE DAY IN NUMBERS")
NUMS = [
    ("+31%", "Nvidia shares rise\nin one day (Mon)"),
    ("3 min", "South Korea's island\nshelter warning lasts"),
    ("14", "killed in Russian\nstrikes on Kyiv region"),
    ("5 days", "Fiji schools to close\nas drought deepens"),
    ("12,000", "evacuated at a\nconcert in England"),
]
NX, NY, NW = 18, 622, 192
for i, (big, small) in enumerate(NUMS):
    x = NX + i * (NW + 8)
    rrect(d, [x, NY, x + NW, NY + 74], 8, fill=(255, 255, 255), outline=(200, 192, 172), width=1)
    d.text((x + 12, NY + 7), big, font=font(F_SANS_B, 26), fill=RED if i == 0 else NAVY)
    for j, ln in enumerate(small.split("\n")):
        d.text((x + 12, NY + 40 + j * 15), ln, font=font(F_SANS, 12), fill=(52, 56, 64))

# --------------------------------------------------------- mid cards: 710–906
section_label(710, "MORE OF THE DAY")
MIDS = [
    ("WAR AT SEA  ·  SUN–MON",
     "Ukraine sinks Russian corvette in Libya",
     "Kyiv says maritime drones sank the Merkury in Benghazi port — the war now reaches the Med."),
    ("GAZA  ·  MON–TUE",
     "Strikes kill 3; four nations demand aid access",
     "Israeli strikes kill three, including a UN aid worker. Four nations urge Israel to open Gaza to aid."),
    ("IRAN  ·  MON",
     "Singer flogged 74 times; US hits shadow banks",
     "An Iranian singer and four crew get 74 lashes each. The US sanctions 24 targets in Iran's shadow banks."),
    ("CHINA  ·  TUE",
     "Official sentenced to death for leaking secrets",
     "A state official is sentenced to death for passing secrets abroad — 100 reports, 35 of them secret."),
    ("MEXICO  ·  MON",
     "Drug lord 'Chapo Isidro' captured",
     "Elite soldiers seize Fausto Isidro Meza Flores, one of Mexico's most wanted, with US intelligence help."),
    ("MARKETS  ·  TUE",
     "Gold jumps to $3,670; Bitcoin tops $63,000",
     "Safe-haven gold surges nearly 4% as the AI trade wobbles; Bitcoin bounces back above $63,000."),
]
CX, CY, CW, CH, CG = 18, 740, 322, 80, 11
for i, (tag, head, body) in enumerate(MIDS):
    x = CX + (i % 3) * (CW + CG)
    y = CY + (i // 3) * (CH + 8)
    rrect(d, [x, y, x + CW, y + CH], 8, fill=(255, 255, 255), outline=(200, 192, 172), width=1)
    d.text((x + 12, y + 7), tag, font=font(F_SANS_B, 10), fill=RED)
    hy = draw_wrapped(d, x + 12, y + 22, head, font(F_SANS_B, 13), CW - 24, INK, leading=15, max_lines=1)
    draw_wrapped(d, x + 12, hy + 1, body, font(F_SANS, 11), CW - 24, (52, 56, 64), leading=13, max_lines=2)

# ----------------------------------------------------- also today: 916 – 1000
section_label(916, "ALSO TODAY  ·  OVERNIGHT")
BRIEFS_L = [
    "•  NATO to send AWACS jets to Poland after Russian missiles land (Mon)",
    "•  Murmansk governor detained on embezzlement charges (Tue)",
    "•  North Korea mulls closing Swiss office after sanctions row (Tue)",
    "•  UN chief: build a global AI safety framework within a year (Tue)",
]
BRIEFS_R = [
    "•  Trump halts Army detonation of toxic lead-azide stockpile in Iowa (Mon)",
    "•  Chicago O'Hare ground stop amid Thanksgiving travel rush (Mon)",
    "•  US seeks $1.1bn in crypto from North Korea-linked Binance hack (Mon)",
    "•  Oracle secures funding for its $300bn OpenAI computing deal (Mon)",
]
by = 946
for ln in BRIEFS_L:
    d.text((18, by), ln, font=font(F_SANS, 12), fill=(30, 34, 42))
    by += 15
by = 946
for ln in BRIEFS_R:
    d.text((522, by), ln, font=font(F_SANS, 12), fill=(30, 34, 42))
    by += 15

# ------------------------------------------------------------------- footer
d.line([(18, 1008), (1006, 1008)], fill=GOLD, width=2)
d.text((18, 1012),
       "DATE CHECK — compiled 02:45 UTC Tue 24 Nov 2026 · Sources: Reuters, CNN, AP, Korea JoongAng Daily, PINA, Investopedia, Times of India",
       font=font(F_SANS_B, 10), fill=NAVY)

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
