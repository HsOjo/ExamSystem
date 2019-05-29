function init() {
    $('.js-del-confirm').click(function () {
        return confirm('你确定要删除吗？');
    });
}

init();