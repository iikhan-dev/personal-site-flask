// Function to update the countdown timer and redirect after 10 seconds
let secondsLeft = 10;
const countdown = document.getElementById("countdown");
const timerText = document.getElementById("timer-text");

function updateTimer() {
    countdown.textContent = secondsLeft;
    secondsLeft--;

    if (secondsLeft < 0) {
        clearInterval(timerInterval);
        window.location.href = "/";
    }
}

const timerInterval = setInterval(updateTimer, 1000); // Update every second
