// Отрицательная площадь
function Otr_S_OKS_Update() {
  var input1 = document.getElementById("otr_s_oks1").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable2111");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      // Очищаем таблицу перед добавлением строк
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kh1[]' id='otrS_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}

// Другой регион
function drygoiRegion_OKS_Update() {
  var input2 = document.getElementById("drugoiReg_oks2").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTable12121");
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
          for (var i = rowCount - 1; i >= input2; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input2; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              var cell3 = row.insertCell(2);
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kn_oks[]' id='drugoiReg_oks_kh'>";
              //cell2.innerHTML = FormDrugoiReg_oks;
              cell3.innerHTML = "<input class='form-control' type='text' name='adress_oks[]' id='drugoiReg_oks_adress'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}




//Без КН
function Not_KN_OKS_Update() {
  var input1 = document.getElementById("bezKn_oks4").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTableBezKn_oks");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kh4[]' id='bezKn_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}


function ENK_OKS_Update() {
  var input1 = document.getElementById("enk_oks5").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTableENK_OKS");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kh5[]' id='enk_oks'>";
          }
      }
  }
    else {
        obj.style.display = "none";
        obj1.style.display = "none";
  }
}










function Otr_S_ZY_Update() {
  var input1 = document.getElementById("otr_s_zy").value;
  var obj = document.getElementById("cr_pr_zu");
  var obj1 = document.getElementById("myTable111");
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
          for (var i = rowCount - 1; i >= input1; i) {
            obj1.deleteRow(i);
          }
        } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input1; i++) {
            var row = obj1.insertRow();
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = i;
            cell2.innerHTML = "<input class='form-control' type='text' name='kh8[]' id='otrS_zy' value='"  + "'>";
          }
    }

  } else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}



function drygoiRegion_ZY_Update() {
  var input2 = document.getElementById("drygoi_reg_zy").value;
  var obj = document.getElementById("cr_pr_zu");
  var obj1 = document.getElementById("myTable61");

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
          for (var i = rowCount - 1; i >= input2; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input2; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              var cell3 = row.insertCell(2);
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kh6[]' id='drugoiReg_zu_kh'>";
              //cell2.innerHTML = FormDrugoiReg_oks;
              cell3.innerHTML = "<input class='form-control' type='text' name='adress_zu[]' id='drugoiReg_zu_adress'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}


// Условные ОКС
function Yslovniu_OKS_Update() {
  var input1 = document.getElementById("uslovnye_oks3").value;
  var obj = document.getElementById("cr_pr_oks");
  var obj1 = document.getElementById("myTableYslovniu");

  if (input1 >= 1) {
      obj.style.display = "block";
      if (obj.style.display === "block") {
          obj1.style.display = "block";
      }
      var rowCount = obj1.rows.length;
      if (rowCount > input1) {
          // Удаляем лишние строки, начиная с последней строки
          for (var i = rowCount - 1; i >= input1; i) {
              obj1.deleteRow(i);
          }
      } else {
          // Добавляем нужное количество строк в таблицу
          for (var i = rowCount; i <= input1; i++) {
              var row = obj1.insertRow();
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = i;
              cell2.innerHTML = "<input class='form-control' type='text' name='kh3[]' id='yslovni_oks'>";
          }
      }
  }
  else {
    obj.style.display = "none";
    obj1.style.display = "none";
  }
}



$(document).ready(function() {
    $('#newCounter1').click(function() {
        if ($(this).is(':checked')) {
            var counterValue = $(this).data('counter');
            $('#id_number_act_oks').val(counterValue);
        } else {
            $('#id_number_act_oks').val('');
        }
    });
});

$(document).ready(function() {
    $('#newCounter2').click(function() {
        if ($(this).is(':checked')) {
            var counterValue = $(this).data('counter');
            $('#id_number_act_zu').val(counterValue);
        } else {
            $('#id_number_act_zu').val('');
        }
    });
});