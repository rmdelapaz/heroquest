(function () {
  'use strict';

  /* ── Page ordering for prev/next ── */
  const pages = [
    // Foundation
    { file: 'heroquest_basics.html', title: 'HeroQuest Basics', icon: '🎯' },
    { file: 'heroquest_dungeon_mastering.html', title: 'Dungeon Mastering', icon: '🎭' },
    { file: 'heroquest_advanced_combat.html', title: 'Advanced Combat', icon: '⚔️' },
    { file: 'heroquest_magic_spells.html', title: 'Magic & Spells', icon: '🔮' },
    { file: 'heroquest_treasure_progression.html', title: 'Treasure & Progression', icon: '💰' },
    { file: 'heroquest_original_quests.html', title: 'Original Quests', icon: '🗡️' },
    // Hero Classes
    { file: 'heroquest_barbarian_tutorial.html', title: 'Barbarian', icon: '🪓' },
    { file: 'heroquest_dwarf_tutorial.html', title: 'Dwarf', icon: '⚒️' },
    { file: 'heroquest_elf_tutorial.html', title: 'Elf', icon: '🏹' },
    { file: 'heroquest_wizard_tutorial.html', title: 'Wizard', icon: '🧙' },
    { file: 'heroquest_warlock_tutorial.html', title: 'Warlock', icon: '🌙' },
    { file: 'heroquest_bard_tutorial.html', title: 'Bard', icon: '🎵' },
    { file: 'heroquest_knight_tutorial.html', title: 'Knight', icon: '🛡️' },
    { file: 'heroquest_berserker_tutorial.html', title: 'Berserker', icon: '⚡' },
    { file: 'heroquest_explorer_tutorial.html', title: 'Explorer', icon: '🗺️' },
    { file: 'heroquest_monk_tutorial.html', title: 'Monk', icon: '🧘' },
    { file: 'heroquest_rogue_tutorial.html', title: 'Rogue', icon: '🗡️' },
    { file: 'heroquest_druid_tutorial.html', title: 'Druid', icon: '🌿' },
    // Digital Tools
    { file: 'heroquest_digital_toolkit.html', title: 'Digital Toolkit', icon: '🛠️' },
    { file: 'heroquest_character_sheet.html', title: 'Character Sheet', icon: '📜' },
    // Custom & Advanced
    { file: 'heroquest_custom_heroes_monsters.html', title: 'Custom Heroes & Monsters', icon: '🦸' },
    { file: 'heroquest_legendary_heroes.html', title: 'Legendary Heroes', icon: '🏆' },
    { file: 'heroquest_online_play.html', title: 'Online Play', icon: '🌐' },
    // Expansions
    { file: 'heroquest_kellars_keep.html', title: "Kellar's Keep", icon: '🏰' },
    { file: 'heroquest_return_witch_lord.html', title: 'Return of the Witch Lord', icon: '👑' },
    { file: 'heroquest_prophecy_telor.html', title: 'Prophecy of Telor', icon: '🔮' },
    { file: 'heroquest_spirit_queens_torment.html', title: "Spirit Queen's Torment", icon: '⚔️' },
    { file: 'heroquest_against_ogre_horde.html', title: 'Against the Ogre Horde', icon: '🛡️' },
    { file: 'heroquest_frozen_horror.html', title: 'The Frozen Horror', icon: '❄️' },
    { file: 'heroquest_mage_of_mirror.html', title: 'Mage of the Mirror', icon: '🪞' },
    { file: 'heroquest_rise_dread_moon.html', title: 'Rise of the Dread Moon', icon: '🌙' },
    { file: 'heroquest_jungles_delthrak.html', title: 'Jungles of Delthrak', icon: '🌿' },
    { file: 'heroquest_rise_dread_moon_knight.html', title: 'Dread Moon Knight', icon: '🌑' },
    // Lore
    { file: 'heroquest_lore_foundations.html', title: 'Lore: Foundations', icon: '📜' },
    { file: 'heroquest_lore_dark_forces.html', title: 'Lore: Dark Forces', icon: '🖤' },
    { file: 'heroquest_lore_kingdoms_regions.html', title: 'Lore: Kingdoms & Regions', icon: '🗺️' },
    { file: 'heroquest_lore_great_events.html', title: 'Lore: Great Events', icon: '⚡' },
    { file: 'heroquest_lore_cosmic_forces.html', title: 'Lore: Cosmic Forces', icon: '✨' },
    { file: 'heroquest_lore_mentors_questgivers.html', title: 'Lore: Mentors & Questgivers', icon: '🧙' },
    { file: 'heroquest_lore_ancient_dungeons.html', title: 'Lore: Ancient Dungeons', icon: '🏚️' },
    { file: 'heroquest_lore_magic_artifacts.html', title: 'Lore: Magic Artifacts', icon: '💎' },
    { file: 'heroquest_lore_kellars_keep.html', title: "Lore: Kellar's Keep", icon: '🏰' },
    { file: 'heroquest_lore_return_witch_lord.html', title: 'Lore: Witch Lord', icon: '👑' },
    { file: 'heroquest_lore_prophecy_telor.html', title: 'Lore: Prophecy of Telor', icon: '🔮' },
    { file: 'heroquest_lore_spirit_queens_torment.html', title: "Lore: Spirit Queen's Torment", icon: '⚔️' },
    { file: 'heroquest_lore_against_ogre_horde.html', title: 'Lore: Ogre Horde', icon: '🛡️' },
    { file: 'heroquest_lore_frozen_horror.html', title: 'Lore: Frozen Horror', icon: '❄️' },
    { file: 'heroquest_lore_mage_of_the_mirror.html', title: 'Lore: Mage of the Mirror', icon: '🪞' },
    { file: 'heroquest_lore_rise_dread_moon.html', title: 'Lore: Dread Moon', icon: '🌙' },
    { file: 'heroquest_lore_jungles_delthrak.html', title: 'Lore: Jungles of Delthrak', icon: '🌿' },
  ];

  /* ── Dark mode ── */
  const savedTheme = localStorage.getItem('hq-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('hq-theme', next);
    const btn = document.getElementById('hq-theme-toggle');
    if (btn) btn.textContent = next === 'dark' ? '☀️ Light' : '🌙 Dark';
  }

  /* ── Detect current page ── */
  const path = window.location.pathname;
  const currentFile = path.substring(path.lastIndexOf('/') + 1) || 'index.html';
  const normalize = (f) => f.replace(/\.html$/, '');
  const isIndex = currentFile === 'index.html' || currentFile === '' || currentFile === 'index';

  /* ── Build top navbar ── */
  const nav = document.createElement('nav');
  nav.id = 'hq-topnav';
  nav.innerHTML = `
    <div class="hq-nav-inner">
      <a href="/index.html" class="hq-nav-brand">⚔️ HeroQuest</a>
      <button class="hq-nav-hamburger" id="hq-hamburger" aria-label="Toggle menu">☰</button>
      <div class="hq-nav-links" id="hq-nav-links">
        <a href="/index.html">🏠 Home</a>
        <a href="https://rays-home.netlify.app/" target="_blank" rel="noopener">🏡 Ray's House of Fun</a>
        <a href="https://rays-home.netlify.app/contact" target="_blank" rel="noopener">✉️ Contact</a>
        <button id="hq-theme-toggle" class="hq-theme-btn">${savedTheme === 'dark' ? '☀️ Light' : '🌙 Dark'}</button>
      </div>
    </div>
  `;
  document.body.prepend(nav);

  /* Hamburger toggle */
  document.getElementById('hq-hamburger').addEventListener('click', function () {
    document.getElementById('hq-nav-links').classList.toggle('open');
  });

  /* Theme button */
  document.getElementById('hq-theme-toggle').addEventListener('click', toggleTheme);

  /* ── Build prev/next nav (non-index pages only) ── */
  if (!isIndex) {
    const idx = pages.findIndex(p => normalize(p.file) === normalize(currentFile));
    if (idx !== -1) {
      const prev = idx > 0 ? pages[idx - 1] : null;
      const next = idx < pages.length - 1 ? pages[idx + 1] : null;

      const bottomNav = document.createElement('nav');
      bottomNav.className = 'hq-page-nav';
      bottomNav.innerHTML = `
        ${prev ? `<a href="${prev.file}" class="hq-page-nav-link hq-prev"><span class="hq-page-nav-dir">← Previous</span><span class="hq-page-nav-title">${prev.icon} ${prev.title}</span></a>` : '<span></span>'}
        <a href="/index.html" class="hq-page-nav-home">⚔️ All Guides</a>
        ${next ? `<a href="${next.file}" class="hq-page-nav-link hq-next"><span class="hq-page-nav-dir">Next →</span><span class="hq-page-nav-title">${next.icon} ${next.title}</span></a>` : '<span></span>'}
      `;

      /* Insert before </body> or after last container */
      const container = document.querySelector('.container') || document.body;
      if (container !== document.body) {
        container.parentNode.insertBefore(bottomNav, container.nextSibling);
      } else {
        document.body.appendChild(bottomNav);
      }
    }
  }

  /* ── Inject navbar + prev/next CSS ── */
  const style = document.createElement('style');
  style.textContent = `
    /* ── Top Navbar ── */
    #hq-topnav {
      position: sticky; top: 0; z-index: 9999;
      background: var(--nav-bg, #1e293b);
      border-bottom: 2px solid var(--nav-border, #3b82f6);
      padding: 0; margin: 0;
      font-family: 'Segoe UI', system-ui, sans-serif;
    }
    .hq-nav-inner {
      max-width: 1200px; margin: 0 auto;
      display: flex; align-items: center; justify-content: space-between;
      padding: 10px 20px;
    }
    .hq-nav-brand {
      font-size: 1.25rem; font-weight: 700;
      color: #fff !important; text-decoration: none !important;
      border-bottom: none !important;
    }
    .hq-nav-links {
      display: flex; align-items: center; gap: 8px;
    }
    .hq-nav-links a {
      color: #cbd5e1 !important; text-decoration: none !important;
      padding: 6px 14px; border-radius: 6px; font-size: 0.9rem;
      font-weight: 500; transition: background 0.2s, color 0.2s;
      border-bottom: none !important; white-space: nowrap;
    }
    .hq-nav-links a:hover { background: rgba(255,255,255,0.1); color: #fff !important; }
    .hq-theme-btn {
      background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
      color: #cbd5e1; padding: 6px 14px; border-radius: 6px; cursor: pointer;
      font-size: 0.9rem; font-weight: 500; transition: background 0.2s;
      white-space: nowrap;
    }
    .hq-theme-btn:hover { background: rgba(255,255,255,0.2); color: #fff; }
    .hq-nav-hamburger {
      display: none; background: none; border: none;
      color: #fff; font-size: 1.5rem; cursor: pointer; padding: 4px 8px;
    }
    @media (max-width: 700px) {
      .hq-nav-hamburger { display: block; }
      .hq-nav-links {
        display: none; flex-direction: column;
        position: absolute; top: 100%; left: 0; right: 0;
        background: var(--nav-bg, #1e293b);
        padding: 12px 20px; gap: 4px;
        border-bottom: 2px solid var(--nav-border, #3b82f6);
      }
      .hq-nav-links.open { display: flex; }
      .hq-nav-links a, .hq-theme-btn { width: 100%; text-align: left; box-sizing: border-box; }
    }

    /* ── Bottom prev/next nav ── */
    .hq-page-nav {
      display: grid; grid-template-columns: 1fr auto 1fr;
      gap: 16px; align-items: center;
      max-width: 1200px; margin: 40px auto 20px;
      padding: 0 20px; font-family: 'Segoe UI', system-ui, sans-serif;
    }
    .hq-page-nav-link {
      display: flex; flex-direction: column; gap: 4px;
      padding: 16px 20px; border-radius: 10px;
      text-decoration: none !important; border-bottom: none !important;
      background: var(--card-bg, #f8fafc);
      border: 1px solid var(--border, #e2e8f0);
      transition: box-shadow 0.2s, transform 0.2s;
    }
    .hq-page-nav-link:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    .hq-prev { text-align: left; }
    .hq-next { text-align: right; justify-self: end; }
    .hq-page-nav-dir {
      font-size: 0.8rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.5px; color: var(--text-muted, #64748b);
    }
    .hq-page-nav-title {
      font-size: 1rem; font-weight: 600;
      color: var(--link-color, #3b82f6) !important;
    }
    .hq-page-nav-home {
      text-decoration: none !important; border-bottom: none !important;
      font-weight: 600; color: var(--link-color, #3b82f6) !important;
      padding: 8px 16px; border-radius: 6px;
      border: 1px solid var(--border, #e2e8f0);
      background: var(--card-bg, #f8fafc);
      white-space: nowrap;
    }
    .hq-page-nav-home:hover { background: var(--link-color, #3b82f6); color: #fff !important; }
    @media (max-width: 700px) {
      .hq-page-nav {
        grid-template-columns: 1fr;
        gap: 10px;
      }
      .hq-next { justify-self: stretch; text-align: left; }
      .hq-page-nav-home { text-align: center; }
    }

    /* Push body down so sticky nav doesn't overlap */
    body { padding-top: 0 !important; }
  `;
  document.head.appendChild(style);
})();
