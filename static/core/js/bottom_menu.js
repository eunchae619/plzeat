const dotIcon = document.querySelector(".jsDot")
const writeIcon = document.querySelector(".jsWrite")
const howIcon = document.querySelector(".jsHow")
const jsI = document.querySelector(".jsI")



const changeDotColor = () => {
    dotIcon.classList.add("jsClickedDot")
    jsI.classList.add("jsClickedDotI")
}

const moveWriteIcon = () => {
    writeIcon.classList.add("jsMoveWrite")
}

const moveHowIcon = () => {
    howIcon.classList.add("jsMoveHow")
}

// 최상위버튼 클릭
const clickDotIcon = (event) => {
    event.preventDefault();
    if (dotIcon.classList.contains("jsOpened")) {
        dotIcon.classList.remove("jsOpened", "jsClickedDot", "jsClickedDotI");
        writeIcon.classList.remove("jsMoveWrite");
        howIcon.classList.remove("jsMoveHow");
        jsI.classList.remove("jsClickedDotI");
    }
    else {
        changeDotColor();
        moveWriteIcon();
        moveHowIcon();
        dotIcon.classList.add("jsOpened")
    }
}