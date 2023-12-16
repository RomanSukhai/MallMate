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

  // Отримання реальних координат для src
  var srcBounds = map.getBounds();
  var srcTopLeft = srcBounds.getNorthWest();
  var srcBottomRight = srcBounds.getSouthEast();

  var w = 994, h = 706;
  var southWest = map.unproject([0, h], map.getMaxZoom());
  var northEast = map.unproject([w, 0], map.getMaxZoom());
  var bounds = new L.LatLngBounds(southWest, northEast);
  map.setMaxBounds(bounds);

  L.imageOverlay(src, bounds).addTo(map);

  // Отримання вибраного ID ТРЦ
  var selectedMallId = localStorage.getItem('selectedMallId');
  var markers = {};
  var xOffset =250; // Зсув вправо
  var yOffset = -170; // Зсув вниз
  // AJAX запит для отримання магазинів
  $.ajax({
    url: '/get_shops/' + selectedMallId,
    method: 'GET',
    success: function (shops) {
      shops.forEach(function (shop) {
        // Підрахунок реальних координат на основі src
        var x = srcTopLeft.lng + (srcBottomRight.lng - srcTopLeft.lng) * (shop.x / w)+ xOffset;
        var y = srcTopLeft.lat + (srcBottomRight.lat - srcTopLeft.lat) * (shop.y / h)+ yOffset;
        var pos = L.latLng(y, x);

        var icon = L.icon({
          iconUrl: '/static/' + shop.iconUrl.replace('/map/', '/'),
          iconSize: [shop.iconWidth, shop.iconHeight],
          iconAnchor: [shop.iconWidth / 2, shop.iconHeight / 2]
        });

        var marker = L.marker(pos, { icon: icon }).addTo(map);
        marker.bindPopup('<h1>' + shop.name + '</h1><p>Інформація про магазин...</p>');
        markers[shop.name.toLowerCase()] = marker;  // Зберігаємо маркер за назвою магазину

      });
      
      // Оновлюємо автозаповнення пошуку за назвами магазинів
      var availableTags = shops.map(function(shop) { return shop.name; });
      $("#searchInput").autocomplete({
        source: availableTags,
        select: function(event, ui) {
          var selectedShop = ui.item.value.toLowerCase();
          if (markers[selectedShop]) {
            map.setView(markers[selectedShop].getLatLng(), 5);  // Центруємо карту на маркері
            markers[selectedShop].openPopup();  // Відкриваємо вікно інформації маркера
          }
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
