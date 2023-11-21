$(document).ready(function(){
    var map = L.map('map', {
        attributionControl: false,
        zoomControl: false,  
        minZoom: 2,
        maxZoom: 5,
        center: [0, 0],
        zoom: 1,
        crs: L.CRS.Simple
      });
      var w = 3840,
          h = 2160,
          url = imageMapUrl;
      
      var southWest = map.unproject([0, h], map.getMaxZoom()-1);
      var northEast = map.unproject([w, 0], map.getMaxZoom()-1);
      var bounds = new L.LatLngBounds(southWest, northEast);
      
      L.imageOverlay(url, bounds).addTo(map);
      
      map.setMaxBounds(bounds);
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

