const newItem = function () {
    let new_item = $('#dummy_item').clone();
    new_item.removeProp('id');
    new_item.addClass('option-item');
    return new_item;
};

let clickCorrect = function () {
    if ($('#type').val() === '2') {
        $('.item-correct').prop('checked', false);
    }
    $(this).prop('checked', true);
};

let refreshNum = function () {
    let num = 'A'.charCodeAt();
    $('.option-item').each(function () {
        let content = $(this).find('.item-num').text(String.fromCharCode(num));
        num++;
    });
};

const addOption = function (is_correct, content) {
    if ($('.option-item').length >= 26) {
        alert('选项数量到达上限！');
        return;
    }

    let item = newItem();

    let item_correct = item.find('.item-correct');
    item_correct.prop('checked', is_correct);
    item_correct.click(clickCorrect);

    item.find('.item-content').val(content);
    item.find('.item-delete').click(function () {
        item.remove();
        refreshNum();
    });
    $('#t_options').find('tbody').append(item);
    item.fadeIn('fast');

    refreshNum();
};

const getData = function () {
    let type = $('#type').val();
    let data = {'data': null, 'correct': null};

    if (type === '1') {
        if ($('#item_true').is(':checked'))
            data['correct'] = true;
        else if ($('#item_false').is(':checked'))
            data['correct'] = false;
    } else if (type === '2' || type === '3') {
        data['data'] = [];
        data['correct'] = [];

        $('.option-item').each(function () {
            let correct = $(this).find('.item-correct').is(':checked');
            let content = $(this).find('.item-content').val();
            data['data'].push(content);
            data['correct'].push(correct);
        });
    }

    return data;
};

const injectData = function () {
    let type = $('#type').val();
    let data_str = $('#data').val();
    let correct_str = $('#correct').val();

    if (data_str !== '' && correct_str !== '') {
        let data = JSON.parse(data_str);
        let correct = JSON.parse(correct_str);

        if (type === '1') {
            if (correct) {
                $('#item_true').prop('checked', true);
            } else {
                $('#item_false').prop('checked', true);
            }
        } else if (type === '2' || type === '3') {
            for (let i = 0; i < data.length; i++) {
                addOption(correct[i], data[i]);
            }
        }
    }
};

const selectType = function (type, speed) {
    if (type == null)
        type = $('#type').val();

    let content_judge = $('#content_judge');
    let content_select = $('#content_select');

    if (type === '1') {
        content_judge.slideDown(speed);
        content_select.slideUp(speed);
    } else if (type === '2' || type === '3') {
        content_judge.slideUp(speed);
        content_select.slideDown(speed);
    } else {
        content_judge.slideUp(speed);
        content_select.slideUp(speed);
    }
};


$('#b_add').click(function () {
    addOption(false, '');
});

$('#form').submit(function (event) {
    let data = getData();
    $('#data').val(JSON.stringify(data['data']));
    $('#correct').val(JSON.stringify(data['correct']));
});


$('#type').change(function () {
    selectType($(this).val(), 'fast');
});

injectData();
selectType(null, 0);