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

        animation.style.maxHeight = "374px";
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
            eyeOneOne.style.left = "56px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "101px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 3) {
            eyeOneOne.style.left = "57px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "102px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 4) {
            eyeOneOne.style.left = "58px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "103px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 5) {
            eyeOneOne.style.left = "59px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "104px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 6) {
            eyeOneOne.style.left = "60px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "104px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 7) {
            eyeOneOne.style.left = "61px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "105px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 8) {
            eyeOneOne.style.left = "62px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "106px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len < 9) {
            eyeOneOne.style.left = "63px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "107px";
            eyeOneTwo.style.top = "111px";
        }
        else if (len > 12) {
            eyeOneOne.style.left = "64px";
            eyeOneOne.style.top = "110px";
            eyeOneTwo.style.left = "108px";
            eyeOneTwo.style.top = "111px";
        }
    }

    function setPositionTwo(len) {
        if (len < 2) {
            eyeTwoOne.style.left = "245px";
            eyeTwoOne.style.top = "167px";
            eyeTwoTwo.style.left = "290px";
            eyeTwoTwo.style.top = "168px";
        }
        else if (len < 3) {
            eyeTwoOne.style.left = "246px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "291px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len < 4) {
            eyeTwoOne.style.left = "247px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "292px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len < 5) {
            eyeTwoOne.style.left = "248px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "293px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len < 6) {
            eyeTwoOne.style.left = "249px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "294px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len < 7) {
            eyeTwoOne.style.left = "250px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "294px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len < 8) {
            eyeTwoOne.style.left = "250px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "294px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len === 11) {
            eyeTwoOne.style.left = "251px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "295px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len === 12) {
            eyeTwoOne.style.left = "252px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "296px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len === 13) {
            eyeTwoOne.style.left = "253px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "297px";
            eyeTwoTwo.style.top = "169px";
        }
        else if (len > 13) {
            eyeTwoOne.style.left = "254px";
            eyeTwoOne.style.top = "168px";
            eyeTwoTwo.style.left = "298px";
            eyeTwoTwo.style.top = "169px";
        }
    }

    function blurHandler() {
        eyeOneOne.style.left = "58px";
        eyeOneOne.style.top = "107px";
        eyeOneTwo.style.left = "104px";
        eyeOneTwo.style.top = "108px";

        eyeTwoOne.style.left = "250px";
        eyeTwoOne.style.top = "164px";
        eyeTwoTwo.style.left = "296px";
        eyeTwoTwo.style.top = "164px";
    }

    function clickHandler() {
        var wrapper = document.querySelector('.wrapper');
        fadeOut(wrapper, 1000);
    }
})();
