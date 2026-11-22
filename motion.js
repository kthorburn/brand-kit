/*
  brand-kit motion. Landing pages only (see BRAND.md, section 8).

  One idea: every element with data-bk-progress gets a CSS variable --p that
  runs from 0 to 1 as the page scrolls. All the effects are plain CSS built on
  that number (motion.css), so a new effect needs no new JavaScript.

    data-bk-progress          0 as the element enters the bottom of the
                              screen, 1 as it leaves the top
    data-bk-progress="pin"    for a tall .bk-stage: 0 when it reaches the top
                              of the screen, 1 when its pinned child lets go

  Also:
    data-bk-reveal            rises into place the first time it is seen
    data-bk-words             text fills in word by word with --p
    data-bk-count="1212"      counts up to the number the first time it is seen
    .bk-steps                 marks the step nearest the middle of the screen

  With reduced motion, or without this script, the page is a normal static
  page with everything visible.
*/
(function () {
  var root = document.documentElement;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  root.classList.add('bk-motion');

  var all = function (sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); };
  var clamp = function (n) { return n < 0 ? 0 : n > 1 ? 1 : n; };

  all('[data-bk-words]').forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', words.join(' '));
    el.style.setProperty('--n', words.length);
    el.innerHTML = words.map(function (w, i) {
      return '<span class="bk-w" aria-hidden="true" style="--i:' + i + '">' + w.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</span>';
    }).join(' ');
  });

  var tracked = all('[data-bk-progress]');
  var stepSets = all('.bk-steps').map(function (el) { return { el: el, steps: all('.bk-step', el) }; });
  var queued = false;

  function update() {
    queued = false;
    var vh = window.innerHeight;
    tracked.forEach(function (el) {
      var r = el.getBoundingClientRect();
      var p = el.dataset.bkProgress === 'pin'
        ? -r.top / Math.max(1, r.height - vh)
        : (vh - r.top) / (vh + r.height);
      el.style.setProperty('--p', clamp(p).toFixed(4));
    });
    stepSets.forEach(function (set) {
      var best = 0, bestDist = Infinity;
      set.steps.forEach(function (s, i) {
        var r = s.getBoundingClientRect();
        var d = Math.abs(r.top + r.height / 2 - vh * 0.55);
        if (d < bestDist) { bestDist = d; best = i; }
      });
      set.el.dataset.step = best;
      set.steps.forEach(function (s, i) { s.classList.toggle('is-active', i === best); });
    });
  }
  // The hero media starts just below the hero copy, whatever its height.
  function measure() {
    all('.bk-stage').forEach(function (stage) {
      var copy = stage.querySelector('.bk-stage-copy');
      if (copy) stage.style.setProperty('--bk-stage-split', (copy.offsetHeight + 8) + 'px');
    });
    queue();
  }
  function queue() { if (!queued) { queued = true; requestAnimationFrame(update); } }
  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', measure);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
  measure();
  update();

  function countUp(el) {
    var target = parseFloat(el.dataset.bkCount), start = null, dur = 1200;
    function frame(t) {
      if (start === null) start = t;
      var k = clamp((t - start) / dur), eased = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(target * eased).toLocaleString('en-US');
      if (k < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  if (!('IntersectionObserver' in window)) return;
  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      seen.unobserve(e.target);
      e.target.classList.remove('bk-pre');
      if (e.target.dataset.bkCount) countUp(e.target);
    });
  }, { rootMargin: '0px 0px -12% 0px' });

  // Only hide what starts below the first screen, so the page is complete on load.
  all('[data-bk-reveal]').forEach(function (el) {
    if (el.getBoundingClientRect().top > window.innerHeight) { el.classList.add('bk-pre'); seen.observe(el); }
  });
  all('[data-bk-count]').forEach(function (el) { seen.observe(el); });
})();
