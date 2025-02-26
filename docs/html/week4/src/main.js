const element = document.querySelector("#app");

let name = "Suphakit P.";
let text = "Information Technology";

let n1, n2;

n1 = 5;
n2 = 10;

element.innerHTML += `<p>${name}</p>`;
element.innerHTML += `<p>${text}</p>`;
element.innerHTML += `<p>${n1 + n2}</p>`;

alert("run");
