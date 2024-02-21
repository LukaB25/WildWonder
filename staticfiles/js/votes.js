document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star');
    let clicked = false;
    let selectedRating = 0;

    const star1 = document.getElementById('1');
    const star2 = document.getElementById('2');
    const star3 = document.getElementById('3');
    const star4 = document.getElementById('4');
    const star5 = document.getElementById('5');

    const starArr = [star1, star2, star3, star4, star5]
    stars.forEach(star => {
        star.addEventListener('click', function() {
            const radioButtonId = this.getAttribute('for');
            const radioButton = document.getElementById(radioButtonId);

            radioButton.click();
            clicked = true;
            selectedRating = parseInt(this.id);
        });
    });

    starArr.forEach(star => {
        star.addEventListener('click', function() {
            const rating = parseInt(this.id);
            starArr.forEach(star => {
                star.classList.remove('checked');
            });
            for (let i = 0; i < rating; i++) {
                starArr[i].classList.add('checked');
            }
        });

        star.addEventListener('mouseover', function() {
            const rating = parseInt(this.id);
            starArr.forEach(star => {
                star.classList.remove('hover');
            });
            for (let i = 0; i < rating; i++) {
                starArr[i].classList.add('hover');
            }
        });

        star.addEventListener('mouseout', function() {
            if (clicked) {
                starArr.forEach(star => {
                    star.classList.remove('hover');
                });
            } else if (!clicked) {
                starArr.forEach(star => {
                    star.classList.remove('hover');
                });
            } else {
                for (let i = 0; i < selectedRating; i++) {
                    starArr[i].classList.add('hover');
                }
            }
        });
    });
});