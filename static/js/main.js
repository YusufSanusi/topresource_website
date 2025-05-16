// Simple mobile menu toggle
document
  .querySelector('.mobile-menu-btn')
  .addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links')
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex'
  })

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()

    const targetId = this.getAttribute('href')
    if (targetId === '#') return

    const targetElement = document.querySelector(targetId)
    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: 'smooth',
      })

      // Close mobile menu if open
      if (window.innerWidth <= 768) {
        document.querySelector('.nav-links').style.display = 'none'
      }
    }
  })
})
