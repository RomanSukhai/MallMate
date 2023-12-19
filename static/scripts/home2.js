function throttle(func, delay) {
    let lastCall = 0;
    return function () {
        let now = Date.now();
        if (now - lastCall < delay) {
            return;
        }
        lastCall = now;
        return func.apply(this, arguments);
    };
}

$(function () {
    function checkIfInView() {
        var offset = 200;
        $('.animate-slide-up:not(.visible)').each(function () {
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

$(document).ready(function () {
    let startX = 0;
    let isDragging = false;
    $('#slider').mousedown(function (e) {
        isDragging = true;
        startX = e.pageX;
    });
    $(document).mouseup(function () {
        isDragging = false;
    });
    $('#slider').mousemove(function (e) {
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

$(document).ready(function () {
    $("#slider img").on("contextmenu", function (e) {
        e.preventDefault();
    });
});

$(document).ready(function () {
    const $radioButtons = $('input[type="radio"][name="slider"]');
    $('.left-arrow').click(function () {
        const $checked = $radioButtons.filter(':checked');
        const prev = $radioButtons.index($checked) - 1;
        if (prev >= 0) {
            $radioButtons.eq(prev).prop('checked', true);
        } else {
            $radioButtons.last().prop('checked', true);
        }
    });
    $('.right-arrow').click(function () {
        const $checked = $radioButtons.filter(':checked');
        const next = $radioButtons.index($checked) + 1;
        if (next < $radioButtons.length) {
            $radioButtons.eq(next).prop('checked', true);
        } else {
            $radioButtons.first().prop('checked', true);
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const sr = ScrollReveal({
        distance: '150px',
        duration: 1700,
        reset: false
    });
    const sr2 = ScrollReveal({
        distance: '200px',
        duration: 2000,
        reset: false
    });
    sr2.reveal('#fromTopHeader', { origin: 'top' });
    sr.reveal('#fromTop', { origin: 'top' });
    sr.reveal('#fromLeft', { origin: 'left' });
    sr.reveal('#fromRight', { origin: 'right' });
    sr.reveal('#fromBottom', { origin: 'bottom' });
});

$(document).ready(function () {
    var mySwiper = new Swiper('.mySwiper', {
        spaceBetween: 100,
        centeredSlides: true,
        autoplay: {
            delay: 3500,
            disableOnInteraction: false,
        },
        speed: 1100,
    });
});

$(document).ready(function () {
    var mySwiper = new Swiper('.myUniqueSwiper', {
        direction: 'vertical',
        spaceBetween: 5,
        centeredSlides: true,
        autoplay: {
            delay: 3500,
            disableOnInteraction: false,
        },
        speed: 1100,
    });
});

$(document).ready(function () {
    var divCreated = false;

    function updateMallName() {
        var savedMallName = localStorage.getItem('selectedMallName');
        if (savedMallName) {
            $('#createDiv p').text(savedMallName);
        } else {
            $('#createDiv p').text('Виберіть ТРЦ..');
        }
    }

    $('#createDiv').click(function (e) {
        e.preventDefault();

        if (!divCreated) {
            var newDiv = $(
                '<div class="TRZ_submit d-flex flex-wrap flex-row">' +
                '<button class="closeDiv d-flex align-content-start justify-content-center">' +
                '<img src="../static/icons/cancel.svg" alt="Закрити">' +
                '</button>' +
                '<p>Оберіть спершу місто, <br> а потім ТЦ</p>' +
                '<div class="dropdown">' +
                '<label for="city-select"><p>Оберіть місто:</p></label>' +
                '<select id="city-select">' +
                '<option value="">Виберіть місто...</option>' +
                '</select>' +
                '</div>' +
                '<div class="dropdown">' +
                '<label for="mall-select"><p>Оберіть ТЦ:</p></label>' +
                '<select id="mall-select" disabled>' +
                '<option value="">Спочатку виберіть місто...</option>' +
                '</select>' +
                '</div>' +
                '</div>'
            );

            $('body').append(newDiv);
            divCreated = true;

            fetch('/get-cities')
                .then(response => response.json())
                .then(cities => {
                    var citySelect = $('#city-select');
                    cities.forEach(function(city) {
                        citySelect.append(new Option(city.name, city.id));
                    });
                    var savedCityId = localStorage.getItem('selectedCityId');
                    if (savedCityId) {
                        $('#city-select').val(savedCityId).change();
                    }
                });

            $('#city-select').change(function() {
                var cityId = $(this).val();
                var mallSelect = $('#mall-select').empty().append('<option value="">Виберіть ТЦ...</option>').prop('disabled', true);

                if (cityId) {
                    localStorage.setItem('selectedCityId', cityId);
                    fetch('/get-malls?cityId=' + cityId)
                        .then(response => response.json())
                        .then(malls => {
                            mallSelect.prop('disabled', false);
                            malls.forEach(function(mall) {
                                mallSelect.append(new Option(mall.name, mall.id));
                            });
                            var savedMallId = localStorage.getItem('selectedMallId');
                            if (savedMallId) {
                                $('#mall-select').val(savedMallId).change();
                            }
                        });
                } else {
                    localStorage.removeItem('selectedCityId');
                    localStorage.removeItem('selectedMallId');
                    localStorage.removeItem('selectedMallName');
                    updateMallName();
                }
            });

            $('#mall-select').change(function() {
                var mallId = $(this).val();
                var mallName = $(this).find('option:selected').text();
                localStorage.setItem('selectedMallId', mallId);
                localStorage.setItem('selectedMallName', mallName);

                updateMallName();
            });

            $('body').on('click', '.closeDiv', function () {
                $(this).parent().remove();
                divCreated = false;
                updateMallName();
            });
        }
    });

    updateMallName();
});
