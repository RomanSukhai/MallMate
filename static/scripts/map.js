$(document).ready(function () {
  var map = L.map('map', {
    attributionControl: false,
    zoomControl: false,
    minZoom: 1,
    maxZoom: 1, // Збільшено maxZoom
    center: [0, 0],
    zoom: 5,
    crs: L.CRS.Simple
  });
  var w = 994,
    h = 706;

  var southWest = map.unproject([0, h], map.getMaxZoom());
  var northEast = map.unproject([w, 0], map.getMaxZoom());
  var bounds = new L.LatLngBounds(southWest, northEast);

  map.setMaxBounds(bounds);

  L.imageOverlay(src, bounds).addTo(map);

  shops.forEach(function (shop) {
    var pos = map.unproject([shop.coords[0], shop.coords[1]], map.getMaxZoom());

    // Іконка без змін
    var icon = L.icon({
      iconUrl: shop.iconUrl,
      iconSize: [shop.iconWidth, shop.iconHeight], 
      iconAnchor: [shop.iconWidth / 2, shop.iconHeight / 2], 
    });

    var marker = L.marker(pos, { icon: icon }).addTo(map);
    marker.bindPopup('<h1>' + shop.name + '</h1><p>Тут інформація про магазин...</p>');
    marker.bindTooltip(shop.name, { permanent: false, direction: 'right' });
    
    var customIconHtml = '<div class="custom-icon-container">';
    if(shop.svg) {
      customIconHtml += '<img src="' + shop.svg + '" class="svg-icon" />';
    }
    customIconHtml += '</div>';
    var customIcon = L.divIcon({
      html: customIconHtml,
      className: 'custom-icon',
      iconSize: L.point(50, 50) 
    });

    L.marker(pos, { icon: customIcon }).addTo(map);
  });
});

$(document).ready(function () {
  $("#searchInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#myList li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

$(document).ready(function () {
  var availableTags = ["Елемент 1", "Елемент 2", "Елемент 3", "Елемент 4", "Елемент 5", "Елемент 6", "Елемент 7", "Елемент 8", "Елемент 9", "Елемент 10"];
  $("#searchInput").autocomplete({
    source: availableTags,
    open: function () {
      var ul = $(".ui-autocomplete:visible");
      var items = ul.find("li").length;
      var itemHeight = ul.find("li").first().outerHeight();
      ul.outerHeight(items * itemHeight);
    }
  });
});

