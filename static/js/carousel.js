// Testimonial Carousel Functionality
document.addEventListener('DOMContentLoaded', function () {
  const carousel = document.querySelector('.carousel-container')
  const cards = document.querySelectorAll('.testimonial-card')
  const dots = document.querySelectorAll('.carousel-dot')
  const prevBtn = document.querySelector('.carousel-btn.prev')
  const nextBtn = document.querySelector('.carousel-btn.next')
  let currentIndex = 0
  const cardCount = cards.length

  function updateCarousel() {
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`

    // Update dots
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentIndex)
    })
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % cardCount
    updateCarousel()
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + cardCount) % cardCount
    updateCarousel()
  }

  // Button events
  nextBtn.addEventListener('click', nextSlide)
  prevBtn.addEventListener('click', prevSlide)

  // Dot navigation
  dots.forEach((dot) => {
    dot.addEventListener('click', function () {
      currentIndex = parseInt(this.getAttribute('data-index'))
      updateCarousel()
    })
  })

  // Auto-advance (optional)
  let autoSlide = setInterval(nextSlide, 5000)

  // Pause on hover
  const carouselWrapper = document.querySelector('.testimonial-carousel')
  carouselWrapper.addEventListener('mouseenter', () => clearInterval(autoSlide))
  carouselWrapper.addEventListener('mouseleave', () => {
    autoSlide = setInterval(nextSlide, 5000)
  })

  // Touch support for mobile
  let touchStartX = 0
  let touchEndX = 0

  carouselWrapper.addEventListener(
    'touchstart',
    (e) => {
      touchStartX = e.changedTouches[0].screenX
    },
    { passive: true }
  )

  carouselWrapper.addEventListener(
    'touchend',
    (e) => {
      touchEndX = e.changedTouches[0].screenX
      handleSwipe()
    },
    { passive: true }
  )

  function handleSwipe() {
    if (touchEndX < touchStartX - 50) {
      nextSlide() // Swipe left
    }
    if (touchEndX > touchStartX + 50) {
      prevSlide() // Swipe right
    }
  }
})
