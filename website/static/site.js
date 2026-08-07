(() => {
  const root = document.documentElement;
  const button = document.querySelector('.menu');
  const mobile = document.querySelector('.mobile');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  const closeMenu = () => {
    if (!button || !mobile) return;
    mobile.classList.remove('open');
    mobile.hidden = true;
    button.setAttribute('aria-expanded', 'false');
    root.classList.remove('menu-open');
  };

  if (button && mobile) {
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      button.setAttribute('aria-expanded', String(open));
      mobile.hidden = !open;
      mobile.classList.toggle('open', open);
      root.classList.toggle('menu-open', open);
    });
    mobile.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        closeMenu();
        button.focus();
      }
    });
    window.addEventListener('resize', () => {
      if (window.innerWidth > 900) closeMenu();
    }, { passive: true });
  }

  const path = `${location.pathname.replace(/\/$/, '')}/`;
  document.querySelectorAll('.navlinks a, .mobile a').forEach(link => {
    const linkPath = `${new URL(link.href).pathname.replace(/\/$/, '')}/`;
    if (linkPath !== '/' && path.startsWith(linkPath)) {
      link.classList.add('current');
      link.setAttribute('aria-current', 'page');
    }
  });

  const reveals = [...document.querySelectorAll('.reveal')];
  if (reduceMotion.matches || !('IntersectionObserver' in window)) {
    reveals.forEach(element => element.classList.add('in'));
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const order = Math.min(Number(entry.target.dataset.reveal || 0), 5);
      entry.target.style.setProperty('--reveal-delay', `${order * 70}ms`);
      entry.target.classList.add('in');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  reveals.forEach(element => observer.observe(element));
})();
