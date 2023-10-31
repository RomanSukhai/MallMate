
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

$(document).ready(function() {
    let startX = 0;
    let isDragging = false;

    $('#slider').mousedown(function(e) {
        isDragging = true;
        startX = e.pageX;
    });

    $(document).mouseup(function() {
        isDragging = false;
    });

    $('#slider').mousemove(function(e) {
        if (isDragging) {
            let moveX = e.pageX - startX;
            
            if (moveX > 50) {
                let prevChecked = $("input[name='slider']:checked").prev("input[name='slider']");
                if (prevChecked.length > 0) {
                    prevChecked.prop('checked', true);
                } else {
                    $("input[name='slider']").last().prop('checked', true);
                }
                isDragging = false;
            } else if (moveX < -50) {
                let nextChecked = $("input[name='slider']:checked").next("input[name='slider']");
                if (nextChecked.length > 0) {
                    nextChecked.prop('checked', true);
                } else {
                    $("input[name='slider']").first().prop('checked', true);
                }
                isDragging = false;
            }
        }
    });
});
$(document).ready(function() {
    $("#slider img").on("contextmenu", function(e) {
        e.preventDefault();
    });
});
$(document).ready(function() {
    const $radioButtons = $('input[type="radio"][name="slider"]');

    $('.left-arrow').click(function() {
        const $checked = $radioButtons.filter(':checked');
        const prev = $radioButtons.index($checked) - 1;
        
        if(prev >= 0) {
            $radioButtons.eq(prev).prop('checked', true);
        } else {
            // якщо ми на першому слайді і натискаємо ліву стрілку, перемикаємося на останній
            $radioButtons.last().prop('checked', true);
        }
    });

    $('.right-arrow').click(function() {
        const $checked = $radioButtons.filter(':checked');
        const next = $radioButtons.index($checked) + 1;

        if(next < $radioButtons.length) {
            $radioButtons.eq(next).prop('checked', true);
        } else {
            // якщо ми на останньому слайді і натискаємо праву стрілку, перемикаємося на перший
            $radioButtons.first().prop('checked', true);
        }
    });
});

