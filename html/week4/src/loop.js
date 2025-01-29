document.querySelector("form").addEventListener("submit", (e) => {
  mxt(e);
});

const mxt = (e) => {
  e.preventDefault();

  let number = Number(document.querySelector("#number").value);
  let rtn = "";

  for (let i = 1; i <= 12; i++) {
    let template = `<p>${number.toLocaleString()} x ${i.toLocaleString()} = ${(
      number * i
    ).toLocaleString()}</p>`;

    rtn += template;
  }

  document.querySelector("div#res").innerHTML = rtn;
};
