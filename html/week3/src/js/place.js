const APILink = `https://raw.githubusercontent.com/kongvut/thai-province-data/master/api_province_with_amphure_tambon.json`;

const base = `<option value="">กรุณาเลือกอำเภอ</option>`;

const provinceList = async () => {
  const data = await fetch(APILink);
  const respData = await data.json();

  for (let i = 0; i < respData.length; i++) {
    const template = `<option value="${respData[i].name_en}">${respData[i].name_th}</option>`;
    document.querySelector("#province").innerHTML += template;
  }
};

const districtList = async (province) => {
  const data = await fetch(APILink);
  const respData = await data.json();

  let index = respData.findIndex((e) => e.name_en == province);

  console.log(index);
  document.querySelector("#district").innerHTML = base;

  for (let i = 0; i < respData[index].amphure.length; i++) {
    const template = `<option value="${respData[index].amphure[i].name_en}">${respData[index].amphure[i].name_th}</option>`;
    document.querySelector("#district").innerHTML += template;
  }
};

provinceList();

document.querySelector("#province").addEventListener("change", async (e) => {
  if (e.target.value != "") {
    await districtList(e.target.value);
    document.querySelector("#district").disabled = false;
  } else {
    document.querySelector("#district").disabled = true;
  }
});
