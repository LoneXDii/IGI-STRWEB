window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    const maxScroll = document.body.scrollHeight - window.innerHeight;

    const scrollPercent = Math.min(scrollPosition / maxScroll, 1);

    const leftDoorTransform = `translateX(${-scrollPercent * 100}%)`;
    const rightDoorTransform = `translateX(${scrollPercent * 100}%)`;

    document.querySelector('.left-door').style.transform = leftDoorTransform;
    document.querySelector('.right-door').style.transform = rightDoorTransform;
});