const instructionSection = document.querySelector('.instructions');

window.addEventListener('scroll', () => {
    const sectionPosition = instructionSection.getBoundingClientRect().top;
    const screenPosition = window.innerHeight / 1;

    if (sectionPosition < screenPosition) {
        instructionSection.classList.add('show');
    }
});
