document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const toggle = document.getElementById("mode-toggle");

    toggle.addEventListener("click", () => {
        body.classList.toggle("dark");
        body.classList.toggle("light");
    });
});