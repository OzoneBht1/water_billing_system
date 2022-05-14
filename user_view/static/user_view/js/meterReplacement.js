var office_code = document.getElementById("office_code");
var province = document.getElementById("Province");
var district = document.getElementById("District");
var municipality = document.getElementById("Municipality");
var js_variable = JSON.parse(document.getElementById("name").textContent);

office_code.addEventListener("change", function () {
  // province.innerHTML="";
  // district.innerHTML="";
  // municipality.innerHTML="";

  for (var i = 0; i < js_variable.length; i++) {
    if (parseInt(office_code.value) == js_variable[i]["Code"]) {
      province.value = js_variable[i]["Province"];
      district.value = js_variable[i]["District"];
      municipality.value = js_variable[i]["Local_Body"];
      break;
    } else {
      province.value = "-";
      district.value = "-";
      municipality.value = "-";
    }
  }
});
