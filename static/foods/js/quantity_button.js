const leftBtn = document.querySelector(".jsLeft");
const rightBtn = document.querySelector(".jsRight");
const quantity = document.querySelector(".jsQuantity");
console.log(quantity.value)

let beforeValue = quantity.value

const clickLeft = (event) => {
    event.preventDefault();
    if (Number(quantity.value) > 1) {
        quantity.value = Number(quantity.value) - 1
    }
}

const clickRight = (event) => {
    event.preventDefault();
    quantity.value = Number(quantity.value) + 1
}

const changeInput = (event) => {
    event.preventDefault();
    if (Number(event.target.value) < 1) {
        event.target.value = beforeValue;
        beforeValue = event.target.value;
    }
    beforeValue = event.target.value;
}

// 메인함수 정의
const btnmain = () => {
    leftBtn.addEventListener("click", clickLeft);
    rightBtn.addEventListener("click", clickRight);
    quantity.addEventListener("input", changeInput)
}

// 메인함수 호출
btnmain();