// Fading effect for service images and texts
document.addEventListener('DOMContentLoaded', () => {
    const imgs = Array.from(document.querySelectorAll('.left-section .component-img'));
    const texts = Array.from(document.querySelectorAll('.right-section .component-text'));
    const total = Math.min(imgs.length, texts.length);
    let current = 0;
    const interval = 5000; // ms between fades

    // initialize
    imgs.forEach((el, i) => el.classList.toggle('active', i === 0));
    texts.forEach((el, i) => el.classList.toggle('active', i === 0));

    setInterval(() => {
        // fade out current
        imgs[current].classList.remove('active');
        texts[current].classList.remove('active');

        // advance index
        current = (current + 1) % total;

        // fade in next
        imgs[current].classList.add('active');
        texts[current].classList.add('active');
    }, interval);
});