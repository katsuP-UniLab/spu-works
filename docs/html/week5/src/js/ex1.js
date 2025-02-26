const showElement = document.querySelector("#res-data");

const greet = (name, lname) => {
  return `Hello, ${name} ${lname}.`;
};

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();

  let fname = document.querySelector("form > #f-name").value;
  let lname = document.querySelector("form > #l-name").value;

  if (fname != "" && lname != "") {
    showElement.innerHTML = greet(fname, lname);
  } else {
    alert("Some form input is still missing.. Try again.");
  }
});
