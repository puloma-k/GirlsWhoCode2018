
var view;
var ourLoc;
var countryRequest;

function init() {
    ourLoc = ol.proj.fromLonLat([-122.151602, 37.481990])

    view = new ol.View({
        center: ourLoc,
        zoom: 6
    });

    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
            source: new ol.source.OSM()
            })
        ],
        view: view
    });
}

function panHome() {
    view.animate({
        center: ourLoc,
        duration: 1500
    });
}

function panToLocation() {
    var countryName = document.getElementById("country-name").value;
    var query = "https://restcountries.eu/rest/v2/name/" + countryName + "?fullText=true"

    countryRequest = new XMLHttpRequest();
    countryRequest.open("GET", query, true);
    countryRequest.send();

    // alert("Ready state " + countryRequest.readyState)
    // alert("status " + countryRequest.status)
    // alert("response " + countryRequest.responseText)

    countryRequest.onload = processCountryRequest;
}

function processCountryRequest() {
    var cleanedResponse = JSON.parse(countryRequest.responseText)

    if (countryRequest.readyState != 4 || countryRequest.status != 200) {
        alert("Error");
    }

    var lat = cleanedResponse[0].latlng[0]
    var lon = cleanedResponse[0].latlng[1]

    var location = ol.proj.fromLonLat([lon, lat])

    view.animate({
        center: location,
        duration: 1500
    });
}















window.onload = init
