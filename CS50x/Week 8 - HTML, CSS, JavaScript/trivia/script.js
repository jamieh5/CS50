let choices_btn = document.querySelectorAll(".choice");
let choices_p = document.querySelectorAll(".choices p");

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
