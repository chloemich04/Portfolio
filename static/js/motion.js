/* Progressive enhancement: content stays visible without JavaScript. */
(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!('IntersectionObserver' in window) || !Element.prototype.animate) return;

  let observer;
  const animations = new Set();
  const seen = new WeakSet();
  const targets = document.querySelectorAll(
    '.hero-copy > *, .portrait-composition, .page-heading > *, ' +
    '.section-heading, .project-card, .about-grid > *, .skills-grid > *, ' +
    '.contact-card, .connect-banner'
  );

  function start() {
    observer?.disconnect();
    if (preference.matches) {
      animations.forEach(animation => animation.cancel());
      animations.clear();
      return;
    }
    observer = new IntersectionObserver(entries => {
      // A queued observer callback may arrive after a preference change.
      if (preference.matches) return;
      let order = 0;
      entries.forEach(entry => {
        if (!entry.isIntersecting || seen.has(entry.target)) return;
        const element = entry.target;
        seen.add(element);
        observer.unobserve(element);
        if (element.contains(document.activeElement)) return;
        const animation = element.animate([
          { opacity: 0, transform: 'translateY(18px)' },
          { opacity: 1, transform: 'translateY(0)' }
        ], {
          duration: 620,
          delay: Math.min(order++ * 65, 195),
          easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
          fill: 'backwards'
        });
        animations.add(animation);
        animation.finished.catch(() => {}).finally(() => animations.delete(animation));
      });
    }, { threshold: 0.08 });
    targets.forEach(element => {
      if (!seen.has(element)) observer.observe(element);
    });
  }

  // Keyboard navigation should never land on fading or moving content.
  document.addEventListener('focusin', () => {
    animations.forEach(animation => {
      if (animation.effect?.target.contains(document.activeElement)) animation.cancel();
    });
  });
  preference.addEventListener('change', start);
  start();
})();
