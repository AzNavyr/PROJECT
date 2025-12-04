let currentIndex = 0;

function showImage(index, tag) {
    const images = document.querySelectorAll(tag);
    if (index >= images.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = images.length - 1;
    } else {
        currentIndex = index;
    }
    images.forEach((img, i) => {
        img.style.transform = `translateX(-${currentIndex * 100}%)`;
    });
}

function nextImage(tag) {
    showImage(currentIndex + 1, tag);
}

function prevImage(tag) {
    showImage(currentIndex - 1, tag);
}

// Initial call to display the first image
showImage(currentIndex);


document.querySelectorAll('.accordion-header').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;

        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
});