document.addEventListener("DOMContentLoaded", function () {
    const text = document.getElementById("typed-author");
    if (!text) return;

    const authorName = text.dataset.author;
    let i = 0;

    function typeWriter() {
        if (i < authorName.length) {
            text.innerHTML += authorName.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    }

    typeWriter();
});
