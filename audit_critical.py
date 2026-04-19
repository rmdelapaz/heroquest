#!/usr/bin/env python3
"""Quick scan: find leftover <style> blocks and problematic inline text colors."""
import re, os

PROJECT = os.path.dirname(os.path.abspath(__file__))
SKIP = {"index.html"}
results = []

for f in sorted(os.listdir(PROJECT)):
    if not f.endswith('.html') or f in SKIP:
        continue
    path = os.path.join(PROJECT, f)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
        lines = content.split('\n')
    
    # Find <style> blocks (not inside <script>)
    # Simple approach: find all <style>...</style> in the raw content
    style_blocks = list(re.finditer(r'<style[^>]*>.*?</style>', content, re.DOTALL | re.IGNORECASE))
    if style_blocks:
        for m in style_blocks:
            start_line = content[:m.start()].count('\n') + 1
            end_line = content[:m.end()].count('\n') + 1
            block_lines = end_line - start_line + 1
            # Check if inside a <script> tag (SVG style blocks are OK)
            pre = content[:m.start()]
            in_svg = pre.rfind('<svg') > pre.rfind('</svg>')
            context = "IN SVG (OK)" if in_svg else "STANDALONE — NEEDS REMOVAL"
            results.append(f"STYLE_BLOCK | {f} | lines {start_line}-{end_line} ({block_lines} lines) | {context}")
    
    # Find problematic text colors (light colors invisible on white)
    problem_colors = ['#c5cae9', '#fef3c7', '#e6f3ff', '#f4e4bc', '#ffebcd', '#e6d6f7',
                       '#e6f2ff', '#dda0dd', '#e6e6fa']
    for i, line in enumerate(lines, 1):
        style_match = re.findall(r'style\s*=\s*"([^"]*)"', line)
        for style_val in style_match:
            if 'color:' in style_val.lower():
                for pc in problem_colors:
                    if pc in style_val.lower():
                        results.append(f"LIGHT_TEXT | {f} | line {i} | color {pc} invisible on white bg")

report = '\n'.join(results) if results else 'No critical issues found.'
out_path = os.path.join(PROJECT, 'audit_critical.txt')
with open(out_path, 'w') as fh:
    fh.write(report + '\n')
print(f"Wrote {len(results)} findings to {out_path}")
print(report)
