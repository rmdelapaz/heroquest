# HeroQuest Site — Continuation Notes

## Project Location
`\\wsl$\Ubuntu\home\practicalace\projects\heroquest`

## What Was Done

### Session 1 — Quick Fixes + main.css Foundation + Lore Batch 1 (April 2026)

**Quick Fixes:**
- `heroquest_barbarian_tutorial.html` — removed stray `<div class="canvas-container">` junk content before `<!DOCTYPE html>`
- `heroques_lore_prophecy_telor.html` → renamed to `heroquest_lore_prophecy_telor.html` (fixed missing 't' typo)
- Updated `nav.js` and `index.html` references to use corrected filename
- `nav.js` — added Netlify pretty URL support: `normalize()` function strips `.html` before comparing in `findIndex`, added `'index'` to isIndex check

**Orphan / Dead File Cleanup (done by Ray):**
- Deleted `/heroquest/heroquest/` subfolder (18 orphan files from older generation)
- Deleted `styles/main copy.css` (dead backup file)

**main.css Foundation Upgrade:**
- Added `*, *::before, *::after { box-sizing: border-box; }` and `html { scroll-behavior: smooth; }`
- Replaced old `body` styles (Trebuchet MS, margin-left/right, `line-height: 110%`) with modern: Segoe UI system font stack, `line-height: 1.6`, `padding: 24px`, CSS variable colors (`var(--bg)`, `var(--text)`)
- Added `.container` base class: `max-width: 960px`, centered, `background: var(--card-bg)`, padded, rounded, shadowed, bordered — this is the shared wrapper all content pages use
- Updated heading styles: removed left/right margins, added `border-radius: 6px`, switched to CSS variables (`var(--heading-bg)`, `var(--heading-text)`), proper `font-size` units (rem instead of x-large/large)
- Updated `strong` to use `var(--text)` instead of hardcoded color
- Updated paragraph margins: removed `margin-left: 45px` → `margin: 0.75rem 0; padding: 0 0.5rem`
- Updated table: `margin: 1rem auto; border-collapse: collapse`
- Updated code/pre: CSS variable colors, `border-radius: 4px`, `line-height: 1.5`
- Updated link color to `var(--link-color)` with hover transition
- Updated list margins: `45px` → `24px`
- Updated blockquote: removed huge left/right margins (150px/140px), now `margin: 1rem 0` with left border accent, CSS variable colors
- Updated img: `max-width: 100%; height: auto` (was `width: 100%`)
- Added `canvas { max-width: 100%; height: auto; }`
- Added `svg { max-width: 100%; height: auto; }`
- Added `.canvas-container` shared class (text-center, padding, border, rounded)
- Added `.table-container` overflow-x: auto
- **Responsive breakpoints added:**
  - Tablet (≤768px): body padding 16px, container padding 24px, heading sizes reduced, list/code margins reduced, `pre` gets `pre-wrap`, `div img` → 80%
  - Phone (≤480px): body padding 8px, container padding 16px, heading sizes further reduced, `div img` → 100%

**Lore Page Inline Style Stripping — Batch 1 (5 of 17 done):**
- `heroquest_lore_foundations.html` — stripped entire `<style>` block (10 rules: body, container, h1, h2, ancient-scroll, realm-card, character-spotlight, cosmologyCanvas, mermaid)
- `heroquest_lore_dark_forces.html` — stripped entire `<style>` block (~32 rules: body, container, headings, villain-card family, chaos-lord/undead/orc/monster variants, evil-title, dark-scroll, corruption-panel, threat-level, ability/weakness tags, chaosCanvas, mermaid, power-meter family, nightmare-zone, servant-grid/card)
- `heroquest_lore_kingdoms_regions.html` — stripped entire `<style>` block (~15 rules: body, container, headings, kingdom-card, kingdom-banner, region-spotlight, ancient-text, political-web, mapCanvas, mermaid, trade-route, settlement-type)
- `heroquest_lore_great_events.html` — stripped entire `<style>` block (~38 rules: body, container, headings, event-card family with 5 variants, event-type badges, chronicle-tome, battle-description, consequence-panel, legend-birth, impact/participant/legacy tags, timelineCanvas, mermaid, scale-meter family, turning-point, campaign-grid/card, prophecy-fulfilled, world-wound)
- `heroquest_lore_cosmic_forces.html` — stripped entire `<style>` block (~36 rules: body, container, headings, divine-card family with 4 force variants, force-type badges, celestial-tome, divine-manifestation, cosmic-warning, divine-blessing, influence/domain/corruption tags, cosmicWebCanvas, mermaid, divine-meter family, prophecy-scroll, pantheon-grid, deity-card, divine-intervention, balance-scale)
- Pattern: each page's `<style>` block overrides body/container/headings + defines 10-40 unique decorative CSS classes. After stripping, main.css handles all base styling. The custom class names remain in the HTML as no-ops (harmless divs).

### Session 2 — CSS Bug Fix + Lore Batch 2 (April 2026)

**CSS Bug Fix:**
- `heroquest_lore_mage_of_the_mirror.html` — fixed `transition: width: 0.6s ease;` → `transition: width 0.6s ease;` (extra colon causing 3 CSS lint errors)

**Lore Page Inline Style Stripping — Batch 2 (10 of 12 remaining done, 15/17 total):**
- `heroquest_lore_mentors_questgivers.html` — stripped ~38 rules (mentor-card family, wisdom-scroll, guidance-lesson, quest-briefing, teaching/specialty/motivation tags, mentorNetworkCanvas, wisdom-meter family, mentor-grid, teaching-card, secret-knowledge, legacy-chain)
- `heroquest_lore_ancient_dungeons.html` — stripped ~35 rules (dungeon-card family, legend-tome, chamber-layout, danger-warning, treasure-hint, hazard/mystery/reward tags, dungeonMapCanvas, exploration-meter family, room-grid/card, secret-passage)
- `heroquest_lore_magic_artifacts.html` — stripped ~37 rules (artifact-card family, arcane-tome, spell-matrix, power-warning, enchantment-effect, power/rarity/curse tags, magicFlowCanvas, magic-meter family, spell-grid/card, creation-forge)
- `heroquest_lore_kellars_keep.html` — stripped ~38 rules (quest-card family, keep-chronicle, fortress-layout, tactical-briefing, danger-assessment, defense/threat/reward tags, keepLayoutCanvas, difficulty-meter family, quest-grid, mission-card, secret-passage, fortress-defense)
- `heroquest_lore_return_witch_lord.html` — stripped ~39 rules (witch-card family, dark-chronicle, necromantic-ritual, corruption-spread, undead-manifestation, malice/power/corruption tags, witchLordCanvas, power-meter family, minion-grid/card, resurrection-phase, ancient-evil, dark-prophecy)
- `heroquest_lore_prophecy_telor.html` — stripped ~39 rules (prophecy-card family, mystic-scroll, vision-sequence, prophecy-warning, destiny-revelation, fate/vision/oracle tags, prophecyWebCanvas, prophecy-meter family, vision-grid/card, temporal-nexus, prophecy-fragment, sage-council)
- `heroquest_lore_spirit_queens_torment.html` — stripped ~40 rules (spirit-card family, ethereal-chronicle, spiritual-manifestation, torment-description, ethereal-vision, sorrow/ethereal/spirit tags, spiritRealmCanvas, anguish-meter family, spirit-grid, realm-boundary, tragic-past, redemption-path, planar-intersection)
- `heroquest_lore_against_ogre_horde.html` — stripped ~40 rules (ogre-card family, savage-chronicle, tribal-dynamics, war-tactics, primal-instinct, brutality/tribal/savage tags, ogreHordeCanvas, ferocity-meter family, horde-grid, tribal-hierarchy, savage-wisdom, civilization-clash, territorial-expansion)
- `heroquest_lore_frozen_horror.html` — stripped ~41 rules (frost-card family, glacial-chronicle, ice-manifestation, freezing-terror, arctic-vision, frost/ice/cold tags, frozenRealmCanvas, terror-meter family, creature-grid/card, permafrost-realm, ancient-prison, winter-salvation, dimensional-rift, eternal-winter). **Also contained `transition: width: 0.6s ease` bug (same as mage_of_mirror) — removed with entire block.**
- `heroquest_lore_mage_of_the_mirror.html` — stripped ~41 rules (mirror-card family, reflection-chronicle, mirror-manifestation, illusion-weaving, reality-distortion, reflection/illusion/mirror tags, mirrorRealmCanvas, deception-meter family, reflection-grid/card, mirror-dimension, twisted-truth, clarity-quest, paradox-chamber, identity-crisis)

### Session 3 — Lore Completion + Foundation Batch (April 2026)

**Lore Page Inline Style Stripping — Final 2 (17/17 complete):**
- `heroquest_lore_rise_dread_moon.html` — no `<style>` block found (already clean)
- `heroquest_lore_jungles_delthrak.html` — no `<style>` block found (already clean)

**Foundation Page Inline Style Stripping — All 6 done:**
- `heroquest_basics.html` — stripped ~540 lines (body, container, container::before, analogy-box, practice-box, hero-card, dice-container, dice-button, dice-result, tutorial-step/steps, canvas, beginner-tip/warning, progress-tracker/item/checkbox, game-flow, flow-step/number, p, strong, em, ul/ol/li, a, code, table/th/td, mermaid, blockquote, quiz-question/options/option, responsive 768px, focus, prefers-reduced-motion, highlight-important, example-scenario, quick-reference, stats-display/stat-item)
- `heroquest_dungeon_mastering.html` — stripped ~585 lines (body, container, headings, psychology-box, scenario-box, voice-guide, dm-tip, tension-meter/indicator, canvas, p, strong, em, ul/ol/li, a, code, table, mermaid, blockquote, responsive 768px, focus, prefers-reduced-motion)
- `heroquest_advanced_combat.html` — stripped ~437 lines (body, container, combat-principle, hero-role, tactics-box, formation-demo, battlefield-grid, grid-cell variants, canvas, p, strong, em, ul/ol/li, a, code, table, mermaid, blockquote, responsive 768px, focus, prefers-reduced-motion)
- `heroquest_magic_spells.html` — stripped ~175 lines (body, container, magic-principle, spell-card, grimoire-entry, mystical-box, mana-bar/indicator, spell-matrix, spell-rune, canvas, mermaid)
- `heroquest_treasure_progression.html` — stripped ~291 lines (body, container, treasure-principle, equipment-card, progression-box, reward-system, treasure-chest, character-sheet, stat-bar/fill, equipment-slot, canvas, mermaid)
- `heroquest_original_quests.html` — stripped ~310 lines (body, container, quest-principle, quest-card, strategy-box, design-analysis, quest-selector, quest-button, difficulty-meter/indicator, canvas, mermaid)

### Session 4 — Hero Tutorial Batch (April 2026)

**Hero Tutorial Page Inline Style Stripping — All 12 done:**
- `heroquest_barbarian_tutorial.html` — stripped 5 rules (hero-card, stat-display, canvas-container, analogy-box, combat-example)
- `heroquest_dwarf_tutorial.html` — stripped 7 rules (hero-card, stat-display, canvas-container, analogy-box, trap-example, special-ability, treasure-box)
- `heroquest_elf_tutorial.html` — stripped 8 rules (hero-card, stat-display, canvas-container, analogy-box, combat-example, spell-ability, ranged-box, flexibility-highlight)
- `heroquest_wizard_tutorial.html` — stripped 9 rules (hero-card, stat-display, canvas-container, analogy-box, spell-mastery, vulnerability-warning, tactical-box, spell-list, positioning-critical)
- `heroquest_warlock_tutorial.html` — stripped 9 rules (hero-card, stat-display, canvas-container, analogy-box, dark-magic, balance-warning, tactical-hybrid, chaos-power, corruption-theme)
- `heroquest_bard_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, inspiration-power, support-mastery, versatility-highlight, team-synergy, performance-art, knowledge-base)
- `heroquest_knight_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, chivalric-code, defensive-mastery, honor-bound, tactical-discipline, protection-aura, noble-bearing)
- `heroquest_berserker_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, berserker-rage, primal-fury, savage-instincts, tribal-wisdom, blood-frenzy, wild-nature)
- `heroquest_explorer_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, survival-mastery, exploration-skills, wilderness-craft, pathfinding-expert, discovery-hunter, frontier-wisdom)
- `heroquest_monk_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, martial-arts, inner-peace, spiritual-power, chi-mastery, enlightened-combat, monastic-wisdom)
- `heroquest_rogue_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, stealth-mastery, thievery-skills, cunning-tactics, shadow-craft, opportunist-nature, criminal-expertise)
- `heroquest_druid_tutorial.html` — stripped 10 rules (hero-card, stat-display, canvas-container, analogy-box, nature-magic, elemental-power, wild-shape, environmental-control, natural-harmony, primal-wisdom)

### Session 5 — Expansion Partial + Digital/Advanced Batch (April 2026)

**Expansion Page Inline Style Stripping — 4 of 10 done:**
- `heroquest_kellars_keep.html` — stripped 59 rules (~420 lines: body, container, container::before, jungle-principle, survival-box, environment-analysis, environment-layers, layer-node family, survival-meter/indicator, jungle-map, jungle-cell family, 8 terrain types, resource-tracker/item family, weather-tracker/condition family, canvas, p, strong, em, ul/ol/li, a, code, table/th/td, mermaid, responsive 768px, focus, prefers-reduced-motion)
- `heroquest_prophecy_telor.html` — stripped 33 rules (~280 lines: body, container, prophecy-principle, divine-card family, choice-node family, text contrast overrides, div[id*=result], power-showcase family, prophecy-tracker, prophecy-stage family, telor-avatar, divine-pulse keyframes, choice-matrix, destiny-box, mystical-analysis, canvas, prophecy-scroll, fate-meter/indicator, divine-powers, section heading colors, ul/ol/li)

**Digital/Advanced Page Inline Style Stripping — All 4 done:**
- `heroquest_digital_toolkit.html` — stripped 62 rules (~470 lines: body, container.toolkit-realm, h3.tool-title, hero-banner family, quick-actions/btn family, toolkit-grid, tool-panel family, character-sheet, stat-row/label/value, dice-grid/btn family, roll-result, spell-grid/card family, spell-name/cost, mana-tracker/circle family, combat-grid, combatant hero/monster, roll-btn family, treasure-btn family, setting-row/label/toggle family, p, strong, em, a, responsive 768px, focus, prefers-reduced-motion)
- `heroquest_custom_heroes_monsters.html` — stripped 43 rules (body, container, headings, quest-card family with 5 type variants, card-type badges, creation-chronicle, design-brief, balance-warning, creation/power/balance tags, creationCanvasElement, mermaid, stat-block/grid/card, conversion-table, example-hero/monster, power-scale/fill/label, table/th/td, formula-box)
- `heroquest_legendary_heroes.html` — stripped 31 rules (body, container, headings, hero-card family with shimmer keyframes, 4 class variants, hero-title variants, legend-scroll, skill-showcase, backstory-panel, weapon-stats, personality-trait, heroLineageCanvas, mermaid, stat-bar/fill/label, adventure-hook)
- `heroquest_online_play.html` — stripped 42 rules (body, container, headings, quest-card family with digitalShimmer keyframes, 5 type variants, card-type badges, digital-chronicle, setup-brief, tech-warning, digital/platform/tool tags, onlineSetupCanvas, mermaid, platform-grid/card, feature-comparison, setup-steps, pro-tip, table/th/td, cost-indicator, free/paid/freemium)

### Session 6 — Expansion Completion via Batch Script (April 2026)

**Expansion Page Inline Style Stripping — Remaining 8 of 10 done (10/10 total):**
- Used `strip_styles.py` batch script run locally in WSL to process all 8 files at once
- `heroquest_return_witch_lord.html` — stripped ~58 rules (villain-principle, magic-card, epic-box, dramatic-analysis, witch-lord-portrait with villain-glow keyframes, boss-phases, phase-node/arrow, power-meter/indicator, legendary-encounters, encounter-card, spell-arsenal, spell-showcase, canvas, strong, em, a, code, table/th/td, blockquote, button/btn, villain-quote with ::before/::after, strategy-highlight, responsive 768px, focus, prefers-reduced-motion, card text contrast, mermaid)
- `heroquest_spirit_queens_torment.html` — stripped ~81 rules
- `heroquest_against_ogre_horde.html` — stripped ~72 rules
- `heroquest_frozen_horror.html` — stripped ~89 rules
- `heroquest_mage_of_mirror.html` — stripped ~78 rules
- `heroquest_rise_dread_moon.html` — stripped ~71 rules
- `heroquest_jungles_delthrak.html` — stripped ~82 rules
- `heroquest_rise_dread_moon_knight.html` — stripped ~69 rules
- **All inline style stripping is now complete across all 49 content pages.** Only `index.html` retains scoped inline styles (by design).

## What Still Needs Doing

### ~~1. Hero Tutorial Page Inline Style Stripping — 12 files~~ ✅ DONE (Session 4)

### ~~2. Expansion Page Inline Style Stripping — 10/10 done~~ ✅ DONE (Sessions 5–6)
- ~~`heroquest_kellars_keep.html`~~ ✅ (59 rules stripped)
- ~~`heroquest_prophecy_telor.html`~~ ✅ (33 rules stripped)
- ~~`heroquest_return_witch_lord.html`~~ ✅ (58 rules stripped — Session 6)
- ~~`heroquest_spirit_queens_torment.html`~~ ✅ (81 rules stripped — Session 6)
- ~~`heroquest_against_ogre_horde.html`~~ ✅ (72 rules stripped — Session 6)
- ~~`heroquest_frozen_horror.html`~~ ✅ (89 rules stripped — Session 6)
- ~~`heroquest_mage_of_mirror.html`~~ ✅ (78 rules stripped — Session 6)
- ~~`heroquest_rise_dread_moon.html`~~ ✅ (71 rules stripped — Session 6)
- ~~`heroquest_jungles_delthrak.html`~~ ✅ (82 rules stripped — Session 6)
- ~~`heroquest_rise_dread_moon_knight.html`~~ ✅ (69 rules stripped — Session 6)

### ~~3. Digital/Advanced Page Inline Style Stripping — 4 files~~ ✅ DONE (Session 5)
- ~~`heroquest_digital_toolkit.html`~~ ✅ (62 rules stripped)
- ~~`heroquest_custom_heroes_monsters.html`~~ ✅ (43 rules stripped)
- ~~`heroquest_legendary_heroes.html`~~ ✅ (31 rules stripped)
- ~~`heroquest_online_play.html`~~ ✅ (42 rules stripped)

### 4. Light/Dark Mode CSS Toggle Behavior Audit — DONE (Session 8)
- Wrote `dark_mode_audit.py` (v2) — programmatic scanner for hardcoded colors across all 49 HTML + CSS files
  - Distinguishes SVG-internal `<style>` blocks (OK) from standalone ones (bad)
  - Categorizes inline colors as text (needs fix) vs decorative (gradient bars, borders — OK)
  - Reports canvas JS colors as informational only
- **Final audit result: 0 actionable HTML issues, 3 minor CSS issues (box-shadow rgba values)**
- **Files fixed during audit:**
  - `heroquest_digital_toolkit.html` — 6× `color: #c5cae9` → `var(--text)` + 5× accent headings `#a663cc`/`#9c88ff` → `var(--accent, ...)`
  - `heroquest_against_ogre_horde.html` — `color: #fef3c7` → `var(--text-muted)` + removed unnecessary inline color
  - `heroquest_prophecy_telor.html` — 3× blue arrow `#0d6efd` → `var(--accent, #0d6efd)`
  - `heroquest_rise_dread_moon.html` — 4× orange arrow `#ffa726` → `var(--accent, #ffa726)`
  - `heroquest_rise_dread_moon_knight.html` — 4× orange arrow `#ffa726` → `var(--accent, #ffa726)`
  - `heroquest_jungles_delthrak.html` — 2× JS template literal colors → `var(--success, #15803d)` and `var(--danger, #dc2626)`
- Remaining 228 inline decorative colors are gradient stat bars, accent borders, rgba backgrounds — self-colored, visible in both modes
- 341 canvas colors are informational — canvases paint own dark backgrounds with fillRect; canvas-helper.js adoption remains opt-in
- Run locally: `python3 dark_mode_audit.py` from project root

### 5. Visual QA Pass — IN PROGRESS (Session 9)
- ~~Automated QA script (`qa_heroquest.py`) — 8 checks across all 50 HTML files~~ ✅
- ~~Playwright screenshot matrix (`screenshot_matrix.py`) — 300 screenshots captured~~ ✅
- ~~Bugs found and fixed by QA script:~~ ✅
  - `heroquest_online_play.html` — `</mermaid>` → `</div>` (unclosed div)
  - `heroquest_digital_toolkit.html` — `rgba(83,52,131,0.3)` → `var(--accent-muted)`, `#7209b7` → `var(--accent, #7209b7)`
  - `heroquest_spirit_queens_torment.html` — 2× `color: #ffffff; text-shadow:...` → `color: var(--text)` (white text invisible on light mode)
  - `heroquest_legendary_heroes.html` — Knight hero-title `color: #000` on `background: #ffd700` confirmed as acceptable self-colored decorative pair (false positive)
- Screenshot review via `screenshots/review.html` contact sheet — **IN PROGRESS**
- Screenshots: 50 pages × 3 viewports (960/768/480) × 2 themes (light/dark) = 300 PNGs
- Review tool features: search filter, viewport/theme toggles, click-to-expand, shift+click lightbox
- `.gitignore` added to exclude `screenshots/`, `qa_heroquest.py`, `screenshot_matrix.py`
- Old utility scripts deleted: `audit_critical.py`, `find_text_colors.py`, `dark_mode_audit.py`

### ~~6. Potential Further Improvements~~ ✅ DONE (Session 7)
- ~~Simplify redundant dark mode overrides in main.css~~ ✅
- ~~Canvas dark mode: add isDark checks + MutationObserver for theme-change redraws~~ ✅
- ~~SVG dark mode text overrides~~ ✅ (no inline SVGs found — non-issue)
- ~~Consider whether some custom classes should be promoted to main.css as shared components~~ ✅

### 7. SVG & Canvas Visual Enhancement Pass — COMPLETE
Goal: Add SVG diagrams and canvas illustrations to content pages where visuals would enhance understanding — same approach used across TypeScript, ICRPG, and other Ray course projects.

Directive: Read each page, identify sections where a diagram/illustration/chart would genuinely improve learning, then add inline SVGs (preferred — they use CSS vars for dark mode) or canvas elements with unique IDs. All SVG IDs use `hq_<pageshort>_<description>` naming convention.

**Completed:**
- `heroquest_basics.html` ✅ — 4 SVGs added (Session 7):
  - `hq_basics_hero_compare` — horizontal bar chart comparing all 4 heroes (Attack/Defend/Body/Mind)
  - `hq_basics_dice_faces` — visual cards showing Skull, Shield, and Blank dice results
  - `hq_basics_dungeon_layout` — top-down dungeon map (corridor → door → room/trap/monster → secret door → treasure room) with legend
  - `hq_basics_turn_flow` — visual timeline: Hero Phase (Move→Attack→Search→Spell) → Evil Wizard Phase (Move→Attack→Reveal) with loop-back

**Remaining (in nav order):**
- `heroquest_dungeon_mastering.html` ✅ — 3 SVGs added (Session 8):
  - `hq_dm_player_types` — 2×2 card grid of 4 player archetypes with priority bars showing combat/puzzle/loot/story weighting
  - `hq_dm_tension_curve` — ideal adventure pacing wave with labeled phases (Explore→Fight→Rest→Boss→Reward→Climax) and frustration/boredom danger zones
  - `hq_dm_spotlight_wheel` — DM hub-and-spoke diagram with 4 heroes and rotation arrows showing spotlight cycling
- `heroquest_advanced_combat.html` ✅ — 4 SVGs added (Session 8):
  - `hq_combat_hero_roles` — formation diagram with front/mid/back line zones and hero placement
  - `hq_combat_pincer` — tactical pincer movement with flanking paths from Elf/Dwarf around enemy cluster
  - `hq_combat_target_priority` — threat triage circles (Priority 1 Chaos Warrior → 2 Fimir → 3 Goblins) with size-coded rings
  - `hq_combat_dice_odds` — horizontal bar chart showing skull probability for 1–4 dice (33%/56%/70%/80%)
- `heroquest_magic_spells.html` ✅ — 1 SVG added (Session 8):
  - `hq_magic_spell_compare` — 4-spell comparison matrix with bars for damage/defense/utility/urgency across Ball of Flame, Wind, Rock Skin, Healing
- `heroquest_treasure_progression.html` ✅ — no SVGs needed (Session 8): page already has 4 canvases + mermaid + interactive simulator; content is reward philosophy, not spatial/structural
- `heroquest_original_quests.html` ✅ — no SVGs needed (Session 8): page already has 3 canvases + mermaid + interactive quest explorer; content is quest analysis and strategy advice
- Hero tutorials (all 12) ✅ — no SVGs needed (Session 8): each already has 5–10 canvases + 2–3 mermaids
  - barbarian (5c/2m), dwarf (6c/3m), elf (8c/3m), wizard (8c/2m), warlock (9c/3m), bard (9c/3m)
  - knight (10c/2m), berserker (9c/2m), explorer (10c/2m), monk (10c/2m), rogue (10c/2m), druid (10c/3m)
- Digital/Advanced pages (all 4) ✅ — no SVGs needed (Session 8): interactive HTML widgets + canvases + mermaids cover visual needs
  - digital_toolkit (0c/1m + interactive dice/stats widgets), custom_heroes_monsters (1c/1m), legendary_heroes (1c/1m), online_play (1c/1m)
- Expansion pages (all 10) ✅ — no SVGs needed (Session 8): most have 4–5 canvases + 1 mermaid; narrative/descriptive content
  - kellars_keep (4c/1m), return_witch_lord (5c/1m), prophecy_telor (0c/0m — narrative), spirit_queens_torment (5c/1m)
  - against_ogre_horde (5c/1m), frozen_horror (5c/1m), mage_of_mirror (5c/1m), rise_dread_moon (4c/1m)
  - jungles_delthrak (5c/1m), rise_dread_moon_knight (2c/1m + interactive HTML)
- Lore pages (all 17) ✅ — no SVGs needed (Session 8): each has 1 canvas + 1 mermaid; worldbuilding/narrative content where text IS the primary medium

### Session 8 — SVG Visual Enhancement Pass: Audit & Completion (April 2026)

**Approach Correction:**
- Initial approach was adding a fixed 4 SVGs per page. Corrected mid-session to evaluate each page individually based on whether a visual genuinely adds something text can’t convey.
- Criteria: Does the concept involve spatial relationships, data comparison, tactical positioning, or probability? If yes, SVG adds value. If the content is narrative, philosophical, or already well-served by existing canvases/mermaids, skip.

**SVGs Added (8 total across 3 pages):**
- `heroquest_dungeon_mastering.html` — 3 SVGs (player archetypes with priority bars, tension pacing curve, spotlight rotation wheel)
- `heroquest_advanced_combat.html` — 4 SVGs (formation zones, pincer movement, target triage, dice probability)
- `heroquest_magic_spells.html` — 1 SVG (spell comparison matrix)

**Full Site Audit Results (all remaining 46 pages evaluated, 0 additional SVGs needed):**
- Foundation pages (treasure_progression, original_quests): already have 3–4 canvases + mermaids + interactive widgets
- Hero tutorials (12 files): already have 5–10 canvases + 2–3 mermaids each
- Digital/Advanced (4 files): interactive HTML widgets + canvases cover visual needs
- Expansion pages (10 files): most have 4–5 canvases + 1 mermaid; narrative content
- Lore pages (17 files): each has 1 canvas + 1 mermaid; worldbuilding text is the primary medium

**1 SVG removed during audit:**
- `hq_dm_difficulty_scale` removed from dungeon_mastering — the Goldilocks text already conveyed the concept clearly; gradient bar was decorative not informative

**Task 7 is now COMPLETE.** All 49 content pages have been evaluated. The original status.md significantly overstated the need for SVG additions — most pages were already visually well-served by their existing canvases, mermaid diagrams, and interactive HTML elements.

### Session 7 — main.css Cleanup + Canvas Helper + Shared Components (April 2026)

**main.css Redundant Dark Override Removal:**
- Removed ALL 20 `[data-theme="dark"]` override rules (body, h1-h4, strong, code/pre, a, h3 a, blockquote, table/td/tr/th, th, .container, .mermaid*, img, .comment-block) — these were redundant because base styles already use CSS variables
- Fixed base styles that still had hardcoded values:
  - Table reset: `#333333` → `var(--table-border)`, added `color: var(--text)`, `th` gets `background-color: var(--card-bg)`
  - `h3 a { color: white }` → `color: var(--heading-text)`
  - `.comment-block { border-left: #1890ff }` → `var(--link-color)`
  - Mermaid base: all hardcoded `rgb()` values → CSS variables (`--mermaid-bg`, `--mermaid-text`, etc.)
  - `img` gets `background-color: var(--card-bg)` in base
- Consolidated duplicate rules: 7 `code` margin rules → 1, duplicate `table` → 1, duplicate `footer` → 1, duplicate `p code` removed
- Added 4 new CSS variables: `--accent`, `--accent-muted`, `--tag-bg`, `--tag-text`

**Shared Component Classes Promoted to main.css (~80+ classes):**
- Cards: `.quest-card`, `.spell-card`, `.hero-card`, `.artifact-card`, `.villain-card`, `.dungeon-card`, `.kingdom-card`, `.event-card`, `.divine-card`, `.mentor-card`, `.spirit-card`, `.ogre-card`, `.frost-card`, `.mirror-card`, `.witch-card`, `.prophecy-card`, `.tool-panel`
- Stat display: `.stat-card`, `.stat-row`, `.stat-label`, `.stat-value`
- Tags/badges: 40+ tag classes (`.impact-tag`, `.domain-tag`, `.teaching-tag`, etc.)
- Progress bars: `.power-fill`, `.power-label`
- Callout boxes: `.analogy-box`, `.practice-box`, `.beginner-tip`, `.combat-example`, `.spell-mastery`, etc. (35+ classes)
- Lore scrolls/tomes: `.ancient-scroll`, `.dark-chronicle`, `.celestial-tome`, etc. (16 classes)
- Quest checklist: `.quest-item`, `.quest-checkbox`, `.quest-text`
- Tool panel: `.tool-title`, `.mod-btn`

**Canvas Dark Mode Helper (`canvas-helper.js`):**
- New shared script: `hqCanvas.colors()` returns theme-aware color palette
- `hqCanvas.isDark()` checks current theme
- `hqCanvas.onThemeChange(fn)` registers draw functions for auto-redraw
- MutationObserver on `<html data-theme>` fires all registered callbacks on toggle
- Light/dark palettes with named colors: bg, text, accent, gold, danger, success, etc.
- **Opt-in adoption**: pages add `<script src="canvas-helper.js"></script>` and update draw functions to use `hqCanvas.colors()` + `hqCanvas.onThemeChange()`

**SVG Dark Mode Audit:**
- Scanned all 50 HTML files — zero inline `<svg>` elements found
- SVG dark mode text overrides confirmed as non-issue

**Canvas Dark Mode Audit (17 files, 44+ canvas elements):**
- 9 files (35 canvases) have self-contained dark backgrounds (fillRect full canvas) — fine in both modes
- 6 lore files have transparent-bg canvases with bright/saturated colors — mostly fine
- 1 file (barbarian tutorial) has black/white text on transparent canvas — candidate for canvas-helper adoption
- Canvas helper is ready for gradual adoption; no canvas JS was modified in this session

## How Remaining Files Were Processed
Session 6 used a Python script (`strip_styles.py`) run locally in WSL to batch-strip all 8 remaining expansion files. The script uses `re.sub(r"\n<style>.*?</style>\n", "\n", content, re.DOTALL)` — same regex pattern as all prior sessions. Script can be deleted after use.

## Architecture Notes
- `nav.js` is an IIFE that injects sticky nav bar (Home, Ray's House of Fun, Contact), dark/light toggle, and prev/next footer on all pages
- Theme state: `localStorage.getItem('hq-theme')`, applied as `data-theme` attribute on `<html>`
- All nav/theme CSS lives inside `nav.js` (injected via `document.head.appendChild(style)`)
- `index.html` uses scoped inline styles (card grid layout, gradient hero, stats counters); NOT targeted for cleanup — it's already modern and self-contained
- `main.css` has CSS variables for light/dark mode, responsive breakpoints at 768px and 480px
- `canvas-helper.js` provides opt-in dark mode support for canvas elements (MutationObserver + color palette)
- Navigation: 49 entries in `nav.js` grouped by: Foundation (6) → Hero Classes (12) → Digital Tools (1) → Custom & Advanced (3) → Expansions (10) → Lore (17)
- `nav.js` matcher uses `normalize()` to strip `.html` for Netlify pretty URL support
- `main.css` `.container` class: max-width 960px, centered, card-bg background, 48px padding, rounded corners, shadow, border
- `dark_mode_audit.py` — v2 audit script scanning all 49 HTML + CSS for hardcoded colors; categorizes as text/decorative/canvas; run with `python3 dark_mode_audit.py`
- Utility scripts (`find_text_colors.py`, `audit_critical.py`, `strip_styles.py`) — deleted after use
- QA tools (`qa_heroquest.py`, `screenshot_matrix.py`) — gitignored, deletable after visual QA pass
- `screenshots/` folder — gitignored, ~300 PNGs + `review.html` contact sheet for visual QA
- `.gitignore` — excludes screenshots/ and QA utility scripts
