// Mobile menu toggle
document.querySelector('nav button').addEventListener('click', function() {
    const mobileMenu = document.querySelector('.md\\:hidden + div');
    if (mobileMenu) {
        mobileMenu.classList.toggle('hidden');
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Pricing toggle
const pricingButtons = document.querySelectorAll('.relative.mt-6 button');
pricingButtons.forEach(button => {
    button.addEventListener('click', function() {
        pricingButtons.forEach(btn => {
            btn.classList.remove('bg-white', 'border-gray-200', 'text-gray-900');
            btn.classList.add('border', 'border-transparent', 'text-gray-700');
        });
        this.classList.add('bg-white', 'border-gray-200', 'text-gray-900');
        this.classList.remove('border', 'border-transparent', 'text-gray-700');
        
        // Here you would update pricing based on monthly/yearly selection
        console.log('Pricing period changed to:', this.textContent.trim());
    });
});

// Form submission
const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for your interest! We will contact you shortly.');
        form.reset();
    });
}