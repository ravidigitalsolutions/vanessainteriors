"""Generates line-art interior illustrations (SVG) used as design placeholders
until genuine Vanessa Interiors project photographs are added."""
import os

INK = "#2a2226"
S = f'fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
PALETTES = {
    "pink":   ("#fde8ec", "#ed3050", "#f5d90a"),
    "blue":   ("#e3f3fb", "#009de3", "#ed3050"),
    "green":  ("#eef4de", "#7ca40f", "#009de3"),
    "plum":   ("#f6e6ef", "#85014d", "#f5d90a"),
    "yellow": ("#fdf7d8", "#e0b400", "#ed3050"),
}


def frame(body, pal="pink", label=""):
    bg, a1, a2 = PALETTES[pal]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="{label}">
<defs><radialGradient id="g1" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{a1}" stop-opacity=".30"/><stop offset="1" stop-color="{a1}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{a2}" stop-opacity=".28"/><stop offset="1" stop-color="{a2}" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="600" fill="#faf6f1"/>
<rect x="0" y="0" width="800" height="470" fill="{bg}"/>
<circle cx="600" cy="170" r="230" fill="url(#g1)"/><circle cx="170" cy="390" r="200" fill="url(#g2)"/>
<line x1="0" y1="470" x2="800" y2="470" stroke="{INK}" stroke-width="3"/>
<g {S}>{body}</g>
<line x1="60" y1="530" x2="300" y2="530" stroke="{a1}" stroke-width="4" stroke-linecap="round"/>
</svg>'''


def plant(x, y):
    return (f'<path d="M{x-22} {y} h44 l-6 52 h-32 z" fill="#fff"/>'
            f'<path d="M{x} {y} C{x-4} {y-40} {x-40} {y-60} {x-54} {y-90}"/><path d="M{x} {y} C{x+6} {y-50} {x+30} {y-70} {x+50} {y-100}"/>'
            f'<path d="M{x} {y} C{x} {y-50} {x-6} {y-90} {x+2} {y-130}"/>'
            f'<ellipse cx="{x-40}" cy="{y-72}" rx="16" ry="7" transform="rotate(-40 {x-40} {y-72})" fill="#7ca40f" fill-opacity=".35"/>'
            f'<ellipse cx="{x+36}" cy="{y-80}" rx="16" ry="7" transform="rotate(35 {x+36} {y-80})" fill="#7ca40f" fill-opacity=".35"/>'
            f'<ellipse cx="{x-2}" cy="{y-112}" rx="7" ry="16" fill="#7ca40f" fill-opacity=".35"/>')


def pendant(x, y0, y1, w=36):
    return f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}"/><path d="M{x-w} {y1+34} Q{x} {y1-14} {x+w} {y1+34} z" fill="#fff"/><ellipse cx="{x}" cy="{y1+44}" rx="{w-10}" ry="6" fill="#f5d90a" fill-opacity=".45" stroke="none"/>'


SCENES = {}

SCENES["living-room"] = ("pink", "Illustration of a living room with sofa and feature wall", f'''
<rect x="300" y="110" width="200" height="130" rx="4" fill="#fff"/><path d="M320 220 l50-60 40 40 30-30 40 50" /><circle cx="455" cy="150" r="14" fill="#ed3050" fill-opacity=".5"/>
<path d="M190 330 q0-40 40-40 h340 q40 0 40 40 v40 h-420z" fill="#fff"/>
<rect x="160" y="340" width="60" height="100" rx="18" fill="#fff"/><rect x="580" y="340" width="60" height="100" rx="18" fill="#fff"/>
<rect x="210" y="370" width="380" height="70" rx="10" fill="#fff"/><line x1="400" y1="370" x2="400" y2="440"/>
<line x1="185" y1="440" x2="185" y2="468"/><line x1="615" y1="440" x2="615" y2="468"/>
<ellipse cx="400" cy="500" rx="130" ry="18" fill="#fff"/>
<line x1="690" y1="468" x2="690" y2="200"/><path d="M650 200 h80 l-18-60 h-44z" fill="#fff"/><line x1="660" y1="468" x2="720" y2="468"/>
{plant(95, 418)}''')

SCENES["modular-kitchen"] = ("green", "Illustration of a modular kitchen with cabinets and pendant lights", f'''
<rect x="80" y="110" width="400" height="110" fill="#fff"/><line x1="180" y1="110" x2="180" y2="220"/><line x1="280" y1="110" x2="280" y2="220"/><line x1="380" y1="110" x2="380" y2="220"/>
<line x1="160" y1="185" x2="160" y2="205"/><line x1="200" y1="185" x2="200" y2="205"/><line x1="360" y1="185" x2="360" y2="205"/><line x1="400" y1="185" x2="400" y2="205"/>
<path d="M530 110 h110 v60 l30 50 h-170 l30-50z" fill="#fff"/>
<rect x="70" y="330" width="620" height="18" fill="#fff"/>
<rect x="80" y="348" width="600" height="120" fill="#fff"/><line x1="230" y1="348" x2="230" y2="468"/><line x1="380" y1="348" x2="380" y2="468"/><line x1="530" y1="348" x2="530" y2="468"/>
<line x1="80" y1="390" x2="230" y2="390"/><line x1="80" y1="430" x2="230" y2="430"/><line x1="130" y1="370" x2="180" y2="370"/><line x1="130" y1="410" x2="180" y2="410"/><line x1="130" y1="450" x2="180" y2="450"/>
<line x1="360" y1="370" x2="360" y2="400"/><line x1="400" y1="370" x2="400" y2="400"/><line x1="550" y1="370" x2="550" y2="400"/>
<ellipse cx="585" cy="324" rx="26" ry="5"/><ellipse cx="640" cy="324" rx="26" ry="5"/>
<path d="M280 330 v-24 h50 v24" fill="#fff"/><path d="M300 306 q0-26 26-26" />
<rect x="90" y="250" width="590" height="70" fill="#7ca40f" fill-opacity=".10" stroke="none"/>
{pendant(560, 0, 60, 28)}''')

SCENES["bedroom-design"] = ("plum", "Illustration of a bedroom with upholstered headboard and side lamps", f'''
<rect x="230" y="190" width="340" height="170" rx="10" fill="#fff"/><line x1="315" y1="190" x2="315" y2="360"/><line x1="400" y1="190" x2="400" y2="360"/><line x1="485" y1="190" x2="485" y2="360"/>
<rect x="210" y="360" width="380" height="80" rx="8" fill="#fff"/><path d="M210 395 h380"/>
<rect x="255" y="325" width="120" height="40" rx="18" fill="#fff"/><rect x="425" y="325" width="120" height="40" rx="18" fill="#fff"/>
<path d="M400 360 h190 v80 h-150 z" fill="#85014d" fill-opacity=".18"/>
<line x1="225" y1="440" x2="225" y2="468"/><line x1="575" y1="440" x2="575" y2="468"/>
<rect x="100" y="380" width="90" height="88" fill="#fff"/><line x1="100" y1="420" x2="190" y2="420"/>
<rect x="610" y="380" width="90" height="88" fill="#fff"/><line x1="610" y1="420" x2="700" y2="420"/>
<line x1="145" y1="380" x2="145" y2="320"/><path d="M118 320 h54 l-10-44 h-34z" fill="#fff"/>
<line x1="655" y1="380" x2="655" y2="320"/><path d="M628 320 h54 l-10-44 h-34z" fill="#fff"/>
<path d="M200 80 h400" stroke-dasharray="2 14"/><rect x="340" y="110" width="120" height="56" rx="4" fill="#fff"/>''')

SCENES["wardrobes"] = ("yellow", "Illustration of a full-height sliding wardrobe with loft storage", f'''
<rect x="120" y="70" width="450" height="80" fill="#fff"/><line x1="270" y1="70" x2="270" y2="150"/><line x1="420" y1="70" x2="420" y2="150"/>
<rect x="120" y="150" width="450" height="318" fill="#fff"/>
<rect x="120" y="150" width="160" height="318" fill="#e0b400" fill-opacity=".14"/><line x1="280" y1="150" x2="280" y2="468"/><line x1="420" y1="150" x2="420" y2="468"/>
<line x1="265" y1="280" x2="265" y2="340"/><line x1="295" y1="280" x2="295" y2="340"/><line x1="435" y1="280" x2="435" y2="340"/>
<line x1="330" y1="200" x2="400" y2="200"/><path d="M340 200 v14 l-18 30 h56 l-18-30 v-14"/><path d="M372 200 v14 l-12 34"/>
<line x1="300" y1="380" x2="400" y2="380"/><line x1="300" y1="420" x2="400" y2="420"/>
<rect x="610" y="150" width="90" height="220" rx="45" fill="#fff"/><path d="M630 200 q20-20 40 0" />
<rect x="600" y="410" width="110" height="30" rx="6" fill="#fff"/><line x1="612" y1="440" x2="612" y2="468"/><line x1="698" y1="440" x2="698" y2="468"/>''')

SCENES["false-ceiling"] = ("blue", "Illustration of a layered false ceiling with cove lighting", f'''
<path d="M40 40 h720 v50 h-80 v40 h-560 v-40 h-80z" fill="#fff"/>
<path d="M120 132 h560" stroke="#f5d90a" stroke-width="8" stroke-opacity=".8"/>
<path d="M200 130 v30 h400 v-30" fill="#fff"/><path d="M210 164 h380" stroke="#f5d90a" stroke-width="6" stroke-opacity=".7"/>
<circle cx="160" cy="112" r="6" fill="{INK}"/><circle cx="640" cy="112" r="6" fill="{INK}"/><circle cx="80" cy="70" r="5" fill="{INK}"/><circle cx="720" cy="70" r="5" fill="{INK}"/>
<line x1="400" y1="160" x2="400" y2="210"/><path d="M340 210 h120 l-20 36 h-80z" fill="#fff"/><path d="M350 246 l-10 24 M400 246 v28 M450 246 l10 24"/>
<path d="M300 300 l-40 168 M500 300 l40 168" stroke-opacity=".25"/>
<path d="M170 400 q0-30 30-30 h120 q30 0 30 30 v40 h-180z" fill="#fff"/><line x1="185" y1="440" x2="185" y2="468"/><line x1="335" y1="440" x2="335" y2="468"/>
<rect x="470" y="360" width="200" height="30" fill="#fff"/><rect x="480" y="390" width="180" height="78" fill="#fff"/><line x1="570" y1="390" x2="570" y2="468"/>''')

SCENES["office-interiors"] = ("blue", "Illustration of an office workspace with desk, chair and shelving", f'''
<rect x="90" y="90" width="220" height="170" fill="#fff"/><line x1="90" y1="120" x2="310" y2="120"/><line x1="90" y1="150" x2="310" y2="150"/><line x1="90" y1="180" x2="310" y2="180"/><line x1="90" y1="210" x2="310" y2="210"/><line x1="90" y1="240" x2="310" y2="240"/>
<rect x="420" y="90" width="300" height="200" fill="#fff"/><line x1="420" y1="140" x2="720" y2="140"/><line x1="420" y1="190" x2="720" y2="190"/><line x1="420" y1="240" x2="720" y2="240"/>
<rect x="440" y="110" width="30" height="30"/><rect x="480" y="100" width="20" height="40"/><rect x="560" y="160" width="60" height="30"/><circle cx="670" cy="220" r="16"/>
<rect x="160" y="340" width="420" height="16" fill="#fff"/><line x1="180" y1="356" x2="180" y2="468"/><line x1="560" y1="356" x2="560" y2="468"/><rect x="440" y="356" width="120" height="80" fill="#fff"/><line x1="440" y1="396" x2="560" y2="396"/>
<rect x="250" y="250" width="140" height="90" rx="6" fill="#fff"/><rect x="262" y="262" width="116" height="66" fill="#009de3" fill-opacity=".18" stroke="none"/><line x1="320" y1="340" x2="320" y2="340"/>
<path d="M300 400 q0-40 40-40 h20 q40 0 40 40 v20 h-100z" fill="#fff"/><line x1="350" y1="420" x2="350" y2="455"/><path d="M320 468 l30-13 30 13"/>
{plant(680, 418)}''')

SCENES["commercial-interiors"] = ("pink", "Illustration of a retail showroom with display shelves and counter", f'''
<rect x="60" y="60" width="680" height="50" fill="#fff"/><path d="M90 85 h140" stroke="#ed3050" stroke-width="8"/>
<path d="M150 110 l-20 30 M300 110 l-20 30 M450 110 l-20 30 M600 110 l-20 30"/>
<rect x="80" y="170" width="200" height="298" fill="#fff"/><line x1="80" y1="240" x2="280" y2="240"/><line x1="80" y1="310" x2="280" y2="310"/><line x1="80" y1="380" x2="280" y2="380"/>
<rect x="100" y="200" width="36" height="40"/><rect x="150" y="210" width="36" height="30"/><rect x="200" y="195" width="50" height="45"/><rect x="110" y="270" width="60" height="40"/><rect x="190" y="280" width="40" height="30"/><rect x="100" y="340" width="40" height="40"/><rect x="160" y="350" width="90" height="30"/>
<rect x="360" y="360" width="200" height="108" fill="#fff"/><rect x="360" y="340" width="200" height="20" fill="#fff"/><path d="M380 400 h160" stroke="#ed3050" stroke-opacity=".5"/>
<circle cx="440" cy="300" r="26" fill="#fff"/><line x1="440" y1="326" x2="440" y2="340"/>
<rect x="610" y="190" width="110" height="278" fill="#fff"/><line x1="610" y1="260" x2="720" y2="260"/><line x1="610" y1="330" x2="720" y2="330"/><line x1="610" y1="400" x2="720" y2="400"/>
<circle cx="640" cy="236" r="12"/><circle cx="690" cy="236" r="12"/><rect x="630" y="290" width="70" height="40"/>''')

SCENES["villa-interiors"] = ("green", "Illustration of a modern two-storey villa", f'''
<rect x="160" y="150" width="300" height="140" fill="#fff"/><rect x="130" y="130" width="360" height="20" fill="#fff"/>
<rect x="160" y="290" width="480" height="178" fill="#fff"/><rect x="130" y="270" width="540" height="20" fill="#fff"/>
<rect x="190" y="175" width="110" height="90" fill="#009de3" fill-opacity=".15"/><line x1="245" y1="175" x2="245" y2="265"/>
<rect x="330" y="175" width="100" height="90" fill="#009de3" fill-opacity=".15"/>
<rect x="190" y="320" width="160" height="110" fill="#009de3" fill-opacity=".15"/><line x1="270" y1="320" x2="270" y2="430"/>
<rect x="400" y="340" width="70" height="128" fill="#fff"/><circle cx="458" cy="405" r="4" fill="{INK}"/>
<rect x="510" y="320" width="100" height="80" fill="#009de3" fill-opacity=".15"/>
<path d="M490 150 h150 v120" /><path d="M500 180 h120 M500 210 h120 M500 240 h120" stroke-opacity=".4"/>
<line x1="720" y1="468" x2="712" y2="250"/><path d="M712 250 q-60 -10 -80 30 M712 250 q50 -30 80 0 M712 250 q-20 -50 -60 -60 M712 250 q30 -60 70 -50"/>
<path d="M40 468 q20-40 50 0 q20-30 45 0" fill="#7ca40f" fill-opacity=".3"/>''')

SCENES["renovation"] = ("yellow", "Illustration of a room being renovated with ladder, paint roller and swatches", f'''
<rect x="80" y="80" width="360" height="388" fill="#fff"/><rect x="80" y="80" width="200" height="388" fill="#e0b400" fill-opacity=".18" stroke="none"/><line x1="280" y1="80" x2="280" y2="468" stroke-dasharray="6 10"/>
<rect x="250" y="160" width="60" height="26" rx="6" fill="#fff"/><path d="M310 173 h20 v40 h-40 v30"/><line x1="290" y1="243" x2="290" y2="310"/>
<path d="M520 468 l60 -330 M640 468 l-60 -330"/><path d="M536 380 h92 M550 300 h64 M564 220 h36"/>
<rect x="660" y="130" width="60" height="44" fill="#ed3050" fill-opacity=".6"/><rect x="660" y="184" width="60" height="44" fill="#7ca40f" fill-opacity=".6"/><rect x="660" y="238" width="60" height="44" fill="#009de3" fill-opacity=".6"/>
<path d="M470 468 v-40 h50 v40" fill="#fff"/><path d="M470 428 q25-18 50 0"/>''')

SCENES["turnkey-interiors"] = ("plum", "Illustration of a floor plan with a key, representing turnkey interiors", f'''
<rect x="100" y="80" width="420" height="360" fill="#fff"/><line x1="100" y1="250" x2="300" y2="250"/><line x1="300" y1="80" x2="300" y2="200"/><line x1="300" y1="240" x2="300" y2="440"/>
<line x1="300" y1="320" x2="520" y2="320"/><line x1="410" y1="320" x2="410" y2="360"/><line x1="410" y1="400" x2="410" y2="440"/>
<path d="M300 200 a40 40 0 0 1 40 40"/><rect x="140" y="110" width="90" height="60" rx="6"/><rect x="340" y="110" width="140" height="80" rx="12"/><rect x="130" y="300" width="60" height="100"/><circle cx="460" cy="380" r="22"/>
<rect x="100" y="80" width="200" height="170" fill="#85014d" fill-opacity=".08" stroke="none"/>
<circle cx="620" cy="250" r="50" fill="#fff"/><circle cx="620" cy="250" r="18"/><path d="M620 300 v150 M620 380 h30 M620 420 h40"/>
<path d="M560 150 q60-60 120 0" stroke="#f5d90a" stroke-width="6"/>''')

SCENES["home-interiors"] = ("pink", "Illustration of an open-plan home with living and dining areas", f'''
<rect x="80" y="100" width="170" height="220" fill="#009de3" fill-opacity=".12"/><rect x="80" y="100" width="170" height="220"/><line x1="165" y1="100" x2="165" y2="320"/>
<path d="M100 380 q0-30 30-30 h170 q30 0 30 30 v30 h-230z" fill="#fff"/><rect x="90" y="400" width="250" height="44" rx="10" fill="#fff"/><line x1="110" y1="444" x2="110" y2="468"/><line x1="320" y1="444" x2="320" y2="468"/>
<rect x="430" y="360" width="240" height="14" fill="#fff"/><line x1="450" y1="374" x2="450" y2="468"/><line x1="650" y1="374" x2="650" y2="468"/>
<path d="M470 360 v-50 h40 v50 M590 360 v-50 h40 v50" fill="#fff"/><path d="M470 420 h40 v48 M630 420 h-40 v48"/>
{pendant(550, 0, 170, 40)}
<rect x="380" y="120" width="120" height="80" rx="4" fill="#fff"/><rect x="600" y="100" width="90" height="120" rx="45" fill="#ed3050" fill-opacity=".12"/>''')

SCENES["apartments"] = ("blue", "Illustration of an apartment building", f'''
<rect x="230" y="70" width="340" height="398" fill="#fff"/>
''' + "".join(f'<rect x="{x}" y="{y}" width="60" height="50" fill="#009de3" fill-opacity=".15"/>' for y in (100, 180, 260, 340) for x in (260, 370, 480)) + f'''
<rect x="370" y="410" width="60" height="58" fill="#fff"/><path d="M40 468 q30-60 60 0 M690 468 q30-50 60 0" fill="#7ca40f" fill-opacity=".3"/>
<path d="M600 468 v-200 h120 v200" fill="#fff"/><path d="M620 300 h80 M620 340 h80 M620 380 h80 M620 420 h80" stroke-opacity=".4"/>''')


def write_all(outdir):
    os.makedirs(outdir, exist_ok=True)
    for name, (pal, label, body) in SCENES.items():
        with open(os.path.join(outdir, f"{name}.svg"), "w") as f:
            f.write(frame(body, pal, label))
    return list(SCENES)


if __name__ == "__main__":
    import sys
    print(write_all(sys.argv[1]))
