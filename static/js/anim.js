// ===== 动态效果：滚动入场 + 点图放大 =====
// 借鉴 jangrundl.de 的 .reveal / IntersectionObserver 滚动淡入上浮
// 借鉴 sangluisme.github.io 的 medium-zoom 点图全屏放大
(function () {
  'use strict';

  // 1) 滚动入场动画
  var revealEls = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  // 2) 全屏点图放大（medium-zoom 风格）
  var overlay = document.getElementById('zoom-overlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = 'zoom-overlay';
    overlay.className = 'zoom-overlay';
    var img = document.createElement('img');
    overlay.appendChild(img);
    document.body.appendChild(overlay);
  }
  var zoomImg = overlay.querySelector('img');

  function openZoom(src, alt) {
    zoomImg.src = src;
    if (alt) zoomImg.alt = alt;
    overlay.classList.add('open');
  }
  function closeZoom() { overlay.classList.remove('open'); }

  document.querySelectorAll('.zoomable').forEach(function (el) {
    el.addEventListener('click', function () {
      openZoom(el.currentSrc || el.src, el.alt || '');
    });
  });
  overlay.addEventListener('click', closeZoom);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeZoom();
  });

  // 3) 移动端菜单开关（借鉴 jangrundl.de 的 nav-toggle）
  var navToggle = document.querySelector('.nav-toggle');
  var menuOverlay = document.getElementById('menu-overlay');
  if (navToggle && menuOverlay) {
    function closeMenu() {
      menuOverlay.classList.remove('open');
      navToggle.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    }
    navToggle.addEventListener('click', function () {
      var open = menuOverlay.classList.toggle('open');
      navToggle.classList.toggle('open', open);
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menuOverlay.addEventListener('click', function (e) {
      if (e.target === menuOverlay || e.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });
  }
})();
