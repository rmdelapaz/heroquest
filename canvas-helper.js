/**
 * HeroQuest Canvas Dark Mode Helper
 * 
 * Provides theme-aware colors for canvas drawing and auto-redraws
 * canvases when the light/dark theme toggles.
 *
 * USAGE:
 *   1. Include this script BEFORE your canvas drawing code:
 *      <script src="canvas-helper.js"></script>
 *
 *   2. Get theme-aware colors in your draw functions:
 *      const colors = hqCanvas.colors();
 *      ctx.fillStyle = colors.bg;       // page background
 *      ctx.fillStyle = colors.cardBg;   // card/surface background
 *      ctx.fillStyle = colors.text;     // primary text
 *      ctx.fillStyle = colors.muted;    // secondary/muted text
 *      ctx.fillStyle = colors.accent;   // accent / link color
 *      ctx.fillStyle = colors.border;   // border / divider lines
 *      ctx.fillStyle = colors.heading;  // heading background
 *      ctx.fillStyle = colors.headingText; // heading text
 *
 *   3. Register draw functions for auto-redraw on theme change:
 *      hqCanvas.onThemeChange(drawMyCanvas);
 *      hqCanvas.onThemeChange(drawAnotherCanvas);
 *
 *   4. Check current theme:
 *      if (hqCanvas.isDark()) { ... }
 */
(function () {
  'use strict';

  const lightPalette = {
    bg: '#f8fafc',
    cardBg: '#ffffff',
    text: '#334155',
    muted: '#64748b',
    accent: '#3b82f6',
    border: '#e2e8f0',
    heading: '#3b82f6',
    headingText: '#ffffff',
    codeBg: '#f1f5f9',
    codeText: '#228b22',
    gold: '#ffd700',
    danger: '#ef4444',
    success: '#22c55e',
    warning: '#f59e0b',
  };

  const darkPalette = {
    bg: '#0f172a',
    cardBg: '#1e293b',
    text: '#cbd5e1',
    muted: '#94a3b8',
    accent: '#60a5fa',
    border: '#334155',
    heading: '#1d4ed8',
    headingText: '#e2e8f0',
    codeBg: '#1e293b',
    codeText: '#86efac',
    gold: '#fbbf24',
    danger: '#f87171',
    success: '#4ade80',
    warning: '#fbbf24',
  };

  const callbacks = [];

  function isDark() {
    return document.documentElement.getAttribute('data-theme') === 'dark';
  }

  function colors() {
    return isDark() ? { ...darkPalette } : { ...lightPalette };
  }

  function onThemeChange(fn) {
    if (typeof fn === 'function') {
      callbacks.push(fn);
    }
  }

  /* Watch for theme changes via MutationObserver */
  const observer = new MutationObserver(function (mutations) {
    for (const m of mutations) {
      if (m.type === 'attributes' && m.attributeName === 'data-theme') {
        callbacks.forEach(function (fn) {
          try { fn(); } catch (e) { console.warn('hqCanvas redraw error:', e); }
        });
        break;
      }
    }
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme'],
  });

  /* Expose global API */
  window.hqCanvas = {
    isDark: isDark,
    colors: colors,
    onThemeChange: onThemeChange,
    light: lightPalette,
    dark: darkPalette,
  };
})();
