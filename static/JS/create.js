    function myFunction() {
      // Get the checkbox
      var checkBox = document.getElementById("myCheck");
      // Get the output text
      var text = document.getElementById("cpo");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }
document.addEventListener("DOMContentLoaded", function(event) {
  var checkBox = document.getElementById("myCheck");
  var text = document.getElementById("cpo");

  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
});

    function myFunction1() {
      // Get the checkbox
      var checkBox = document.getElementById("myCheck1");
      // Get the output text
      var text = document.getElementById("cz");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }
document.addEventListener("DOMContentLoaded", function(event) {
  var checkBox = document.getElementById("myCheck1");
  var text = document.getElementById("cz");

  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
});
    function myFunction1_1() {
      // Get the checkbox
      var checkBox = document.getElementById("myCheck1_1");
      // Get the output text
      var text = document.getElementById("cz1_1");
      var text2 = document.getElementById("cz1_2");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
        text2.style.display = "none";
      } else {
        text.style.display = "none";
        text2.style.display = "";
      }
    }




    function check_oks_detail() {
      // Get the checkbox
      var checkBox = document.getElementById("check_oks_detail");
      // Get the output text
      var text = document.getElementById("prim_oks_detail");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }

    function check_zu_detail() {
      // Get the checkbox
      var checkBox = document.getElementById("check_zu_detail");
      // Get the output text
      var text = document.getElementById("prim_zu_detail");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }


    function check_detail09() {
      // Get the checkbox
      var checkBox = document.getElementById("check_detail09");
      // Get the output text
      var text = document.getElementById("check_detail09_1");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }

    function check_zu09() {
      // Get the checkbox
      var checkBox = document.getElementById("check_zu09");
      // Get the output text
      var text = document.getElementById("check_zu09_1");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }
    function check_oks08() {
      // Get the checkbox
      var checkBox = document.getElementById("check_oks08");
      // Get the output text
      var text = document.getElementById("check_oks08_1");

      // If the checkbox is checked, display the output text
      if (checkBox.checked == true){
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }


// Отрицательная площадь
function Otr_S_OKS() {
  var input1 = document.getElementById("otr_s_oks1").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      // Очищаем таблицу перед добавлением строк
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh1[]' id='otrS_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}
// Другой регион
function drygoiRegion_OKS() {
  var input2 = document.getElementById("drugoiReg_oks2").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable1");
  var FormDrugoiReg_oks = "{{ FormDrugoiReg_oks.kh }}";
  var FormDrugoiReg_oks1 = "{{ FormDrugoiReg_oks.adress }}";
  console.log(input2)

  if (input2 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      // Добавляем нужное количество строк в таблицу
      var rowCount = obj1.rows.length;
      if (rowCount > input2) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input2; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input2; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              var cell3 = row.insertCell(2);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kn_oks[]' id='drugoiReg_oks_kh'>";
              //cell2.innerHTML = FormDrugoiReg_oks;
              cell3.innerHTML = "<div style='text-align: center'><b>Адресс</b></div><input class='form-control' type='text' name='adress_oks[]' id='drugoiReg_oks_adress'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}

// Условные ОКС
function Yslovniu_OKS() {
  var input1 = document.getElementById("uslovnye_oks3").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable2");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh3[]' id='yslovni_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}
//Бех КН
function Not_KN_OKS() {
  var input1 = document.getElementById("bezKn_oks4").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable3");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh4[]' id='bezKn_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}
//ЕНК
function ENK_OKS() {
  var input1 = document.getElementById("enk_oks5").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable4");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh5[]' id='enk_oks'>";
          }
      }
  }
    else {
        obj.style.display = "none";
        obj1.style.display = "none";
  }
}






function Otr_S_ZY() {
  var input1 = document.getElementById("otr_s_zy").value;
  var obj = document.getElementById("cr_pr_zu");
  var obj1 = document.getElementById("myTable5");
  console.log(input1)

  if (input1 >= 1) {
     obj.style.display = "block";
     if (obj.style.display === "block") {
        obj1.style.display = "block";
     }

     // Добавляем нужное количество строк в таблицу
     var rowCount = obj1.rows.length;
        if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i--) {
            obj1.deleteRow(i);
          }
        } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input1; i++) {
            var row = obj1.insertRow();
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = i;
            cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh8[]' id='otrS_zy' value='"  + "'>";
          }
    }

  } else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}
// Другой регион
function drygoiRegion_ZY() {
  var input2 = document.getElementById("drygoi_reg_zy").value;
  var obj = document.getElementById("cr_pr_zu");
  var obj1 = document.getElementById("myTable6");

  console.log(input2)

  if (input2 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      // Очищаем таблицу перед добавлением строк
      var rowCount = obj1.rows.length;
      if (rowCount > input2) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input2; i--) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount + 1; i <= input2; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              var cell3 = row.insertCell(2);
              cell1.innerHTML = i;
              cell2.innerHTML = "<div style='text-align: center'><b>КН</b></div><input class='form-control' type='text' name='kh6[]' id='drugoiReg_zu_kh'>";
              //cell2.innerHTML = FormDrugoiReg_oks;
              cell3.innerHTML = "<div style='text-align: center'><b>Адресс</b></div><input class='form-control' type='text' name='adress_zu[]' id='drugoiReg_zu_adress'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}

/*var b_oks =  document.getElementById('poluch_on_oks').value
var a_oks = document.getElementById('zagr_on_oks').value
var c_oks = document.getElementById('povtor_on_oks').value
*/

/*
poluch_on_oks.oninput = function() {
     b_oks = poluch_on_oks.value;
    console.log(b_oks);

zagr_on_oks.oninput = function() {
     a_oks = zagr_on_oks.value;
    console.log(a_oks);
  };
povtor_on_oks.oninput = function() {
     c_oks = povtor_on_oks.value;
    console.log(c_oks);
  };
  };*/
//console.log(c_oks + a_oks != b_oks)

//poluch_on_oks.oninput = document.getElementById("poluch_on_oks").value;

//console.log(B_oks,A_oks,C_oks)

function updateInput() {
    var b_oks =  Number(document.getElementById('poluch_on_oks').value);
    var a_oks = Number(document.getElementById('zagr_on_oks').value);
    var c_oks = Number(document.getElementById('povtor_on_oks').value);
      if(b_oks === c_oks + a_oks) {
      console.log('Равно ')
      alert('Правильное число')      //console.log(b_oks+c_oks + a_oks)
      }
      else{
      alert('Не правильное число')
  }
}

function updateInput1() {
    var d_zu =  Number(document.getElementById('zagr_on_zu').value);
    var f_zu = Number(document.getElementById('poluch_on_zu').value);
    //var f_zu1 = Number(document.getElementById('poluch_on_zu'));
    var g_zu = Number(document.getElementById('povtor_on_zu').value);
    var h_zu = Number(document.getElementById('sx_zu').value);
    var e_zu = Number(document.getElementById('np_zu').value);
    var w_zu = Number(document.getElementById('oot_zu').value);
    var k_zu = Number(document.getElementById('wf_zu').value);
    var v_zu = Number(document.getElementById('prom_zu').value);
    var n_zu = Number(document.getElementById('lf_zu').value);
    var x_zu = Number(document.getElementById('zz_zu').value);
    var q_zu = Number(document.getElementById('bezcat_zu').value);
    var y_zu = Number(document.getElementById('usl_zu').value);
    var r_zu = Number(document.getElementById('obosoblennye_zu').value);
    var checkBox = document.getElementById('myCheck1_1');

      // If the checkbox is checked, display the output text
      if (checkBox.checked == false && f_zu != d_zu + g_zu + y_zu + r_zu){
        document.getElementById('poluch_on_zu').style.backgroundColor = '#ff0000b5';
        console.log('Неправильное число 1');

      }
      if (checkBox.checked == true && f_zu != h_zu + e_zu + w_zu + k_zu + v_zu + n_zu + x_zu + q_zu + y_zu + r_zu + g_zu){
        document.getElementById('poluch_on_zu').style.backgroundColor = '#ff0000b5';
        console.log('Неправильное число 2');      //console.log(b_oks+c_oks + a_oks)


      }
    }

function checkValues() {
  var zag_on_zu = document.getElementById('zagr_on_oks').value;
  var pov_on_zu = document.getElementById('povtor_on_oks').value;
  var pch_on_zu = document.getElementById('poluch_on_oks').value;

  // Проверяем, что значения в input являются числами
  if (isNaN(zag_on_zu) || isNaN(pov_on_zu) || isNaN(pch_on_zu)) {
    document.getElementById('povtor_on_oks').style.backgroundColor = 'white'; // Если есть некорректные значения, то не меняем цвет
    return;
  }

  if (Number(zag_on_zu) + Number(pov_on_zu) == Number(pch_on_zu)) {
    document.getElementById('poluch_on_oks').style.backgroundColor = 'green';
  } else {
    document.getElementById('poluch_on_oks').style.backgroundColor = 'red';
  }
}
// Вызываем функцию при вводе значений в любой из input
document.getElementById('zagr_on_oks').addEventListener('input', checkValues);
document.getElementById('povtor_on_oks').addEventListener('input', checkValues);
document.getElementById('poluch_on_oks').addEventListener('input', checkValues);

function checkValues_zu() {
  var zag_on_zu = document.getElementById('zagr_on_zu').value;
  var pov_on_zu = document.getElementById('povtor_on_zu').value;
  var pch_on_zu = document.getElementById('poluch_on_zu').value;
  var usl_zu1 = document.getElementById('usl_zu').value;
  var osob_zu = document.getElementById('obosoblennye_zu').value;
  var checkBox = document.getElementById('myCheck1_1');


  // Проверяем, что значения в input являются числами
  if (isNaN(zag_on_zu) || isNaN(pov_on_zu) || isNaN(pch_on_zu) || isNaN(usl_zu1) ||  isNaN(osob_zu)  ) {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'white'; // Если есть некорректные значения, то не меняем цвет
    return;
  }
  if ( checkBox.checked == false) {

  if (Number(zag_on_zu) + Number(pov_on_zu) + Number(usl_zu1) + Number(osob_zu)  == Number(pch_on_zu) )  {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'green';
  } else {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'red';
  }
  }
}

// Вызываем функцию при вводе значений в любой из input
document.getElementById('zagr_on_zu').addEventListener('input', checkValues_zu);
document.getElementById('povtor_on_zu').addEventListener('input', checkValues_zu);
document.getElementById('poluch_on_zu').addEventListener('input', checkValues_zu);
document.getElementById('usl_zu').addEventListener('input', checkValues_zu);
document.getElementById('obosoblennye_zu').addEventListener('input', checkValues_zu);


function checkValues_zu_cheked() {
    var f_zu = Number(document.getElementById('poluch_on_zu').value);
    //var f_zu1 = Number(document.getElementById('poluch_on_zu'));
    var g_zu = Number(document.getElementById('povtor_on_zu').value);
    var h_zu = Number(document.getElementById('sx_zu').value);
    var e_zu = Number(document.getElementById('np_zu').value);
    var w_zu = Number(document.getElementById('oot_zu').value);
    var k_zu = Number(document.getElementById('wf_zu').value);
    var v_zu = Number(document.getElementById('prom_zu').value);
    var n_zu = Number(document.getElementById('lf_zu').value);
    var x_zu = Number(document.getElementById('zz_zu').value);
    var q_zu = Number(document.getElementById('bezcat_zu').value);
    var y_zu = Number(document.getElementById('usl_zu').value);
    var r_zu = Number(document.getElementById('obosoblennye_zu').value);
    var checkBox = document.getElementById('myCheck1_1');



  // Проверяем, что значения в input являются числами
  if ( isNaN(f_zu) || isNaN(g_zu) || isNaN(h_zu) ||  isNaN(e_zu) || isNaN(w_zu) || isNaN(k_zu) || isNaN(v_zu) || isNaN(n_zu) || isNaN(x_zu) || isNaN(q_zu) || isNaN(y_zu) || isNaN(r_zu)) {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'white'; // Если есть некорректные значения, то не меняем цвет
    return;
  }
  if ( checkBox.checked == true) {
  if (Number(h_zu) + Number(e_zu) + Number(w_zu) + Number(k_zu) + Number(v_zu) + Number(n_zu) + Number(x_zu) +Number(q_zu) + Number(y_zu) + Number(r_zu) + Number(g_zu)  == Number(f_zu) ) {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'green';
  } else {
    document.getElementById('poluch_on_zu').style.backgroundColor = 'red';
  }
  }
}
document.getElementById('poluch_on_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('povtor_on_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('sx_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('np_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('oot_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('wf_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('prom_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('lf_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('zz_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('bezcat_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('usl_zu').addEventListener('input', checkValues_zu_cheked);
document.getElementById('obosoblennye_zu').addEventListener('input', checkValues_zu_cheked);



console.log('Привет от JavaScript!');

