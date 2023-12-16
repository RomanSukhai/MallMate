$(document).ready(function () {
  // Ініціалізація карти
  var map = L.map('map', {
    attributionControl: false,
    zoomControl: false,
    minZoom: 1,
    maxZoom: 1,
    center: [0, 0],
    zoom: 5,
    crs: L.CRS.Simple
  });

  var w = 994, h = 706;
  var southWest = map.unproject([0, h], map.getMaxZoom());
  var northEast = map.unproject([w, 0], map.getMaxZoom());
  var bounds = new L.LatLngBounds(southWest, northEast);
  map.setMaxBounds(bounds);

  L.imageOverlay(src, bounds).addTo(map);

  // Отримання вибраного ID ТРЦ
  var selectedMallId = localStorage.getItem('selectedMallId');

  // AJAX запит для отримання магазинів
  $.ajax({
    url: '/get_shops/' + selectedMallId,
    method: 'GET',
    success: function (shops) {
      shops.forEach(function (shop) {
        var pos = L.latLng(shop.y, shop.x); // Використовуємо координати y, x
        var iconUrl = shop.iconUrl.replace('/map/', '/');

        var icon = L.icon({
          iconUrl: iconUrl,
          iconSize: [shop.iconWidth, shop.iconHeight],
          iconAnchor: [shop.iconWidth / 2, shop.iconHeight / 2]
        });

        var marker = L.marker(pos, { icon: icon }).addTo(map);
        marker.bindPopup('<h1>' + shop.name + '</h1><p>Інформація про магазин...</p>');
      });
      
      // Оновлюємо автозаповнення пошуку за назвами магазинів
      var availableTags = shops.map(function(shop) { return shop.name; });
      $("#searchInput").autocomplete({
        source: availableTags,
        open: function () {
          var ul = $(".ui-autocomplete:visible");
          var items = ul.find("li").length;
          var itemHeight = ul.find("li").first().outerHeight();
          ul.outerHeight(items * itemHeight);
        }
      });
    },
    error: function(xhr, status, error) {
      console.log("Помилка отримання даних: ", error);
    }
  });

  // Функція пошуку
  $("#searchInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#myList li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
