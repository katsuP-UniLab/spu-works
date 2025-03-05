const locationSearch = window.location.href
  .split("/")
  .filter(() => {
    return true;
  })
  .reverse();

let path = "";

if (locationSearch[0] == "") {
  path = locationSearch[1];
} else {
  path = locationSearch[0];
}

if (path != "") {
  switch (path) {
    case "course":
      path = "course";
      break;
    case "register":
      path = "register";
      break;

    default:
      path = "home";
      break;
  }
}

const navBarTemplate = `<a href="/" class="logo">Go2UpSkills</a>
<a href="${path == "home" ? "#" : "/"}">Home</a>
<a href="${path == "course" ? "#" : "/course"}">Course</a>
<a href="${path == "register" ? "#" : "/register"}">Register</a>`;

document.querySelector("#nav").innerHTML = navBarTemplate;

let item = document.querySelectorAll("#nav > a");

item.forEach((i) => {
  let link = i.href.split("/").reverse()[0];

  if (link == "#") {
    i.classList.toggle("active");
  }
});
