'use strict';

(function () {

    var inputLogin = document.querySelector('.form__input--login');
    var inputPassword = document.querySelector('.form__input--password');

    var eyeOneOne = document.querySelector('.animation__eye--one-one');
    var eyeOneTwo = document.querySelector('.animation__eye--one-two');

    var eyeTwoOne = document.querySelector('.animation__eye--two-one');
    var eyeTwoTwo = document.querySelector('.animation__eye--two-two');

    inputLogin.addEventListener('focus', firstFocusHandler);
    inputPassword.addEventListener('focus', firstFocusHandler);

    inputLogin.addEventListener('input', inputHandler);
    inputPassword.addEventListener('input', inputHandler);

    inputLogin.addEventListener('blur', blurHandler);
    inputPassword.addEventListener('blur', blurHandler);

    function firstFocusHandler() {
        var animation = document.querySelector('.animation');
        var animationVideo = document.querySelector('.animation__video');
        var eye = document.querySelectorAll('.animation__eye');
        var button = document.querySelector('.form__button');
        var about = document.querySelector('.about');

        for (var i = 0; i < eye.length; i++) {
            eye[i].style.display = "block";
            fadeIn(eye[i], 2000);
        }

        animation.style.maxHeight = "187px";
        animationVideo.style.display = "block";
        fadeIn(animationVideo, 2000);
        fadeIn(about, 2000);
        animationVideo.play();

        inputLogin.removeEventListener('focus', firstFocusHandler);
        inputPassword.removeEventListener('focus', firstFocusHandler);

        inputLogin.addEventListener('focus', focusHandler);
        inputPassword.addEventListener('focus', focusHandler);

        button.addEventListener('click', clickHandler);
    }

    function fadeIn(elem, speed) {
        var inInterval = setInterval(function () {
            elem.style.opacity = Number(elem.style.opacity) + 0.02;
            if (elem.style.opacity >= 1)
                clearInterval(inInterval);
        }, speed / 50);
    }

    function fadeOut(elem, speed) {
        var outInterval = setInterval(function () {
            if (!elem.style.opacity) {
                elem.style.opacity = 1;
            }
            elem.style.opacity -= 0.02;
            if (elem.style.opacity <= 0)
                clearInterval(outInterval);
        }, speed / 50);
    }

    function focusHandler(evt) {
        evt.preventDefault();
        evt.stopPropagation();
        var length = evt.target.value.length;
        setPositionOne(length);
        setPositionTwo(length);
    }

    function inputHandler(evt) {
        var length = evt.target.value.length;
        setPositionOne(length);
        setPositionTwo(length);
    }

    function setPositionOne(len) {
        if (len < 2) {
            eyeOneOne.style.left = "28px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "50px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 3) {
            eyeOneOne.style.left = "28px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "51px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 4) {
            eyeOneOne.style.left = "29px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "52px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 5) {
            eyeOneOne.style.left = "29px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "52px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 6) {
            eyeOneOne.style.left = "30px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "52px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 7) {
            eyeOneOne.style.left = "31px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "53px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 8) {
            eyeOneOne.style.left = "31px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "53px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len < 9) {
            eyeOneOne.style.left = "32px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "54px";
            eyeOneTwo.style.top = "55px";
        }
        else if (len > 12) {
            eyeOneOne.style.left = "32px";
            eyeOneOne.style.top = "55px";
            eyeOneTwo.style.left = "54px";
            eyeOneTwo.style.top = "55px";
        }
    }

    function setPositionTwo(len) {
        if (len < 2) {
            eyeTwoOne.style.left = "123px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "145px";
            eyeTwoTwo.style.top = "84px";
        }
        else if (len < 3) {
            eyeTwoOne.style.left = "123px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "146px";
            eyeTwoTwo.style.top = "84px";
        }
        else if (len < 4) {
            eyeTwoOne.style.left = "123px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "146px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len < 5) {
            eyeTwoOne.style.left = "124px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "146px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len < 6) {
            eyeTwoOne.style.left = "124px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "147px";
            eyeTwoTwo.style.top = "84,5px";
        }
        else if (len < 7) {
            eyeTwoOne.style.left = "125px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "147px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len < 8) {
            eyeTwoOne.style.left = "125px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "147px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len === 11) {
            eyeTwoOne.style.left = "125px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "147px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len === 12) {
            eyeTwoOne.style.left = "126px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "148px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len === 13) {
            eyeTwoOne.style.left = "126px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "148px";
            eyeTwoTwo.style.top = "85px";
        }
        else if (len > 13) {
            eyeTwoOne.style.left = "127px";
            eyeTwoOne.style.top = "84px";
            eyeTwoTwo.style.left = "149px";
            eyeTwoTwo.style.top = "85px";
        }
    }

    function blurHandler() {
        eyeOneOne.style.left = "29px";
        eyeOneOne.style.top = "54px";
        eyeOneTwo.style.left = "52px";
        eyeOneTwo.style.top = "54px";

        eyeTwoOne.style.left = "125px";
        eyeTwoOne.style.top = "82px";
        eyeTwoTwo.style.left = "148px";
        eyeTwoTwo.style.top = "82px";
    }

    function clickHandler() {
        var wrapper = document.querySelector('.wrapper');
        fadeOut(wrapper, 1000);
    }
})();
