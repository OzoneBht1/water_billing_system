var js_variable = JSON.parse(document.getElementById("name").textContent);

var lookup = {};
var lookup2 = {};

var months = {
  January: 1,
  February: 2,
  March: 3,
  April: 4,
  May: 5,
  June: 6,
  July: 7,
  August: 8,
  September: 9,
  October: 10,
  November: 11,
  December: 12,
};

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
  f.innerText = null;
  g.innerText = null;

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
        // municipality.innerHTML =
        //   municipality.innerHTML +
        //   '<option value="' +
        //   js_variable[i]["Local_Body"] +
        //   '">' +
        //   js_variable[i]["Local_Body"] +
        //   "</option>";
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
  g.innerText = null;
  // municipality.innerHTML = "--Select Municipality--";
  const selectedDistrict = f.options[f.selectedIndex].value;
  console.log(selectedDistrict);
  for (var i = 0; i < js_variable.length; i++) {
    if (js_variable[i]["District"] === selectedDistrict) {
      municipality.innerHTML =
        municipality.innerHTML +
        '<option value="' +
        js_variable[i]["Local_Body"] +
        '">' +
        js_variable[i]["Local_Body"] +
        "</option>";
    }
  }
});

// ********************************************************************

// These are used for setting the penalty if paid late

var prevUnit = document.getElementById("previous_unit");
var currUnit = document.getElementById("current_unit");
var consumedUnit = document.getElementById("consumed_unit");
var discount = 0;
var today = new Date();
var penalty = document.getElementById("penalty");
var read_month = document.getElementById("month");
var discountAmount = document.getElementById("discount");

var bill_amt = document.getElementById("bill_amount");
var final_bill = document.getElementById("final_bill");

read_month.addEventListener("change", function () {
  setPenalty();
});

prevUnit.addEventListener("change", function () {
  currUnit.setAttribute("min", prevUnit.value);
  setConsumedUnit();
});

currUnit.addEventListener("change", function () {
  console.log(currUnit.value);
  setConsumedUnit();
});

// var payDate = newDate(2002, )

function setPenalty() {
  var early = true;
  var val = months[read_month.value];
  let payDate = new Date(2022, val - 1, 10);
  console.log(payDate);
  let currentDate = new Date(2022, today.getMonth(), today.getDate());
  console.log(currentDate);
  var diff = Math.abs(currentDate - payDate);
  console.log(diff);

  var diffDays = Math.ceil(diff / (1000 * 3600 * 24));
  if (val > today.getMonth() + 1) {
    early = true;
  } else if (val < today.getMonth() + 1) {
    early = false;
  } else if (val == today.getMonth() + 1) {
    if (today.getDate() < 10) {
      early = true;
    } else {
      early = false;
    }
  }
  console.log(diffDays);

  penaltyCalc(diffDays, early);
}
function penaltyCalc(diffDays, early) {
  if (early) {
    penalty.value = 0;
    discount = 0.05;
    discountAmount.value = 5;
  } else {
    if (diffDays <= 10) {
      penalty.value = 0;
    } else {
      penalty.value = parseFloat((diffDays * 0.2).toFixed(2));
      discount = 0;
      discountAmount.value = 0;
      console.log(discount);
    }
  }
  setFinalAmount();
}

function setConsumedUnit() {
  consumedUnit.value = currUnit.value - prevUnit.value;
  setInitialBill();
  setFinalAmount();
}

function setInitialBill() {
  var unit = parseInt(consumedUnit.value);
  var bill = 0;
  if (unit < 10) {
    bill = 100;
  } else if (unit >= 10 && unit < 15) {
    bill = 100 + (unit - 10) * 11;
  } else if (unit >= 15 && unit < 30) {
    bill = 100 + 5 * 11 + (unit - 15) * 12.5;
  } else if (unit >= 30 && unit < 50) {
    bill = 100 + 5 * 11 + 14 * 12.5 + (unit - 30) * 14.5;
  } else if (unit >= 50 && unit < 100) {
    bill = 100 + 5 * 11 + 14 * 12.5 + 20 * 14.5 + (unit - 50) * 17;
  } else if (unit >= 100) {
    bill = 100 + 5 * 11 + 14 * 12.5 + 20 * 14.5 + 30 * 17 + (unit - 100) * 20.5;
  }
  bill_amt.value = bill;
}

console.log(discount);

function setFinalAmount() {
  final_amount =
    parseFloat(bill_amt.value) -
    parseFloat(bill_amt.value) * parseFloat(discount) +
    parseFloat(penalty.value);
  console.log(final_amount);
  console.log(bill_amt.value);
  console.log(discount);
  final_bill.value = final_amount;
}
