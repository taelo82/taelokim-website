// Reading progress + click-to-load YouTube facades.
// The facade keeps the YouTube iframe (and its ~700KB of JS) out of the
// initial load, so LCP stays fast and Google doesn't dock the page for it.

(function () {
  const bar = document.querySelector('.progress');
  if (bar && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
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

  document.querySelectorAll('.video-embed[data-video]').forEach((el) => {
    el.addEventListener('click', () => {
      const id = el.dataset.video;
      const t = el.dataset.start ? '&start=' + el.dataset.start : '';
      const f = document.createElement('iframe');
      f.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0${t}`;
      f.title = el.dataset.title || 'YouTube video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      el.replaceChildren(f);
    }, { once: true });
  });
})();
