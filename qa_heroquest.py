#!/usr/bin/env python3
"""
HeroQuest Site — QA Audit Script
=================================
Checks:
  1. Nav file existence — every file in nav.js pages[] exists on disk
  2. Orphan HTML files — HTML files on disk not listed in nav.js (except index.html)
  3. Broken internal links — <a href="..."> targets that don't resolve
  4. HTML structure — missing DOCTYPE, duplicate IDs, unclosed common tags
  5. CSS variable coverage — hardcoded color values outside SVG/canvas contexts
  6. External resource check — missing src/href for scripts, stylesheets, images
  7. Empty <style> blocks — leftover empty style tags from stripping
  8. nav.js sync — QA script's page list matches nav.js on disk

Run from the heroquest project root:
    python3 qa_heroquest.py
"""

import os
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser

# ── Configuration ──────────────────────────────────────────────────────────
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Pages array extracted from nav.js (must match exactly)
NAV_PAGES = [
    "heroquest_basics.html",
    "heroquest_dungeon_mastering.html",
    "heroquest_advanced_combat.html",
    "heroquest_magic_spells.html",
    "heroquest_treasure_progression.html",
    "heroquest_original_quests.html",
    "heroquest_barbarian_tutorial.html",
    "heroquest_dwarf_tutorial.html",
    "heroquest_elf_tutorial.html",
    "heroquest_wizard_tutorial.html",
    "heroquest_warlock_tutorial.html",
    "heroquest_bard_tutorial.html",
    "heroquest_knight_tutorial.html",
    "heroquest_berserker_tutorial.html",
    "heroquest_explorer_tutorial.html",
    "heroquest_monk_tutorial.html",
    "heroquest_rogue_tutorial.html",
    "heroquest_druid_tutorial.html",
    "heroquest_digital_toolkit.html",
    "heroquest_custom_heroes_monsters.html",
    "heroquest_legendary_heroes.html",
    "heroquest_online_play.html",
    "heroquest_kellars_keep.html",
    "heroquest_return_witch_lord.html",
    "heroquest_prophecy_telor.html",
    "heroquest_spirit_queens_torment.html",
    "heroquest_against_ogre_horde.html",
    "heroquest_frozen_horror.html",
    "heroquest_mage_of_mirror.html",
    "heroquest_rise_dread_moon.html",
    "heroquest_jungles_delthrak.html",
    "heroquest_rise_dread_moon_knight.html",
    "heroquest_lore_foundations.html",
    "heroquest_lore_dark_forces.html",
    "heroquest_lore_kingdoms_regions.html",
    "heroquest_lore_great_events.html",
    "heroquest_lore_cosmic_forces.html",
    "heroquest_lore_mentors_questgivers.html",
    "heroquest_lore_ancient_dungeons.html",
    "heroquest_lore_magic_artifacts.html",
    "heroquest_lore_kellars_keep.html",
    "heroquest_lore_return_witch_lord.html",
    "heroquest_lore_prophecy_telor.html",
    "heroquest_lore_spirit_queens_torment.html",
    "heroquest_lore_against_ogre_horde.html",
    "heroquest_lore_frozen_horror.html",
    "heroquest_lore_mage_of_the_mirror.html",
    "heroquest_lore_rise_dread_moon.html",
    "heroquest_lore_jungles_delthrak.html",
]

# Known CSS variables from main.css
KNOWN_CSS_VARS = {
    "--bg", "--card-bg", "--text", "--text-muted",
    "--heading-bg", "--heading-text", "--border",
    "--code-bg", "--code-text", "--link-color",
    "--blockquote-bg", "--nav-bg", "--nav-border",
    "--table-border", "--accent", "--accent-muted",
    "--tag-bg", "--tag-text",
    "--mermaid-bg", "--mermaid-border", "--mermaid-node-fill",
    "--mermaid-node-stroke", "--mermaid-text", "--mermaid-edge",
}

# Color patterns to detect hardcoded colors
COLOR_HEX = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}\b')
COLOR_RGB = re.compile(r'rgba?\(\s*\d+')
COLOR_NAMED = re.compile(
    r'\b(color|background|background-color|border-color|border|outline)\s*:\s*'
    r'(white|black|red|blue|green|yellow|orange|purple|gray|grey|pink|brown|navy|teal|maroon)\b',
    re.IGNORECASE
)

# ── Helpers ────────────────────────────────────────────────────────────────

def get_html_files():
    """Return all .html files in the project root."""
    return sorted(
        f for f in os.listdir(PROJECT_DIR)
        if f.endswith('.html') and os.path.isfile(os.path.join(PROJECT_DIR, f))
    )


def read_file(filename):
    """Read file contents, return empty string on error."""
    path = os.path.join(PROJECT_DIR, filename)
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as fh:
            return fh.read()
    except FileNotFoundError:
        return ""


class IDCollector(HTMLParser):
    """Collects all id attributes and detects duplicates."""
    def __init__(self):
        super().__init__()
        self.ids = defaultdict(int)
        self.in_svg = 0
        self.in_script = 0
        self.in_style = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'svg':
            self.in_svg += 1
        if tag == 'script':
            self.in_script += 1
        if tag == 'style':
            self.in_style += 1
        attr_dict = dict(attrs)
        if 'id' in attr_dict and attr_dict['id']:
            self.ids[attr_dict['id']] += 1

    def handle_endtag(self, tag):
        if tag == 'svg' and self.in_svg > 0:
            self.in_svg -= 1
        if tag == 'script' and self.in_script > 0:
            self.in_script -= 1
        if tag == 'style' and self.in_style > 0:
            self.in_style -= 1


def is_inside_svg_or_canvas_js(content, match_start):
    """
    Check if a color match is inside an SVG <style> block, a <canvas>-related
    JS block, or an inline style that's decorative (gradient bars, etc.).
    Returns a category string: 'svg', 'canvas_js', 'style_block', or 'html'.
    """
    # Check if inside <svg>...</svg>
    svg_opens = [m.start() for m in re.finditer(r'<svg[\s>]', content[:match_start], re.IGNORECASE)]
    svg_closes = [m.start() for m in re.finditer(r'</svg>', content[:match_start], re.IGNORECASE)]
    if len(svg_opens) > len(svg_closes):
        return 'svg'

    # Check if inside <script>...</script>
    script_opens = [m.start() for m in re.finditer(r'<script[\s>]', content[:match_start], re.IGNORECASE)]
    script_closes = [m.start() for m in re.finditer(r'</script>', content[:match_start], re.IGNORECASE)]
    if len(script_opens) > len(script_closes):
        return 'canvas_js'

    # Check if inside <style>...</style>
    style_opens = [m.start() for m in re.finditer(r'<style[\s>]', content[:match_start], re.IGNORECASE)]
    style_closes = [m.start() for m in re.finditer(r'</style>', content[:match_start], re.IGNORECASE)]
    if len(style_opens) > len(style_closes):
        return 'style_block'

    return 'html'


# ── Check Functions ────────────────────────────────────────────────────────

def check_nav_files():
    """Check 1: Every nav.js page exists on disk."""
    print("\n" + "=" * 60)
    print("CHECK 1: Nav Page File Existence")
    print("=" * 60)
    issues = []
    for page in NAV_PAGES:
        path = os.path.join(PROJECT_DIR, page)
        if not os.path.isfile(path):
            issues.append(f"  MISSING: {page}")
    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ All {len(NAV_PAGES)} nav pages exist on disk.")
    return len(issues)


def check_orphan_files():
    """Check 2: HTML files on disk not in nav.js."""
    print("\n" + "=" * 60)
    print("CHECK 2: Orphan HTML Files (not in nav.js)")
    print("=" * 60)
    html_files = get_html_files()
    nav_set = set(NAV_PAGES)
    nav_set.add("index.html")  # index is intentionally excluded from nav
    orphans = [f for f in html_files if f not in nav_set]
    if orphans:
        for o in orphans:
            print(f"  ORPHAN: {o}")
    else:
        print(f"  ✓ No orphan HTML files. ({len(html_files)} total, {len(NAV_PAGES)} in nav + index.html)")
    return len(orphans)


def check_broken_links():
    """Check 3: Internal <a href> links that don't resolve."""
    print("\n" + "=" * 60)
    print("CHECK 3: Broken Internal Links")
    print("=" * 60)
    html_files = get_html_files()
    all_files_lower = {f.lower() for f in html_files}
    # Also include files in styles/ etc.
    for root, dirs, files in os.walk(PROJECT_DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '.vscode')]
        for f in files:
            relpath = os.path.relpath(os.path.join(root, f), PROJECT_DIR)
            all_files_lower.add(relpath.lower().replace('\\', '/'))

    href_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\'#]+)', re.IGNORECASE)
    issues = []

    for html_file in html_files:
        content = read_file(html_file)
        for match in href_pattern.finditer(content):
            href = match.group(1).strip()
            # Skip external links, mailto, javascript, data URIs
            if any(href.startswith(p) for p in ('http://', 'https://', 'mailto:', 'javascript:', 'data:', '//')):
                continue
            # Skip absolute paths that start with / (Netlify routes)
            if href.startswith('/'):
                target = href.lstrip('/')
            else:
                target = href

            # Strip query params
            target = target.split('?')[0]
            if not target:
                continue

            target_path = os.path.join(PROJECT_DIR, target)
            if not os.path.exists(target_path):
                # Also try without .html (Netlify pretty URLs)
                if not os.path.exists(target_path + '.html'):
                    issues.append(f"  {html_file}: broken link → {href}")

    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ All internal links resolve across {len(html_files)} files.")
    return len(issues)


def check_html_structure():
    """Check 4: DOCTYPE, duplicate IDs, basic structure."""
    print("\n" + "=" * 60)
    print("CHECK 4: HTML Structure Validation")
    print("=" * 60)
    html_files = get_html_files()
    issues = []

    for html_file in html_files:
        content = read_file(html_file)
        file_issues = []

        # Check DOCTYPE
        if not content.strip().lower().startswith('<!doctype html'):
            doctype_pos = content.lower().find('<!doctype html')
            if doctype_pos == -1:
                file_issues.append("missing <!DOCTYPE html>")
            elif doctype_pos > 0:
                before = content[:doctype_pos].strip()
                if before:
                    file_issues.append(f"stray content before <!DOCTYPE html>: {before[:60]}...")

        # Check for <html>, <head>, <body>
        if '<html' not in content.lower():
            file_issues.append("missing <html> tag")
        if '<head' not in content.lower():
            file_issues.append("missing <head> tag")
        if '<body' not in content.lower():
            file_issues.append("missing <body> tag")

        # Check duplicate IDs
        collector = IDCollector()
        try:
            collector.feed(content)
        except Exception:
            file_issues.append("HTML parse error")

        dupes = {id_val: count for id_val, count in collector.ids.items() if count > 1}
        if dupes:
            for id_val, count in dupes.items():
                file_issues.append(f'duplicate id="{id_val}" ({count}×)')

        # Check for empty <style> blocks (leftover from stripping)
        empty_styles = re.findall(r'<style[^>]*>\s*</style>', content, re.IGNORECASE)
        if empty_styles:
            file_issues.append(f"{len(empty_styles)} empty <style> block(s)")

        # Check for unclosed container div (common bug)
        div_opens = len(re.findall(r'<div[\s>]', content, re.IGNORECASE))
        div_closes = len(re.findall(r'</div>', content, re.IGNORECASE))
        if div_opens != div_closes:
            diff = div_opens - div_closes
            if diff > 0:
                file_issues.append(f"{diff} unclosed <div> tag(s)")
            else:
                file_issues.append(f"{abs(diff)} extra </div> tag(s)")

        if file_issues:
            for issue in file_issues:
                issues.append(f"  {html_file}: {issue}")

    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ All {len(html_files)} files pass structure checks.")
    return len(issues)


def check_resource_refs():
    """Check 5: Missing local resources (scripts, stylesheets, images)."""
    print("\n" + "=" * 60)
    print("CHECK 5: Missing Local Resources (src/href)")
    print("=" * 60)
    html_files = get_html_files()
    patterns = [
        (re.compile(r'<script\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'script'),
        (re.compile(r'<link\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE), 'stylesheet'),
        (re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'image'),
    ]
    issues = []

    for html_file in html_files:
        content = read_file(html_file)
        for pattern, res_type in patterns:
            for match in pattern.finditer(content):
                ref = match.group(1).strip()
                if any(ref.startswith(p) for p in ('http://', 'https://', 'data:', '//', 'blob:')):
                    continue
                if ref.startswith('/'):
                    target = ref.lstrip('/')
                else:
                    target = ref
                target_path = os.path.join(PROJECT_DIR, target)
                if not os.path.exists(target_path):
                    issues.append(f"  {html_file}: missing {res_type} → {ref}")

    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ All local resources found across {len(html_files)} files.")
    return len(issues)


def check_hardcoded_colors():
    """Check 6: Hardcoded colors in HTML (outside SVG/canvas JS)."""
    print("\n" + "=" * 60)
    print("CHECK 6: Hardcoded Colors (potential dark mode issues)")
    print("=" * 60)
    html_files = get_html_files()
    issues = []
    info_items = []

    css_path = os.path.join(PROJECT_DIR, 'styles', 'main.css')
    files_to_check = html_files[:]
    if os.path.isfile(css_path):
        files_to_check.append(os.path.join('styles', 'main.css'))

    for filename in files_to_check:
        content = read_file(filename)

        inline_style_pattern = re.compile(r'style=["\']([^"\']+)["\']', re.IGNORECASE)

        for match in inline_style_pattern.finditer(content):
            style_val = match.group(1)
            context = is_inside_svg_or_canvas_js(content, match.start())

            if context in ('svg', 'canvas_js'):
                continue

            # Check for hex colors
            hex_colors = COLOR_HEX.findall(style_val)
            for color in hex_colors:
                var_check = re.search(r'var\([^)]*' + re.escape(color), style_val)
                if var_check:
                    continue
                if 'gradient' in style_val.lower():
                    info_items.append(f"  [decorative] {filename}: gradient with {color}")
                    continue
                if re.search(r'(?:^|;)\s*color\s*:', style_val):
                    issues.append(f"  {filename}: inline color: {color} (line ~{content[:match.start()].count(chr(10))+1})")
                elif re.search(r'background', style_val, re.IGNORECASE):
                    info_items.append(f"  [bg] {filename}: inline background with {color}")

            # Check for rgb/rgba
            rgb_colors = COLOR_RGB.findall(style_val)
            for color in rgb_colors:
                if 'gradient' in style_val.lower():
                    continue
                if re.search(r'(?:^|;)\s*color\s*:', style_val):
                    issues.append(f"  {filename}: inline color: {color}... (line ~{content[:match.start()].count(chr(10))+1})")

    if issues:
        print(f"  Found {len(issues)} actionable hardcoded color(s):")
        for i in issues:
            print(i)
    else:
        print(f"  ✓ No actionable hardcoded text colors found.")

    if info_items:
        print(f"\n  ℹ {len(info_items)} decorative/background colors (informational only):")
        for item in info_items[:10]:
            print(item)
        if len(info_items) > 10:
            print(f"  ... and {len(info_items) - 10} more")

    return len(issues)


def check_nav_js_sync():
    """Check 7: Verify nav.js on disk matches our expected pages list."""
    print("\n" + "=" * 60)
    print("CHECK 7: nav.js Sync Verification")
    print("=" * 60)
    nav_content = read_file("nav.js")

    file_pattern = re.compile(r"file:\s*['\"]([^'\"]+)['\"]")
    nav_js_files = file_pattern.findall(nav_content)

    issues = []
    if len(nav_js_files) != len(NAV_PAGES):
        issues.append(f"  Count mismatch: nav.js has {len(nav_js_files)} pages, script expects {len(NAV_PAGES)}")

    for i, (js_file, script_file) in enumerate(zip(nav_js_files, NAV_PAGES)):
        if js_file != script_file:
            issues.append(f"  Position {i}: nav.js has '{js_file}', script has '{script_file}'")

    js_set = set(nav_js_files)
    script_set = set(NAV_PAGES)
    only_in_js = js_set - script_set
    only_in_script = script_set - js_set
    if only_in_js:
        issues.append(f"  In nav.js but not in QA script: {only_in_js}")
    if only_in_script:
        issues.append(f"  In QA script but not in nav.js: {only_in_script}")

    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ nav.js and QA script are in sync ({len(NAV_PAGES)} pages).")
    return len(issues)


def check_main_css_refs():
    """Check 8: All pages reference main.css and nav.js."""
    print("\n" + "=" * 60)
    print("CHECK 8: main.css & nav.js References")
    print("=" * 60)
    html_files = get_html_files()
    issues = []

    for html_file in html_files:
        content = read_file(html_file)
        if 'main.css' not in content and html_file != 'index.html':
            issues.append(f"  {html_file}: missing main.css reference")
        if 'nav.js' not in content and html_file != 'index.html':
            issues.append(f"  {html_file}: missing nav.js reference")

    if issues:
        for i in issues:
            print(i)
    else:
        print(f"  ✓ All {len(html_files) - 1} content pages reference main.css and nav.js.")
    return len(issues)


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║          HeroQuest Site — QA Audit Report                 ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print(f"║  Project: {PROJECT_DIR}")
    print(f"║  HTML files: {len(get_html_files())}")
    print(f"║  Nav pages: {len(NAV_PAGES)}")
    print("╚════════════════════════════════════════════════════════════╝")

    total_issues = 0
    total_issues += check_nav_files()
    total_issues += check_orphan_files()
    total_issues += check_broken_links()
    total_issues += check_html_structure()
    total_issues += check_resource_refs()
    total_issues += check_hardcoded_colors()
    total_issues += check_nav_js_sync()
    total_issues += check_main_css_refs()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if total_issues == 0:
        print("  ✅ ALL CHECKS PASSED — 0 issues found!")
    else:
        print(f"  ⚠ {total_issues} issue(s) found. Review above for details.")
    print()

    return 0 if total_issues == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
