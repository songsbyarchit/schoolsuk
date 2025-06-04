document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const toggle = document.getElementById("mode-toggle");

    toggle.addEventListener("click", () => {
        body.classList.toggle("dark");
        body.classList.toggle("light");
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const reveals = document.querySelectorAll('.reveal');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // remove this line if you want repeated animation
            }
        });
    }, { threshold: 0.1 });

    reveals.forEach(el => observer.observe(el));
});