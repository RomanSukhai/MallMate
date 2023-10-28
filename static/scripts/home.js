$(function() {
    function checkIfInView() {
        $('.animate-slide-up').each(function() {
            var elementTop = $(this).offset().top;
            var elementBottom = elementTop + $(this).outerHeight();
            var viewportTop = $(window).scrollTop();
            var viewportBottom = viewportTop + $(window).height();

            if (elementBottom > viewportTop && elementTop < viewportBottom) {
                $(this).addClass('visible'); 
            } else {
                $(this).removeClass('visible');
            }
        });
    }
    checkIfInView();
    $(window).on('scroll', checkIfInView);
});