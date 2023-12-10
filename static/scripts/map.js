$(document).ready(function(){
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

  shops.forEach(function(shop) {
    var pos = map.unproject([shop.coords[0], shop.coords[1]], map.getMaxZoom());
    
    var customHtml = `
        <div style="text-align: center;">
            <img src="${shop.iconUrl}" style="width: 38px; height: 38px;">
            <div>${shop.text}</div>
            <svg width="100" height="50">
                <!-- Тут можна додати SVG код -->
                <text x="10" y="25" fill="black">${shop.text}</text>
            </svg>
        </div>`;

        var customIcon = L.icon({
            html: customHtml,
            iconUrl: shop.iconUrl,
            iconSize: [shop.iconWidth, shop.iconHeight], // Розмір іконки для кожного магазину
            iconAnchor: [shop.iconWidth / 2, shop.iconHeight], // Якір іконки
            popupAnchor: [0, -shop.iconHeight / 2] // Якір вспливаючого вікна
        });

    L.marker(pos, {icon: customIcon}).addTo(map);
});
});

$(document).ready(function(){
    $("#searchInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myList li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

$(document).ready(function() {
    var availableTags = ["Елемент 1", "Елемент 2", "Елемент 3", "Елемент 4", "Елемент 5", "Елемент 6", "Елемент 7", "Елемент 8", "Елемент 9", "Елемент 10"];
    $("#searchInput").autocomplete({
        source:availableTags,
        open: function() {
            var ul = $(".ui-autocomplete:visible");
            var items = ul.find("li").length;
            var itemHeight = ul.find("li").first().outerHeight();
            ul.outerHeight(items * itemHeight);
        }
    });
});

