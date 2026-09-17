#!/usr/bin/env python3
"""Original schematic Maya numerals, CC0; no font or network required.
Run from any directory; requires rsvg-convert for the bundled PDF derivatives.
Dot = 1, horizontal bar = 5; stylized shell = 0. Not archaeological tracings.
"""
from pathlib import Path
import subprocess
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'images' / 'maya_vector'
OUT.mkdir(exist_ok=True)
for n in range(20):
    shapes = []
    if n == 0:
        shapes = ['<path d="M12 53 C17 26 80 22 89 49 C96 74 19 82 12 53 Z" fill="none" stroke="#183447" stroke-width="4"/>',
                  '<path d="M14 53 Q50 65 89 49 M29 57 Q25 43 37 35 M46 59 Q40 43 51 32 M63 57 Q57 42 65 33 M76 54 Q76 42 77 39" fill="none" stroke="#183447" stroke-width="3"/>']
    else:
        bars, dots = divmod(n, 5)
        # Each numeral shares the same canvas and unit size (no giant single dot).
        rows = bars + bool(dots)
        top = 50 - (rows - 1) * 10
        if dots:
            for j in range(dots):
                x = 50 + (j - (dots - 1) / 2) * 19
                shapes.append(f'<circle cx="{x}" cy="{top}" r="6" fill="#183447"/>')
        for j in range(bars):
            y = top + (j + bool(dots))*20
            shapes.append(f'<rect x="13" y="{y-5}" width="74" height="10" rx="2" fill="#183447"/>')
    name = OUT / f'maya_{n:02d}.svg'
    name.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">\n'+f'<title>Número maya {n}: esquema didáctico</title>\n'+'\n'.join(shapes)+'\n</svg>\n')
    subprocess.run(['rsvg-convert','-f','pdf','-o',str(name.with_suffix('.pdf')),str(name)],check=True)
print('Generated 20 distinct SVG/PDF Maya numerals.')
