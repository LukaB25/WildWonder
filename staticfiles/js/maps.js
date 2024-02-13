function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 1,
        center: {
            lat: 46.619261,
            lng: -33.134766
        },
    });

    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    var locations = [{
        lat: 44.8654, lng: 15.5820
    }];

    var markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
}
