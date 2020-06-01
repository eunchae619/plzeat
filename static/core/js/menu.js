// 변수 선언
const menu = document.querySelector(".jsMenu")
const hiddenMenu = document.querySelector(".jsHiddenMenu")

// 함수 정의

const clickMenu = (event) => {
    event.preventDefault();
    if (hiddenMenu.classList.contains("jsClickedHiddenMenu")) {
        hiddenMenu.classList.remove("jsClickedHiddenMenu")
    } else {
        hiddenMenu.classList.add("jsClickedHiddenMenu")
    }
}


const main = () => {
    menu.addEventListener("click", clickMenu)
}


// 함수 호출
main()