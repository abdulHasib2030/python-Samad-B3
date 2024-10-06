function append(value) {
    document.getElementById("result").value += value;
}

function clearDisplay() {
    document.getElementById("result").value = "";
}

function deleteLast() {
    let currentValue = document.getElementById("result").value;
    document.getElementById("result").value = currentValue.slice(0, -1);
}

function calculate() {
    let currentValue = document.getElementById("result").value;
    try {
        document.getElementById("result").value = eval(currentValue);
    } catch (e) {
        document.getElementById("result").value = "Error";
    }
}
