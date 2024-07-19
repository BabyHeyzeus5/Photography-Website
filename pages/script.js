document.addEventListener("DOMContentLoaded", function() {
    const overlay = document.getElementById('overlay');
    const enlargedImage = document.getElementById('enlargedImage');

    document.querySelectorAll('.preview-size').forEach(image => {
        image.addEventListener('click', function() {
            enlargedImage.src = this.src;
            overlay.style.display = 'flex';
        });
    });

    overlay.addEventListener('click', function() {
        overlay.style.display = 'none';
    });
});