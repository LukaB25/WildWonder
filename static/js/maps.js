let map;

window.initMap = async function() {
    let latitude = parseFloat(document.getElementById('map').getAttribute('data-latitude'));
    let longitude = parseFloat(document.getElementById('map').getAttribute('data-longitude'));

    console.log(latitude, longitude);

    let position = { lat: isNaN(latitude) ? 0 : latitude, lng: isNaN(longitude) ? 0 : longitude };

    const { Map } = await google.maps.importLibrary('maps');
    const { Marker } = await google.maps.importLibrary('marker');

    map = new Map(document.getElementById('map'), {
        center: position,
        zoom: isNaN(latitude) || isNaN(longitude) ? 2 : 10,
    });

    if (!isNaN(latitude) && !isNaN(longitude)) {
        new Marker({
            position: position,
            map: map,
            title: 'Location',
        });
    }
};