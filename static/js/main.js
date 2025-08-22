// Additional functionality or analytics
document.addEventListener('DOMContentLoaded', function() {
    // Form submission handling
    const contactForm = document.querySelector('#contact form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Form handling logic here
            alert('Thank you for your message. We will get back to you soon!');
            this.reset();
        });
    }

    // SEO optimization - track user engagement
    const trackEngagement = () => {
        // Custom engagement tracking code would go here
    };

    // Call tracking function
    trackEngagement();
});

// Check for dark mode preference on page load
if (localStorage.getItem('darkMode') === 'true') {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}