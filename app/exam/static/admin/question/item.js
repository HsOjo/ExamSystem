const newItem = function () {
    let new_item = $('#dummy_item').clone();
    new_item.removeAttr('id');
    new_item.addClass('option-item');
    return new_item;
};

const addOption = function (is_correct, content) {
    let item = newItem();
    item.find('.item-correct').attr('checked', is_correct);
    item.find('.item-content').val(content);
    item.find('.item-delete').click(function () {
        item.remove();
    });
    $('#t_options').find('tbody').append(item);
    item.fadeIn('fast');
};

const getData = function () {
    let data = {'data': [], 'correct': []};

    $('.option-item').each(function () {
        let correct = $(this).find('.item-correct').is(':checked');
        let content = $(this).find('.item-content').val();
        data['data'].push(content);
        data['correct'].push(correct);
    });

    return data;
};

const injectData = function () {
    let data = JSON.parse($('#data').val());
    let correct = JSON.parse($('#correct').val());
    for (let i = 0; i < data.length; i++) {
        addOption(correct[i], data[i]);
    }
};