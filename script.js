const greetscreen = document.querySelector('.greetscreen');
const logo = document.querySelector('.logo');

greetscreen.addEventListener('click', () => {
    setTimeout(() => {
        window.location.href = "homepage.html";
    }, 0);
});