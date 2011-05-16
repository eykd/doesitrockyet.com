function $(selector) {
    return bonzo(qwery(selector));
}

$script.ready('main', function() {
    domReady(function() {
        if (!bowser.msie) {
            $('.cat').attr('src', 'http://cache.doesitrockyet.com/img/CatHeadphones_8.gif');
            $('.answer').text('Yes!');
        }
    });
});