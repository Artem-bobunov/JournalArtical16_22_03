$(document).ready(function() {
    // Следим за изменениями состояния checkbox-ов
    $("#flexSwitchCheckDefault1, #flexSwitchCheckDefault2").change(function () {
        var totalPolucheno1 = 0;
        var totalZagruzheno1 = 0;
        var totalCountOcenka1 = 0;
        var totalCountNotOcenka1 = 0;
        var totalpoluchenoZU2 = 0;
        var totalZagruzhenoZU2 = 0;
        var totalCountOcenkaZU2 = 0;
        var totalCountNotOcenkaZU2 = 0;

        $("input#flexSwitchCheckDefault1:checked").each(function () {
            totalPolucheno1 += parseInt($(this).data("polucheno"));
            totalZagruzheno1 += parseInt($(this).data("zagruzheno"));
            totalCountOcenka1 += parseInt($(this).data("ocenka"));
            totalCountNotOcenka1 += parseInt($(this).data("not-ocenka"));
        });

        $("input#flexSwitchCheckDefault2:checked").each(function () {
            totalpoluchenoZU2 += parseInt($(this).data("poluchenozu"));
            totalZagruzhenoZU2 += parseInt($(this).data("zagruzhenozu"));
            totalCountOcenkaZU2 += parseInt($(this).data("ocenkazu"));
            totalCountNotOcenkaZU2 += parseInt($(this).data("not-ocenkazu"));
        });

        var sum1 = totalCountOcenka1 + totalCountNotOcenka1;
        var sum2 = totalCountOcenkaZU2 + totalCountNotOcenkaZU2;
        var sum = sum1 + sum2
        var totalPolucheno  = totalPolucheno1 + totalpoluchenoZU2
        var totalZagruzheno = totalZagruzheno1 + totalZagruzhenoZU2

        if (isNaN(sum1)) {
            sum1 = 0;
        }

        if (isNaN(sum2)) {
            sum2 = 0;
        }

        // Выводим итоговые значения в соответствующие элементы на странице
        $("#total-poluchenoOH").text(totalPolucheno);
        $("#total-zagruzhenoOH").text(totalZagruzheno);
        $("#total-count_ocenka").text(sum);

        $("#total-poluchenoOH_zu").text(totalpoluchenoZU2);
        $("#total-zagruzhenoOH_zu").text(totalZagruzhenoZU2);
        $("#total-count_ocenka1").text(sum2);

        localStorage.setItem('checkbox1', $('#flexSwitchCheckDefault1').prop('checked'));
        localStorage.setItem('checkbox2', $('#flexSwitchCheckDefault2').prop('checked'));

    });

});

function editData(elem, id, value) {
    console.log('Editing data with id', id, 'and value', value);
    elem.querySelector('span').setAttribute('hidden', 'hidden');
    var input = elem.querySelector('input');
    input.removeAttribute('hidden');
    input.focus();
    input.addEventListener('blur', function () {
        var newValue = this.value;
        if (value != newValue) {
            updateData(id, this.name, newValue);
        }
        elem.querySelector('span').textContent = newValue;
        input.setAttribute('hidden', 'hidden');
        elem.querySelector('span').removeAttribute('hidden');
    });
}

function updateData(id, name, newValue) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/update-data/' + id + '/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log('Data updated successfully');
        } else {
            console.log('Error updating data');
        }
    };
    var data = {};
    data[name] = newValue;

    var shouldSave = true; // Флаг, который определяет, нужно ли сохранять значение или нет

    // Проверяем, есть ли значение поля `number_act_zu` или `number_act_oks` в базе данных
    var zuFields = document.querySelectorAll('[name="number_act_zu"]');
    var oksFields = document.querySelectorAll('[name="number_act_oks"]');
    for (var i = 0; i < zuFields.length; i++) {
        var zuValue = zuFields[i].value;
        if (zuValue === newValue && zuFields[i].dataset.id !== id) {
            // Если значение уже есть в базе данных, устанавливаем флаг в `false` и вызываем модальное окно
            shouldSave = false;
            $('#myModal').modal('show');
            elem.querySelector('span').removeAttribute('hidden');
            break;
        }
    }
    if (shouldSave) {
        for (var i = 0; i < oksFields.length; i++) {
            var oksValue = oksFields[i].value;
            if (oksValue === newValue && oksFields[i].dataset.id !== id) {
                // Если значение уже есть в базе данных, устанавливаем флаг в `false` и вызываем модальное окно
                shouldSave = false;
                $('#myModal').modal('show');
                elem.querySelector('span').removeAttribute('hidden');
                

                break;
            }
        }
    }

    if (shouldSave) {
        xhr.send(JSON.stringify(data)); // Сохраняем значение, только если флаг `shouldSave` установлен в `true`

    }
}




function handleFilterChange() {
    // получаем выбранную опцию
    var selectedOption = document.querySelector('#dropdown').value;
    // находим все поля ОКС и ЗУ
    var oksFields = document.querySelectorAll('[id^=oks_container]');
    var zuFields = document.querySelectorAll('[id^=zu_container]');
    // скрываем или показываем поля в зависимости от выбранной опции
    if (selectedOption === '') { // если ничего не выбрано, показываем все поля
        for (var i = 0; i < oksFields.length; i++) {
            oksFields[i].style.display = '';
        }
        for (var i = 0; i < zuFields.length; i++) {
            zuFields[i].style.display = '';
        }
    } else if (selectedOption === 'ЗУ') {
        for (var i = 0; i < oksFields.length; i++) {
            oksFields[i].style.display = 'none';
        }
        for (var i = 0; i < zuFields.length; i++) {
            zuFields[i].style.display = '';
        }
    } else {
        for (var i = 0; i < oksFields.length; i++) {
            oksFields[i].style.display = '';
        }
        for (var i = 0; i < zuFields.length; i++) {
            zuFields[i].style.display = 'none';
        }
    }
}

// вызываем функцию обработки изменения фильтра при загрузке страницы
window.onload = function() {
    handleFilterChange();
};


