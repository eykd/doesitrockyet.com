function $(selector) {
    return bonzo(qwery(selector));
}

$script.ready('main', function() {
    if (!bowser.msie) {
        $('.cat').attr('src', 'img/CatHeadphones_8.gif');
        $('.answer').text('Yes!');
    }
});