document.addEventListener("DOMContentLoaded", function () {
    let currentPage = window.location.pathname.substring(1);

    if (currentPage === 'accounts/login/' || currentPage === 'accounts/signup/' || currentPage === 'accounts/logout/') {
        document.getElementsByClassName('about-section')[0].classList.add('hide');
        document.getElementById('hero-img').classList.add('hero-img-full-screen');
        document.getElementsByClassName('footer')[0].classList.add('sticky-footer');
    }
    else {
        document.getElementsByClassName('about-section')[0].classList.remove('hide');
        document.getElementById('hero-img').classList.remove('hero-img-full-screen');
        document.getElementsByClassName('footer')[0].classList.remove('sticky-footer');
    }
});
