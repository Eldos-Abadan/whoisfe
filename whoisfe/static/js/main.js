/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*==================== SCROLL SECTIONS ACTIVE LINK ====================*/
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2000,
    delay: 200,
//     reset: true
});

sr.reveal('.home__data, .about__img, .skills__subtitle, .skills__text',{}); 
sr.reveal('.textarea, .about__subtitle, .about__text, .skills__img',{delay: 400}); 
sr.reveal('.home__social-icon',{ interval: 200}); 
sr.reveal('.skills__data, .work__img, .contact__input',{interval: 200}); 
const form = document.querySelector('.contact__form');
const button = document.querySelector('.contact__button');

button.addEventListener('click', () => {
  form.classList.toggle('hidden');
});
document.addEventListener('DOMContentLoaded', function() {
    var formGroups = document.querySelectorAll('.about__form .form__group');
    for (var i = 0; i < formGroups.length; i++) {
        formGroups[i].classList.add('show');
    }
});
window.addEventListener('scroll', animateFormElements);

// Animate form elements when they become visible
function animateFormElements() {
    const formGroups = document.querySelectorAll('.about__form .form__group');
    
    formGroups.forEach((formGroup) => {
        const position = formGroup.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        
        if (position.top < windowHeight) {
            formGroup.classList.add('show');
        }
    });
}

// Initial animation check on page load
animateFormElements();