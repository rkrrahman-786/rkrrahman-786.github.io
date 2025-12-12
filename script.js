const orb = document.querySelector('.cursor-orb');
let mouseX = 0;
let mouseY = 0;
let orbX = 0;
let orbY = 0;

const updateOrb = () => {
  orbX += (mouseX - orbX) * 0.15;
  orbY += (mouseY - orbY) * 0.15;
  orb.style.transform = `translate3d(${orbX - 11}px, ${orbY - 11}px, 0)`;
  requestAnimationFrame(updateOrb);
};

document.addEventListener('mousemove', (event) => {
  mouseX = event.clientX;
  mouseY = event.clientY;
  orb.style.opacity = 1;
});

document.addEventListener('mouseleave', () => {
  orb.style.opacity = 0;
});

updateOrb();

const animatedEls = document.querySelectorAll('[data-animate]');
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

animatedEls.forEach((el, index) => {
  el.style.transitionDelay = `${index * 0.04}s`;
  observer.observe(el);
});

// Modal functionality
const reserveBtn = document.getElementById('reserveSlotBtn');
const modal = document.getElementById('reserveModal');
const closeBtn = document.getElementById('closeModal');

reserveBtn.addEventListener('click', () => {
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
});

closeBtn.addEventListener('click', () => {
  modal.classList.remove('active');
  document.body.style.overflow = '';
});

modal.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
});

