document.addEventListener('DOMContentLoaded', function() {
    var footer = document.querySelector('.footer');
    window.addEventListener('scroll', function() {
        if (window.innerHeight >= document.body.scrollHeight) {
            footer.style.display = 'none';
        } else if (window.scrollY >= document.body.scrollHeight - window.innerHeight) {
            footer.style.display = 'block';
        } else {
            footer.style.display = 'none';
        }
    });
});
