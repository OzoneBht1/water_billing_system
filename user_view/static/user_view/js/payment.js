var js_variable = JSON.parse(document.getElementById("name").textContent);

var lookup = {};
var lookup2 = {};

// console.log(js_variable);
var e = document.getElementById("province");
var f = document.getElementById("district");
console.log("working?");
e.addEventListener("click", function () {
  for (var i = 0; i < js_variable.length; i++) {
    var currentProvince = js_variable[i]["Province"];
    if (!(currentProvince in lookup)) {
      lookup[currentProvince] = 1;
      province.innerHTML =
        province.innerHTML +
        '<option value="' +
        currentProvince +
        '">' +
        currentProvince +
        "</option>";
    }
  }
});

console.log(js_variable[0]["Province"]);

e.addEventListener("change", function () {
  // district.innerHTML = "--Select District--";
  // municipality.innerHTML = "--Select Municipality--";
  const selectedProvince = e.options[e.selectedIndex].value;
  console.log(selectedProvince);
  for (var i = 0; i < js_variable.length; i++) {
    if (js_variable[i]["Province"] === selectedProvince) {
      var currentDistrict = js_variable[i]["District"];
      if (!(currentDistrict in lookup2)) {
        lookup2[currentDistrict] = 1;
        district.innerHTML =
          district.innerHTML +
          '<option value="' +
          js_variable[i]["District"] +
          '">' +
          js_variable[i]["District"] +
          "</option>";
        municipality.innerHTML =
          municipality.innerHTML +
          '<option value="' +
          js_variable[i]["Local Body"] +
          '">' +
          js_variable[i]["Local Body"] +
          "</option>";
      }
    }
  }
});

//     console.log(js_variable[i]["District"]);
//     district.innerHTML =
//       district.innerHTML +
//       '<option value="' +
//       js_variable[i]["District"] +
//       '">' +
//       js_variable[i]["District"] +
//       "</option>";
//   }
// }

f.addEventListener("change", function () {
  // municipality.innerHTML = "--Select Municipality--";
  const selectedDistrict = f.options[f.selectedIndex].value;
  console.log(selectedDistrict);
  for (var i = 0; i < js_variable.length; i++) {
    if (js_variable[i]["District"] === selectedDistrict) {
      municipality.innerHTML =
        municipality.innerHTML +
        '<option value="' +
        js_variable[i]["Local Body"] +
        '">' +
        js_variable[i]["Local Body"] +
        "</option>";
    }
  }
});
