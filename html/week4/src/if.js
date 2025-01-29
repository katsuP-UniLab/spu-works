const starter = () => {
  let score = prompt("กรุณากรอกคะแนน", "");
  let text = `เกรดของคุณคือ `;

  if (score != "" && score == undefined) {
    let grade = "";

    switch (Number(score)) {
      case score >= 80 && score <= 100:
        grade = "A";
        break;
      case score >= 75 && score < 80:
        grade = "B+";
        break;
      case score >= 70 && score < 75:
        grade = "B";
        break;
      case score >= 65 && score < 70:
        grade = "C+";
        break;
      case score >= 60 && score < 65:
        grade = "C";
        break;
      case score >= 55 && score < 60:
        grade = "D+";
        break;
      case score >= 50 && score < 55:
        grade = "D";
        break;
      case score < 50 && score >= 0:
        grade = "F";
        break;

      default:
        grade = "";
        break;
    }

    if (grade == "") {
      text = "คะแนนไม่ถุกต้อง";
      document.querySelector("#alert-button").innerHTML = `run alert`;
    } else {
      text += grade;
      document.querySelector(
        "#alert-button"
      ).innerHTML = `Grade ${grade} <br /> Try again?`;
    }
  } else {
    text = "คะแนนไม่ถุกต้อง";
    document.querySelector("#alert-button").innerHTML = `run alert`;
  }

  alert(text);
};

document.querySelector("form").addEventListener("submit", (event) => {
  submitFunction(event);
});

const submitFunction = (e) => {
  e.preventDefault();

  let stack = Number(document.querySelector("input#stack").value);
  let mid = Number(document.querySelector("input#mid").value);
  let final = Number(document.querySelector("input#final").value);

  let score = 0;
  let grade = "";

  if (stack >= 0 && stack <= 40) {
    if (mid >= 0 && mid <= 20) {
      if (final >= 0 && final <= 40) {
        score = stack + mid + final;
        grade = String(calScore(score));
        console.log(calScore(score));
      }
    }
  }

  document.querySelector(
    "#app > #grade-res"
  ).innerHTML = `Your Grade is ${grade}`;
};

const calScore = (score) => {
  console.log(Number(score));
  let grade = "";

  if (Number(score) >= 80 && Number(score) <= 100) {
    grade = "A";
  } else if (Number(score) >= 75 && Number(score) < 80) {
    grade = "B+";
  } else if (Number(score) >= 70 && Number(score) < 75) {
    grade = "B";
  } else if (Number(score) >= 65 && Number(score) < 70) {
    grade = "C+";
  } else if (Number(score) >= 60 && Number(score) < 65) {
    grade = "C";
  } else if (Number(score) >= 55 && Number(score) < 60) {
    grade = "D+";
  } else if (Number(score) >= 50 && Number(score) < 55) {
    grade = "D";
  } else if (Number(score) < 50 && Number(score) >= 0) {
    grade = "F";
  } else {
    grade = "";
  }

  return grade;
};

const factorial = (inpNo) => {
  let res = 1;

  for (let i = 1; i <= inpNo; i++) {
    res = res * i;
  }

  return res;
};

// starter();
