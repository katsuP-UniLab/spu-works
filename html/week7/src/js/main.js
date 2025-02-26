const main = document.querySelectorAll(".cut");

const apiFetch = async () => {
  for (let i = 0; i < main.length; i++) {
    let element = main[i];

    const call = await fetch("https://frame.000189.xyz/rdm");
    const resp = await call.json();

    element.innerHTML = `<div class="breaker" style="background: url(${resp.url});">
    <div class="overlay"></div>
  </div>`;
  }
};

apiFetch();
