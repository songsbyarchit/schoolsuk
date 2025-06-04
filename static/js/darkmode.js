document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const toggle = document.getElementById("mode-toggle");

    // Apply saved theme
    const savedMode = localStorage.getItem("theme");
    if (savedMode === "dark") {
        body.classList.remove("light");
        body.classList.add("dark");
        toggle.checked = true;
    }

    toggle.addEventListener("click", () => {
        const isDark = body.classList.contains("dark");
        body.classList.toggle("dark");
        body.classList.toggle("light");
        localStorage.setItem("theme", isDark ? "light" : "dark");
    });

    // Reveal animations
    const reveals = document.querySelectorAll('.reveal');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // remove if you want animation to repeat
            }
        });
    }, { threshold: 0.1 });

    reveals.forEach(el => observer.observe(el));
});