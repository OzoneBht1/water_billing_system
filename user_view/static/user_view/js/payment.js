var js_variable = JSON.parse(document.getElementById("name").textContent);

var lookup = {};
var lookup2 = {};

// console.log(js_variable);
var e = document.getElementById("province");
var f = document.getElementById("district");
var g = document.getElementById("municipality");

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

// ********************************************************************

var today = new Date();
var penalty = document.getElementById("penalty");
var read_month = document.getElementById("month");
var read_date = document.getElementById("date");
var month = document.getElementById("month").value;
var date = document.getElementById("date").value;
// These are used for setting the penalty if paid late

var prevUnit = document.getElementById("previous_unit");
var currUnit = document.getElementById("current_unit");
var consumedUnit = document.getElementById("consumed_unit");

var today = new Date();

read_month.addEventListener("change", function () {
  console.log(read_month.value);
  setPenalty();
});

read_date.addEventListener("change", function () {
  console.log(read_date.value);
  setPenalty();
});

prevUnit.addEventListener("change", function () {
  console.log(prevUnit.value);
  currUnit.setAttribute("min", prevUnit.value);
  setConsumedUnit();
});

currUnit.addEventListener("change", function () {
  console.log(currUnit.value);
  setConsumedUnit();
});

// var payDate = newDate(2002, )

function setPenalty() {
  let payDate = new Date(2022, month, date);
  let currentDate = new Date(2022, today.getMonth() + 1, today.getDate());
  var diff = Math.abs(currentDate - payDate);
  console.log(diff);
  var diffDays = Math.ceil(diff / (1000 * 3600 * 24));
  console.log(diffDays);
  penalty.value = diffDays;
}
function penaltyCalc() {}

function setConsumedUnit() {
  consumedUnit.value = currUnit.value - prevUnit.value;
}
