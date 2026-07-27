// Reading progress, click-to-load YouTube facades, and a table of contents
// built from the article's own h2s.
//
// The facade keeps the YouTube iframe (and its ~700KB of JS) out of the
// initial load, so LCP stays fast and Google doesn't dock the page for it.

(function () {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Reading progress ──
  const bar = document.querySelector('.progress');
  if (bar && !reduced) {
    let ticking = false;
    const update = () => {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
      ticking = false;
    };
    addEventListener('scroll', () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // ── Video facades ──
  document.querySelectorAll('.video-embed[data-video]').forEach((el) => {
    const load = () => {
      const id = el.dataset.video;
      const t = el.dataset.start ? '&start=' + el.dataset.start : '';
      const f = document.createElement('iframe');
      f.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0${t}`;
      f.title = el.dataset.title || 'YouTube video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      el.replaceChildren(f);
    };
    el.addEventListener('click', load, { once: true });
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); load(); }
    }, { once: true });
  });

  // ── Table of contents ──
  // Skips the FAQ heading: it's a landmark, not a section you navigate to.
  const body = document.querySelector('.post-body');
  if (!body) return;
  const heads = [...body.querySelectorAll('h2[id]')].filter(h => !h.closest('.takeaways, .related'));
  if (heads.length < 4) return;

  const nav = document.createElement('nav');
  nav.className = 'toc';
  nav.setAttribute('aria-label', 'On this page');
  nav.innerHTML = '<div class="toc__label">On this page</div><ol></ol>';
  const ol = nav.querySelector('ol');

  heads.forEach((h) => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + h.id;
    // Section heads carry a decorative ::before tick; textContent ignores it.
    a.textContent = h.textContent.trim();
    li.append(a);
    ol.append(li);
  });
  document.body.append(nav);

  const links = new Map(heads.map((h, i) => [h, ol.children[i].firstChild]));
  let current = null;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      if (current) current.removeAttribute('data-active');
      current = links.get(e.target);
      if (current) current.setAttribute('data-active', '');
    });
  }, { rootMargin: '-90px 0px -70% 0px' });
  heads.forEach(h => io.observe(h));
})();
