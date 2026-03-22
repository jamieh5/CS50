let choices_btn = document.querySelectorAll(".choice");
let choices_p = document.querySelectorAll(".choices p");

// Handling the correct answer for the first question
for (let i = 0; i < choices_btn.length; i++) {
  choices_btn[i].addEventListener("click", function () {
    choices_p[i].style.visibility = "visible";
    if (choices_btn[i].innerHTML != "Norris") {
      choices_btn[i].style.backgroundColor = "red";
    } else {
      choices_btn[i].style.backgroundColor = "green";
    }
  });
}

// Handling the correct answer for the second question
document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();
  answer = document.querySelector("#answer");
  p = document.querySelector("#form-p");
  if (answer.value != 24) {
    p.innerHTML = "Incorrect!";
    answer.style.backgroundColor = "red";
  } else {
    p.innerHTML = "Correct!";
    answer.style.backgroundColor = "green";
  }
  p.style.visibility = "visible";
});
