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

    // Set initial title
    const language = localStorage.getItem('language') || 'ro';
    updateTitleByLanguage(language);

    // Listen for language changes (assuming you dispatch a custom event)
    window.addEventListener('languageChanged', function(e) {
        updateTitleByLanguage(e.detail.language);
    });
});

function updateTitleByLanguage(language) {
    if (language === 'en') {
        document.title = 'Cubevo Data Concept | Modern Software Solutions';
    } else {
        document.title = 'Cubevo Data Concept | Soluții software moderne';
    }
}

// Check for dark mode preference on page load
if (localStorage.getItem('darkMode') === 'true') {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}

// Example: when user clicks the language button
function setLanguage(lang) {
    localStorage.setItem('language', lang);
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    // ...other logic...
}