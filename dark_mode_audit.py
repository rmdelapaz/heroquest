#!/usr/bin/env python3
"""
HeroQuest Dark/Light Mode Audit Script v2
- Distinguishes SVG <style> blocks (OK) from standalone ones (bad)
- Categorizes inline colors as decorative (fine) vs text (needs fix)

Usage: python3 dark_mode_audit.py [project_dir]
"""

import re
import os
import sys
from collections import defaultdict

PROJECT_DIR = sys.argv[1] if len(sys.argv) > 1 else "."
SKIP_FILES = {"index.html"}

HEX_COLOR = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}\b')
RGB_COLOR = re.compile(r'rgba?\([^)]+\)')
SAFE_HEX = {'#fff', '#ffffff', '#000', '#000000'}

# Light text colors that are invisible on white backgrounds
INVISIBLE_ON_WHITE = {
    '#c5cae9', '#fef3c7', '#e6f3ff', '#f4e4bc', '#ffebcd', '#e6d6f7',
    '#e6f2ff', '#e6e6fa', '#f0f0f0', '#dcdcdc', '#d3d3d3',
}


def find_html_files(project_dir):
    files = []
    for f in sorted(os.listdir(project_dir)):
        if f.endswith('.html') and f not in SKIP_FILES:
            files.append(os.path.join(project_dir, f))
    return files


def scan_leftover_style_blocks(filepath, content):
    """Check for standalone <style> blocks NOT inside <svg> elements."""
    issues = []
    # Find all <style>...</style> blocks
    for m in re.finditer(r'<style[^>]*>.*?</style>', content, re.DOTALL | re.IGNORECASE):
        start_line = content[:m.start()].count('\n') + 1
        end_line = content[:m.end()].count('\n') + 1
        # Check if inside an <svg> element
        pre = content[:m.start()]
        last_svg_open = pre.rfind('<svg')
        last_svg_close = pre.rfind('</svg>')
        in_svg = last_svg_open > last_svg_close and last_svg_open != -1
        if not in_svg:
            issues.append((start_line, end_line, f"Standalone <style> block (lines {start_line}-{end_line})"))
    return issues


def scan_inline_style_colors(filepath, lines):
    """Check inline style= attributes for hardcoded colors, categorized."""
    text_issues = []  # Colors used for text — may be invisible
    deco_issues = []  # Decorative colors — gradient bars, borders, backgrounds
    style_attr = re.compile(r'style\s*=\s*"([^"]*)"', re.IGNORECASE)

    for i, line in enumerate(lines, 1):
        for match in style_attr.finditer(line):
            style_val = match.group(1)

            for hex_match in HEX_COLOR.finditer(style_val):
                color = hex_match.group().lower()
                pre = style_val[:hex_match.start()]
                if 'var(' in pre and ',' in pre.split('var(')[-1]:
                    continue
                if color in SAFE_HEX:
                    continue

                # Categorize: is this a text color or decorative?
                last_prop = pre.split(';')[-1]
                if 'color:' in last_prop and 'background' not in last_prop and 'border' not in last_prop:
                    # This is a text color property
                    if color in INVISIBLE_ON_WHITE:
                        text_issues.append((i, f"🔴 TEXT color {color} invisible on white: style=\"{style_val[:50]}...\""))
                    else:
                        text_issues.append((i, f"🟡 TEXT color {color}: style=\"{style_val[:50]}...\""))
                else:
                    deco_issues.append((i, f"Decorative {color} in style=\"{style_val[:50]}...\""))

            for rgb_match in RGB_COLOR.finditer(style_val):
                pre = style_val[:rgb_match.start()]
                if 'var(' in pre:
                    continue
                deco_issues.append((i, f"Decorative {rgb_match.group()[:30]} in style attr"))

    return text_issues, deco_issues


def scan_canvas_js_colors(filepath, lines):
    issues = []
    in_script = False
    has_canvas_helper = False
    for i, line in enumerate(lines, 1):
        if 'canvas-helper.js' in line:
            has_canvas_helper = True
        if '<script>' in line.lower() or '<script ' in line.lower():
            in_script = True
        if '</script>' in line.lower():
            in_script = False
            continue
        if in_script:
            color_assign = re.compile(r'(?:fillStyle|strokeStyle)\s*=\s*[\'"]([^"\']+)[\'"]')
            for match in color_assign.finditer(line):
                color = match.group(1)
                if not color.startswith('var(') and 'gradient' not in color.lower():
                    if any(c in color.lower() for c in ['#fff', '#ffffff', 'white', '#f4', '#e6', '#ffebcd', '#f0f0']):
                        issues.append((i, f"Canvas text/bg '{color}' — may clash in dark mode"))
                    elif any(c in color.lower() for c in ['#000', '#000000', 'black', '#333', '#1a', '#0f', '#2f']):
                        issues.append((i, f"Canvas dark bg '{color}' (OK if fillRect covers canvas)"))
    if issues and not has_canvas_helper:
        issues.insert(0, (0, "No canvas-helper.js — canvases won't respond to theme toggle"))
    return issues


def scan_css_file(css_path):
    issues = []
    if not os.path.exists(css_path):
        return [("N/A", f"CSS file not found: {css_path}")]
    with open(css_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    in_root = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if ':root' in stripped or '[data-theme' in stripped:
            in_root = True
        if in_root and '}' in stripped:
            in_root = False
            continue
        if in_root or stripped.startswith('/*') or stripped.startswith('*'):
            continue
        color_props = ['color:', 'background-color:', 'background:', 'border-color:',
                       'border:', 'border-left:', 'border-right:', 'border-top:', 'border-bottom:',
                       'box-shadow:', 'text-shadow:']
        for prop in color_props:
            if prop in stripped.lower():
                value_part = stripped.split(prop, 1)[-1]
                if value_part and 'var(' not in value_part:
                    if HEX_COLOR.findall(value_part) or RGB_COLOR.findall(value_part):
                        issues.append((i, f"Hardcoded: {stripped.strip()[:80]}"))
    return issues


def main():
    print("=" * 70)
    print("HeroQuest Dark/Light Mode Audit v2")
    print("=" * 70)

    html_files = find_html_files(PROJECT_DIR)
    print(f"\nScanning {len(html_files)} HTML files + CSS in {PROJECT_DIR}\n")

    total = defaultdict(int)

    css_path = os.path.join(PROJECT_DIR, "styles", "main.css")
    print(f"{'─'*70}\n[CSS] {css_path}\n{'─'*70}")
    css_issues = scan_css_file(css_path)
    if css_issues:
        for ln, desc in css_issues:
            print(f"  Line {ln}: {desc}")
        total["CSS hardcoded colors"] += len(css_issues)
    else:
        print("  ✅ Clean")

    files_with_issues = 0
    for filepath in html_files:
        fname = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.split('\n')
        issues_found = False

        # Style blocks (excluding SVG-internal ones)
        style_issues = scan_leftover_style_blocks(filepath, content)
        if style_issues:
            if not issues_found:
                print(f"\n{'─'*70}\n[HTML] {fname}\n{'─'*70}")
                issues_found = True
            print(f"\n  🔴 STANDALONE <style> blocks (should have been stripped):")
            for s, e, desc in style_issues:
                print(f"    {desc}")
            total["Standalone <style> blocks"] += len(style_issues)

        # Inline colors
        text_issues, deco_issues = scan_inline_style_colors(filepath, lines)
        if text_issues:
            if not issues_found:
                print(f"\n{'─'*70}\n[HTML] {fname}\n{'─'*70}")
                issues_found = True
            print(f"\n  🟡 Inline TEXT colors ({len(text_issues)}):")
            for ln, desc in text_issues[:5]:  # Show first 5
                print(f"    Line {ln}: {desc}")
            if len(text_issues) > 5:
                print(f"    ... and {len(text_issues)-5} more")
            total["Inline text colors"] += len(text_issues)

        if deco_issues:
            total["Inline decorative colors (OK)"] += len(deco_issues)

        # Canvas (summary only)
        canvas_issues = scan_canvas_js_colors(filepath, lines)
        if canvas_issues:
            total["Canvas colors (info)"] += len(canvas_issues)

        if issues_found:
            files_with_issues += 1

    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"Files scanned: {len(html_files)} HTML + 1 CSS")
    print(f"Files with actionable issues: {files_with_issues}")
    print()
    for cat, count in sorted(total.items()):
        if "OK" in cat or "info" in cat:
            icon = "🔵"
        elif "Standalone" in cat:
            icon = "🔴"
        elif "text" in cat.lower():
            icon = "🟡"
        else:
            icon = "🟡"
        print(f"  {icon} {cat}: {count}")
    print()
    print("🔴 = Must fix  |  🟡 = Review  |  🔵 = Informational (no action needed)")


if __name__ == "__main__":
    main()
