var navigation = document.querySelector(".navigation-wrapper");

document.addEventListener("scroll", function () {
    var invert = false;
    if (document.scrollingElement.scrollTop > 16) {
        invert = true;
    }
    
    if (navigation.classList.contains("invert") != invert) {
        navigation.classList[invert ? "add" : "remove"]("invert");
    }
});
