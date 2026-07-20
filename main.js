document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
      
      // Prevent scrolling when menu is open
      if (navLinks.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    });
  }

  // Add subtle fade-in animation to artwork cards on scroll
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = 1;
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const cards = document.querySelectorAll('.artwork-card');
  cards.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = 'translateY(30px)';
    card.style.transition = `all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) ${index * 0.1}s`;
    observer.observe(card);
  });
});
