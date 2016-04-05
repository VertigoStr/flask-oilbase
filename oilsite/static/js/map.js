ymaps.ready(init);
function init(){ 
    var myMap, 
        myPlacemark,
        list = document.getElementsByClassName('js-map');
    if (list.length > 0) {
        var zoom = list[0].getAttribute('data-zoom');
        myMap = new ymaps.Map("map", {
            center: list[0].getAttribute('data-coords').split(","),
            zoom: zoom,
            controls: []
        });

        for (var i = 0; i < list.length; i++) {
            myPlacemark = new ymaps.Placemark( 
                list[i].getAttribute('data-coords').split(","), 
                {
                    hintContent: list[i].getAttribute('data-address')
                }
            );
            myMap.geoObjects.add(myPlacemark);
        }

        $('.js-map').click(function() {       
            var x = $(this).attr('data-coords').split(",");
             myMap.panTo(
                [parseFloat(x[0]), parseFloat(x[1])], {
                    flying: true
            });
        });
    }
}