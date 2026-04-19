#!/usr/bin/env python3
"""Find the 27 inline text color issues with file, line, and context."""
import re, os

PROJECT = os.path.dirname(os.path.abspath(__file__))
SKIP = {"index.html"}
HEX = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}\b')

for f in sorted(os.listdir(PROJECT)):
    if not f.endswith('.html') or f in SKIP:
        continue
    with open(os.path.join(PROJECT, f), 'r') as fh:
        lines = fh.readlines()
    hits = []
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r'style\s*=\s*"([^"]*)"', line):
            sv = m.group(1)
            parts = sv.split(';')
            for part in parts:
                p = part.strip().lower()
                if p.startswith('color:') and 'background' not in p:
                    for hx in HEX.finditer(part):
                        color = hx.group().lower()
                        if color not in ('#fff', '#ffffff', '#000', '#000000'):
                            if 'var(' not in part[:hx.start()]:
                                hits.append((i, color, sv[:80]))
    if hits:
        print(f"\n{'='*60}")
        print(f"{f} — {len(hits)} text color issues")
        print(f"{'='*60}")
        for ln, color, ctx in hits:
            print(f"  Line {ln}: {color}")
            print(f"    {ctx}")
