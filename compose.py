#!/usr/bin/env python3
"""THE DAY'S LEDGER - NI23 G4 akun7 compose. PIL local only.
Cream paper, forest-green ink, copper accents. Flat original drawings.
Map style: dotted_map (dots mark land, numbered pins mark story numbers)."""
import sys
from PIL import Image, ImageDraw, ImageFont

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)
PB = lambda s: F("PlayfairDisplay-Black.ttf", s)
PBD = lambda s: F("PlayfairDisplay-Bold.ttf", s)
AB = lambda s: F("Archivo-Bold.ttf", s)
AR = lambda s: F("Archivo.ttf", s)
def fb(n):
    return PBD(n)
def fr(n):
    return AR(n)
def fsr(n):
    return AR(n)

CREAM = (247, 240, 220); PAPER = (252, 247, 232); INK = (27, 67, 50)
INK2 = (20, 52, 38); COPPER = (184, 115, 51); RED = (165, 40, 32)
GREY = (90, 90, 82)
REGIONS = {
 "MIDDLE EAST": (184, 115, 51), "GLOBAL": (90, 130, 90), "EUROPE": (70, 100, 160),
 "NORTH AMERICA": (150, 60, 60), "ASIA-PACIFIC": (40, 130, 130), "SOUTH ASIA": (190, 150, 40),
 "AFRICA": (140, 90, 160), "SOUTHEAST ASIA": (60, 160, 110),
}
MAP_SRC = "dotted_map"
# num, region, loc, status, category, title(head), deck, source, icon(kind)
CARDS = [
 (1,"GLOBAL","UNITED NATIONS","OFFICIAL","GLOBAL - AI","UN Talks on Killer AI Go On","Member nations agree in Geneva to keep negotiating rules for lethal AI weapons systems.","SalonVision wire, 23 Nov","globe"),
 (2,"MIDDLE EAST","STRAIT OF HORMUZ","REPORTED","MIDDLE EAST - WAR","Tanker Set Burning in Hormuz","A tanker burns in the Strait as the Iran-US war widens into the Gulf at Hormuz.","AP live, 23 Nov","ship"),
 (3,"EUROPE","ANTALYA, TURKIYE","OFFICIAL","EUROPE - CLIMATE","COP31 Ends With No Deal","The final Turkiye draft in Antalya omits 'fossil fuels' after days of COP31 talks.","BBC / AP, 23 Nov","leaf"),
 (4,"MIDDLE EAST","BAHRAIN","CLAIM","MIDDLE EAST - WAR","IRGC Claims Patriot Radars Hit","Iran's IRGC claims 2 Patriot radars destroyed at a US base in Bahrain.","AP / AFP wires","radar"),
 (5,"NORTH AMERICA","WASHINGTON","OFFICIAL","N. AMERICA - POLITICS","Democrats' Majority Confirmed 258-173","The largest House majority since 1992, confirmed for Democrats in Washington.","BBC, 23 Nov","flag"),
 (6,"EUROPE","KYIV, UKRAINE","REPORTED","EUROPE - WAR","Boy, 7, Pulled Alive From Rubble","Freed after hours in Kyiv rubble; 6 killed in the Russian strike on Ukraine.","BBC, 23 Nov","house"),
 (7,"EUROPE","KYIV REGION","ON RECORD","EUROPE - WAR","14 Missing in Kyiv, Zelenskiy Says","14 missing after a Russian drone hit a Kyiv block, Zelenskiy tells Ukraine.","JagranJosh, 23 Nov","house"),
 (8,"EUROPE","GULF OF FINLAND","ONGOING","EUROPE - SEA","Russian Cargo Ship Still Burns","The ship still burns off Finland hours after the attack in the Gulf of Finland.","BBC, 23 Nov","ship"),
 (9,"AFRICA","BENGHAZI, LIBYA","REPORTED","AFRICA - SEA","Blast on Russian Ship: Suspected Drone","A blast in Benghazi port on a Russian ship; a suspected drone strike in Libya.","BBC, 23 Nov","ship"),
 (10,"SOUTHEAST ASIA","THE HAGUE","OFFICIAL","ASIA - LAW","ICJ: Myanmar Guilty of Genocide","The 2017 campaign in Myanmar; 700,000+ Rohingya fled to Bangladesh.","Guardian / NYT wires","scale"),
 (11,"SOUTH ASIA","WELLINGTON, NZ","REPORTED","SOUTH ASIA - SPORT","India Pile Up Record 720/9 Declared","The highest Test total in New Zealand: 720 for 9 declared at Wellington.","ObserverVoice, 23 Nov","ball"),
 (12,"GLOBAL","WORLD MARKETS","REPORTED","GLOBAL - MONEY","Gold Slides to $3,538 an Ounce","Gold down $2,000+ from the 2026 record of $5,595 an ounce in world markets.","ObserverVoice, 23 Nov","coin"),
 (13,"NORTH AMERICA","WASHINGTON","REPORTED","N. AMERICA - LAW","FBI Probes Hack of Justice Database","The Bureau probes a suspected hack of its criminal database in Washington.","AP wire, 23 Nov","shield"),
]
# checker grid: (num, region, topic, src, head, deck, kind)
grid = [
 (1, "GLOBAL", "AI talks", "SalonVision wire, 23 Nov", "UN Talks on Killer AI Go On", "Member nations agree in Geneva to keep negotiating rules for lethal AI weapons systems.", "globe"),
 (2, "MIDDLE EAST", "Hormuz tanker", "AP live, 23 Nov", "Tanker Set Burning in Hormuz", "A tanker burns in the Strait as the Iran-US war widens into the Gulf at Hormuz.", "ship"),
 (3, "EUROPE", "COP31 climate", "BBC / AP, 23 Nov", "COP31 Ends With No Deal", "The final Turkiye draft in Antalya omits 'fossil fuels' after days of COP31 talks.", "leaf"),
 (4, "MIDDLE EAST", "Patriot claim", "AP / AFP wires", "IRGC Claims Patriot Radars Hit", "Iran's IRGC claims 2 Patriot radars destroyed at a US base in Bahrain.", "radar"),
 (5, "NORTH AMERICA", "House majority", "BBC, 23 Nov", "Democrats' Majority Confirmed 258-173", "The largest House majority since 1992, confirmed for Democrats in Washington.", "flag"),
 (6, "EUROPE", "Kyiv rescue", "BBC, 23 Nov", "Boy, 7, Pulled Alive From Rubble", "Freed after hours in Kyiv rubble; 6 killed in the Russian strike on Ukraine.", "house"),
 (7, "EUROPE", "Kyiv missing", "JagranJosh, 23 Nov", "14 Missing in Kyiv, Zelenskiy Says", "14 missing after a Russian drone hit a Kyiv block, Zelenskiy tells Ukraine.", "house"),
 (8, "EUROPE", "Finland ship fire", "BBC, 23 Nov", "Russian Cargo Ship Still Burns", "The ship still burns off Finland hours after the attack in the Gulf of Finland.", "ship"),
 (9, "AFRICA", "Benghazi blast", "BBC, 23 Nov", "Blast on Russian Ship: Suspected Drone", "A blast in Benghazi port on a Russian ship; a suspected drone strike in Libya.", "ship"),
 (10, "SOUTHEAST ASIA", "ICJ Myanmar", "Guardian / NYT wires", "ICJ: Myanmar Guilty of Genocide", "The 2017 campaign in Myanmar; 700,000+ Rohingya fled to Bangladesh.", "scale"),
 (11, "SOUTH ASIA", "India record", "ObserverVoice, 23 Nov", "India Pile Up Record 720/9 Declared", "The highest Test total in New Zealand: 720 for 9 declared at Wellington.", "ball"),
 (12, "GLOBAL", "Gold slide", "ObserverVoice, 23 Nov", "Gold Slides to $3,538 an Ounce", "Gold down $2,000+ from the 2026 record of $5,595 an ounce in world markets.", "coin"),
 (13, "NORTH AMERICA", "FBI hack probe", "AP wire, 23 Nov", "FBI Probes Hack of Justice Database", "The Bureau probes a suspected hack of its criminal database in Washington.", "shield"),
]
NUMS = [("258-173", "Democrats House win, card 5"), ("720/9d", "India record total, card 11"),
 ("14", "missing in Kyiv, card 7"), ("6", "killed in Kyiv, card 6"),
 ("$3,538", "gold per ounce, card 12"), ("700,000+", "Rohingya fled, card 10")]
TL = [("00:02Z", "UN AI talks begin"), ("02:00Z", "Albanese on COP31"), ("Morning", "Kyiv boy rescued"),
 ("Midday", "Hormuz tanker burns"), ("Afternoon", "House 258-173 confirmed"), ("Evening", "Alcaraz wins ATP title")]
BRIEFS_L = [
 "3 Houthi missile on W. Saudi Arabia intercepted - AFP",
 "10 Russia-bound ship towed after Gulf of Finland attack",
 "14 UK-EU Brexit reset: Burnham calls it a 'landmark'",
 "15 Thousands march in Lisbon over the cost of living",
 "16 Myanmar junta calls ASEAN decision 'unfair'",
 "19 Nepal PM Shah holds bilateral talks with PM Modi",
 "21 Guru Nanak Jayanti: 'Sewa, Simran aur Sangat'",
 "23 UPDATE ONLY: 7 body bags found, 50 still missing, Indonesia",
 "26 Test day 5: India chase a famous win (NZ 119/2)",
 "27 India win ODI series in NZ 3-2; Phillips top player",
 "28 Anupama retains IBSF world women's snooker title",
 "29 World Chess Championship captivates the fans",
 "31 Pilgrim bus tragedy in Kota, Rajasthan: 9 dead",
 "32 Tata Steel sells pipe unit for Rs28,000 crore",
]
BRIEFS_R = [
 "33 Pilots seek SpiceJet audit; IndiGo holds 65.9%",
 "35 IFFI 2026 hosts BRICS roundtable in Goa",
 "36 Modi opens AI centre at IIT Patna, Rs400 crore",
 "38 Chief Justice: AI rules mandatory in law study",
 "39 JEE Main 2027 session 1 registration closes today",
 "42 India-EU free trade pact likely signed 16 Dec",
 "44 Trump criticises Schumer amid Democrat push",
 "45 US Army to detonate unstable explosives in Iowa",
 "47 Miley Cyrus marries Maxx Morando in California",
 "48 Alcaraz beats Zverev for first ATP Finals title",
 "4 Swimmer crosses Hormuz to highlight wildlife harm",
 "6 US declassifies more UFO footage filmed in Mideast",
 "20 India and Bulgaria discuss IMEC, Black Sea",
]
ALSO = BRIEFS_L + BRIEFS_R
dc = ("Xi-Trump-Putin summit - 19 Nov 2026 · Russian missiles hit Poland - 20 Nov 2026 · "
 "SpiceJet Rs5,500 crore fundraise - 18 Nov 2026 · Hyderabad bomb-threat emails - 21 Nov 2026 · "
 "Paolo Bulgari death reported - 22 Nov 2026 · Kim Jong-un in Seoul - 22 Nov 2026 · "
 "South Korea education minister quit - reported 22 Nov 2026 · Indonesia candy factory fire itself - 22 Nov 2026")
DCHECK = [
 "D1 Xi-Trump-Putin summit - 19 Nov 2026",
 "D2 Russian missiles hit Poland - 20 Nov 2026",
 "D3 SpiceJet Rs5,500cr fundraise - 18 Nov 2026",
 "D4 Hyderabad bomb-threat emails - 21 Nov 2026",
 "D5 Paolo Bulgari death reported - 22 Nov 2026",
 "D6 Kim Jong-un in Seoul - 22 Nov 2026",
 "D11 S. Korea education minister quit - 22 Nov",
 "D12 Indonesia candy factory FIRE itself - 22 Nov",
]
NUMBERS = [("258-173","Democrats' House win - card 5"),("720/9d","India's record total - card 11"),
 ("14","missing in Kyiv - card 7"),("6","killed in Kyiv - card 6"),
 ("$3,538","gold per ounce - card 12"),("700,000+","Rohingya fled - card 10")]
PINS = [(1,0.50,0.30),(2,0.58,0.48),(3,0.52,0.28),(4,0.57,0.44),(5,0.13,0.42),(6,0.52,0.30),
 (7,0.53,0.31),(8,0.50,0.26),(9,0.50,0.55),(10,0.68,0.45),(11,0.88,0.72),(12,0.30,0.40),(13,0.11,0.40)]

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def icon(d, kind, x, y, s, col):
    if kind == "ship":
        d.polygon([(x, y+14*s/20), (x+20*s/20, y+14*s/20), (x+17*s/20, y+19*s/20), (x+3*s/20, y+19*s/20)], fill=col)
        d.rectangle([x+8*s/20, y+5*s/20, x+13*s/20, y+14*s/20], fill=col)
        d.line([x+15*s/20, y+2*s/20, x+15*s/20, y+14*s/20], fill=col, width=2)
    elif kind == "globe":
        d.ellipse([x+2, y+2, x+s-2, y+s-2], outline=col, width=3)
        d.line([x+2, y+s/2, x+s-2, y+s/2], fill=col, width=2); d.line([x+s/2, y+2, x+s/2, y+s-2], fill=col, width=2)
    elif kind == "leaf":
        d.ellipse([x+3, y+3, x+s-3, y+s-6], fill=col); d.line([x+4, y+s-2, x+s-4, y+4], fill=CREAM, width=2)
    elif kind == "radar":
        d.arc([x+2, y+2, x+s-2, y+s-2], 200, 320, fill=col, width=3); d.line([x+s/2, y+s-3, x+s/2, y+8], fill=col, width=3)
        d.ellipse([x+s/2-3, y+s-6, x+s/2+3, y+s], fill=col)
    elif kind == "flag":
        d.line([x+4, y+2, x+4, y+s-2], fill=col, width=3); d.polygon([(x+4, y+3), (x+s-2, y+7), (x+4, y+12)], fill=col)
    elif kind == "house":
        d.polygon([(x+2, y+s/2), (x+s/2, y+2), (x+s-2, y+s/2)], fill=col); d.rectangle([x+6, y+s/2, x+s-6, y+s-2], outline=col, width=3)
    elif kind == "scale":
        d.line([x+s/2, y+3, x+s/2, y+s-3], fill=col, width=3); d.line([x+4, y+7, x+s-4, y+7], fill=col, width=3)
        d.polygon([(x+4, y+7), (x+1, y+14), (x+10, y+14)], fill=col); d.polygon([(x+s-4, y+7), (x+s-10, y+14), (x+s-1, y+14)], fill=col)
    elif kind == "ball":
        d.ellipse([x+3, y+3, x+s-3, y+s-3], outline=col, width=3); d.arc([x+6, y+3, x+s+4, y+s-3], 90, 270, fill=col, width=2)
    elif kind == "coin":
        d.ellipse([x+3, y+3, x+s-3, y+s-3], fill=col); d.text((x+s/2, y+s/2), "$", font=AB(int(s*0.55)), fill=CREAM, anchor="mm")
    elif kind == "shield":
        d.polygon([(x+s/2, y+2), (x+s-3, y+6), (x+s-3, y+s/2), (x+s/2, y+s-2), (x+3, y+s/2), (x+3, y+6)], outline=col, width=3)
    else:
        d.ellipse([x+3, y+3, x+s-3, y+s-3], fill=col)

def header_common(d, W):
    d.rectangle([0, 0, W, 22], fill=INK)
    d.text((10, 11), "THE DAY'S LEDGER", font=AB(13), fill=CREAM, anchor="lm")
    d.text((W-10, 11), "40 STORIES - 7 REGIONS - EVERY ONE FROM 23 NOVEMBER 2026", font=AB(13), fill=(240, 200, 150), anchor="rm")
    d.text((512, 58), "Monday 23 November 2026", font=PB(72), fill=INK, anchor="mm")
    d.text((512, 98), "THE DAY'S LEDGER - the whole of Monday, on one page", font=PBD(19), fill=COPPER, anchor="mm")
    d.text((512, 116), "UN talks on killer AI go on  -  Tanker burns in Hormuz  -  COP31 ends with no deal", font=AR(14), fill=INK2, anchor="mm")
    regs = [("MIDDLE EAST 4", REGIONS["MIDDLE EAST"]), ("EUROPE 10", REGIONS["EUROPE"]), ("N. AMERICA 6", REGIONS["NORTH AMERICA"]),
            ("SOUTH ASIA 13", REGIONS["SOUTH ASIA"]), ("SE ASIA 3", REGIONS["SOUTHEAST ASIA"]), ("AFRICA 1", REGIONS["AFRICA"]), ("GLOBAL 3", REGIONS["GLOBAL"])]
    x = 8
    for name, col in regs:
        w = d.textlength(name, font=AB(12)) + 16
        d.rectangle([x, 124, x+w, 144], fill=col); d.text((x+w/2, 134), name, font=AB(12), fill=(255,255,255), anchor="mm"); x += w + 6
    d.text((1016, 134), "counts: main + also-on", font=AR(11), fill=GREY, anchor="rm")
    tl = ["00:02Z UN AI talks", "02:00Z Albanese on COP31", "MORNING Kyiv rescue", "MIDDAY Hormuz tanker", "AFTERNOON House 258-173", "EVENING Alcaraz title"]
    d.rectangle([8, 150, 1016, 170], outline=INK, width=1)
    x = 16
    for t in tl:
        d.text((x, 160), t, font=AB(11), fill=INK2, anchor="lm"); x += d.textlength(t, font=AB(11)) + 22

def _card(d, c, x, y, w, h, title_font, fact_font):
    num, reg, loc, status, cat, title, fact, src, ic = c
    col = REGIONS.get(reg, COPPER)
    d.rectangle([x, y, x+w, y+h], fill=PAPER, outline=INK, width=1)
    d.rectangle([x, y, x+w, y+20], fill=col)
    d.text((x+6, y+10), f"{num}. {loc}", font=AB(11), fill=(255,255,255), anchor="lm")
    d.text((x+w-6, y+10), status, font=AB(11), fill=(255,255,255), anchor="rm")
    icon(d, ic, x+w-38, y+23, 26, col)
    ty = y + 23
    for ln in wrap(d, title, title_font, w-50)[:2]:
        d.text((x+7, ty), ln, font=title_font, fill=INK); ty += 28
    fy = ty + 1
    for ln in wrap(d, fact, fact_font, w-14)[:2]:
        d.text((x+7, fy), ln, font=fact_font, fill=(40,40,36)); fy += 15
    d.text((x+7, y+h-8), cat + "  |  " + src, font=AB(10), fill=GREY, anchor="lm")

def lead(d, c, x, y, w, h):
    _card(d, c, x, y, w, h, fb(28), fr(15))

def mini(d, c, x, y, w, h):
    _card(d, c, x, y, w, h, fb(28), fr(15))

def numbers_box(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=INK)
    d.text((x+8, y+12), "THE DAY IN NUMBERS", font=AB(13), fill=(240,200,150), anchor="lm")
    yy = y + 22
    for big, small in NUMBERS:
        d.text((x+8, yy+7), big, font=PB(18), fill=CREAM, anchor="lm")
        d.text((x+112, yy+7), small, font=AR(11), fill=CREAM, anchor="lm"); yy += 16

def dcheck_box(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=(250, 238, 230), outline=RED, width=2)
    d.text((x+8, y+11), "DATE CHECK - NOT 23 NOV", font=AB(12), fill=RED, anchor="lm")
    yy = y + 23
    for t in DCHECK:
        for ln in wrap(d, t, AR(10), w-14)[:1]:
            d.text((x+7, yy), ln, font=AR(10), fill=(90,30,25)); yy += 12

def map_box(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=PAPER, outline=INK, width=1)
    d.text((x+8, y+10), "WHERE - pins = card numbers", font=AB(11), fill=INK, anchor="lm")
    d.text((x+w-8, y+10), "Dots mark land; pins mark story numbers.", font=AR(10), fill=GREY, anchor="rm")
    blobs = [(0.08,0.45,0.16,0.20),(0.20,0.30,0.10,0.14),(0.30,0.55,0.09,0.16),(0.47,0.32,0.20,0.16),(0.52,0.55,0.10,0.12),(0.68,0.35,0.22,0.20),(0.82,0.62,0.10,0.12)]
    for bx, by, bw, bh in blobs:
        for i in range(6):
            for j in range(2):
                d.ellipse([x+10+(bx+i*bw/6)*(w-20), y+20+(by+j*bh/2)*(h-28), x+12+(bx+i*bw/6)*(w-20), y+22+(by+j*bh/2)*(h-28)], fill=(150,160,140))
    for n, px, py in PINS:
        cx, cy = x+10+px*(w-20), y+20+py*(h-28)
        d.ellipse([cx-7, cy-7, cx+7, cy+7], fill=COPPER); d.text((cx, cy), str(n), font=AB(9), fill=(255,255,255), anchor="mm")

def also_footer(d, y0):
    d.text((8, y0+8), "ALSO ON MONDAY - numbered on from the main cards", font=AB(13), fill=INK, anchor="lm")
    cols = 4; colw = 252; yy0 = y0 + 19
    for i, t in enumerate(ALSO):
        cx = 8 + (i % cols) * colw; cy = yy0 + (i // cols) * 13
        num, rest = t.split(" ", 1)
        d.text((cx, cy), num, font=AB(11), fill=COPPER, anchor="lm")
        txt = rest if len(rest) <= 38 else rest[:38].rsplit(" ", 1)[0]
        d.text((cx+24, cy), txt, font=fsr(11), fill=(40,40,36), anchor="lm")
    fy = yy0 + 7 * 13 + 4
    d.line([8, fy, 1016, fy], fill=INK, width=1)
    d.text((8, fy+10), "HOW SURE: REPORTED = named source reports it. CLAIM = one side's account, labelled. ONGOING = still developing.", font=fsr(11), fill=INK2, anchor="lm")
    d.text((8, fy+24), "Every story happened, or was first reported, on Monday 23 November 2026. Contested claims are attributed.  Original drawings.", font=fsr(11), fill=INK2, anchor="lm")
    return fy

def variant_a(path):
    img = Image.new("RGB", (1024, 1024), CREAM); d = ImageDraw.Draw(img)
    header_common(d, 1024)
    gx, gy, gw, gh, gap = 8, 178, 333, 124, 4
    cells = [(gx + (i % 3)*(gw+gap), gy + (i//3)*(gh+gap)) for i in range(15)]
    for i, c in enumerate(CARDS):
        x, y = cells[i]
        if i == 0: lead(d, c, x, y, gw, gh)
        else: mini(d, c, x, y, gw, gh)
    numbers_box(d, *cells[13], gw, gh); dcheck_box(d, *cells[14], gw, gh)
    my = gy + 5*(gh+gap) - gap + 5
    map_box(d, 8, my, 1008, 44)
    also_footer(d, my + 48)
    img.save(path, optimize=True)

def variant_b(path):
    img = Image.new("RGB", (1024, 1024), CREAM); d = ImageDraw.Draw(img)
    header_common(d, 1024)
    lead(d, CARDS[0], 8, 178, 330, 190)
    numbers_box(d, 8, 376, 330, 130)
    map_box(d, 8, 514, 330, 110)
    dcheck_box(d, 8, 632, 330, 120)
    rest = CARDS[1:]
    gx, gy, gw, gh, gap = 346, 178, 335, 94, 4
    for i, c in enumerate(rest):
        x = gx + (i % 2)*(gw+gap); y = gy + (i//2)*(gh+gap)
        mini(d, c, x, y, gw, gh)
    also_footer(d, 760)
    img.save(path, optimize=True)

if __name__ == "__main__":
    variant_a("/tmp/ni23g4-akun7-A.png")
    variant_b("/tmp/ni23g4-akun7-B.png")
    print("rendered A and B")
