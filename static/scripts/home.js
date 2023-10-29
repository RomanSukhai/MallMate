function throttle(func, delay) {
    let lastCall = 0;
    return function() {
        let now = Date.now();
        if (now - lastCall < delay) {
            return;
        }
        lastCall = now;
        return func.apply(this, arguments);
    };
}

$(function() {
    function checkIfInView() {
        var offset = 200; 
        $('.animate-slide-up:not(.visible)').each(function() {
            var elementTop = $(this).offset().top;
            var elementBottom = elementTop + $(this).outerHeight();
            var viewportTop = $(window).scrollTop() - offset;
            var viewportBottom = viewportTop + $(window).height() + offset;

            if (elementTop < viewportBottom && elementBottom > viewportTop) {
                $(this).addClass('visible'); 
            }
        });
    }
    function onScroll() {
        requestAnimationFrame(checkIfInView);
    }
    $(window).on('scroll', throttle(onScroll, 250));
});

