/**
 * Face of Kolkata Photography — Interactive Controller
 * Dynamic Typewriter, Counter Animation, Mobile Drawer & Intake Estimator
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Drawer Navigation
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      drawer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (!drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
        drawer.classList.remove('open');
      }
    });

    drawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.remove('open');
      });
    });
  }

  // 2. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const phrases = [
      "Royal Bengali Wedding Cinematography",
      "Soulful Candid Storytelling in Dum Dum",
      "Pre-Wedding Poetry at Kolkata Landmarks",
      "Heirloom Fine-Art Album Craftsmanship"
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let speed = 90;

    function typeLoop() {
      const currentPhrase = phrases[phraseIdx];

      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
        speed = 45;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
        speed = 90;
      }

      if (!isDeleting && charIdx === currentPhrase.length) {
        isDeleting = true;
        speed = 2200; // Pause at full phrase
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        speed = 400; // Pause before typing next
      }

      setTimeout(typeLoop, speed);
    }

    typeLoop();
  }

  // 3. Counter Animation
  const counters = document.querySelectorAll('.telemetry-val');
  if (counters.length > 0) {
    let animated = false;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          counters.forEach(counter => {
            const rawTarget = counter.getAttribute('data-target');
            if (!rawTarget) return;
            const target = parseFloat(rawTarget);
            const isDecimal = rawTarget.includes('.');
            let count = 0;
            const step = target / 40;

            const timer = setInterval(() => {
              count += step;
              if (count >= target) {
                counter.textContent = isDecimal ? target.toFixed(1) : Math.floor(target) + (rawTarget.includes('+') ? '+' : '');
                clearInterval(timer);
              } else {
                counter.textContent = isDecimal ? count.toFixed(1) : Math.floor(count);
              }
            }, 35);
          });
        }
      });
    }, { threshold: 0.3 });

    const heroTelemetry = document.querySelector('.hero-telemetry');
    if (heroTelemetry) observer.observe(heroTelemetry);
  }

  // 4. Interactive Package & Ceremony Intake Widget
  const eventSelect = document.getElementById('eventType');
  const coverageSelect = document.getElementById('coverageType');
  const albumSelect = document.getElementById('albumType');

  const estTitle = document.getElementById('estTitle');
  const estTimeline = document.getElementById('estTimeline');
  const estWaBtn = document.getElementById('estWaBtn');

  function updateEstimator() {
    if (!eventSelect || !coverageSelect || !estTitle || !estWaBtn) return;

    const eventVal = eventSelect.value;
    const coverageVal = coverageSelect.value;
    const albumVal = albumSelect ? albumSelect.value : 'Archival Handcrafted Album';

    estTitle.textContent = `${eventVal} — ${coverageVal}`;
    estTimeline.textContent = `Includes: ${coverageVal} with ${albumVal} | Dual Lead Cinematographers & Same-Day Teaser Delivery`;

    const phone = '917980723203';
    const message = `Hello Face of Kolkata Photography! 🙏✨ I would like to check availability and consult about:\n- Event: ${eventVal}\n- Coverage Style: ${coverageVal}\n- Album Style: ${albumVal}\n\nPlease share your availability and consultation details.`;
    estWaBtn.href = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  }

  if (eventSelect && coverageSelect) {
    eventSelect.addEventListener('change', updateEstimator);
    coverageSelect.addEventListener('change', updateEstimator);
    if (albumSelect) albumSelect.addEventListener('change', updateEstimator);
    updateEstimator();
  }
});
