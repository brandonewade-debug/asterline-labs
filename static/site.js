(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    const close = () => {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
    };
    toggle.addEventListener('click', () => {
      const next = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(next));
      nav.classList.toggle('open', next);
    });
    nav.addEventListener('click', event => {
      if (event.target.closest('a')) close();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') close();
    });
    document.addEventListener('click', event => {
      if (!nav.contains(event.target) && !toggle.contains(event.target)) close();
    });
  }

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
