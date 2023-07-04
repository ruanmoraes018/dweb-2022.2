var mapElement = document.getElementById('map');
var lat_origem = mapElement.getAttribute('data-lat-origem');
var lng_origem = mapElement.getAttribute('data-lng-origem');
var lat_destino = mapElement.getAttribute('data-lat-destino');
var lng_destino = mapElement.getAttribute('data-lng-destino');

var lat_media = (parseFloat(lat_origem) + parseFloat(lat_destino)) / 2;
var lng_media = (parseFloat(lng_origem) + parseFloat(lng_destino)) / 2;

var map = L.map('map').setView([lat_media, lng_media], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18, // Ajuste o valor máximo de zoom conforme necessário
}).addTo(map);

var origemMarker = L.marker([lat_origem, lng_origem]).addTo(map);
var destinoMarker = L.marker([lat_destino, lng_destino]).addTo(map);

var rota = L.polyline([[lat_origem, lng_origem], [lat_destino, lng_destino]], { color: 'red' }).addTo(map);

// Calcula a distância entre os pontos de origem e destino
var distancia = map.distance([lat_origem, lng_origem], [lat_destino, lng_destino]);

// Função para ajustar o zoom e visualização do mapa
function ajustarZoomMapa() {
    map.fitBounds(rota.getBounds().pad(0.1), {
        maxZoom: 15, // Ajuste o valor máximo de zoom conforme necessário
    });
}

// Chama a função quando a janela for redimensionada
window.onresize = ajustarZoomMapa;

// Chama a função inicialmente para ajustar o zoom ao carregar a página
ajustarZoomMapa();



//Segunda Versão

// var mapElement = document.getElementById('map');
// var lat_origem = mapElement.getAttribute('data-lat-origem');
// var lng_origem = mapElement.getAttribute('data-lng-origem');
// var lat_destino = mapElement.getAttribute('data-lat-destino');
// var lng_destino = mapElement.getAttribute('data-lng-destino');

// var lat_media = (parseFloat(lat_origem) + parseFloat(lat_destino)) / 2;
// var lng_media = (parseFloat(lng_origem) + parseFloat(lng_destino)) / 2;

// var map = L.map('map').setView([lat_media, lng_media], 13);

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
//     maxZoom: 18, // Ajuste o valor máximo de zoom conforme necessário
// }).addTo(map);

// var origemMarker = L.marker([lat_origem, lng_origem]).addTo(map);
// var destinoMarker = L.marker([lat_destino, lng_destino]).addTo(map);

// var rota = L.polyline([[lat_origem, lng_origem], [lat_destino, lng_destino]], { color: 'red' }).addTo(map);

// // Calcula a distância entre os pontos de origem e destino
// var distancia = map.distance([lat_origem, lng_origem], [lat_destino, lng_destino]);

// // Ajusta o zoom com base na distância
// map.fitBounds(rota.getBounds().pad(0.1), {
//     maxZoom: 15, // Ajuste o valor máximo de zoom conforme necessário
// });





//Primeira versão

// var mapElement = document.getElementById('map');
// var lat_origem = mapElement.getAttribute('data-lat-origem');
// var lng_origem = mapElement.getAttribute('data-lng-origem');
// var lat_destino = mapElement.getAttribute('data-lat-destino');
// var lng_destino = mapElement.getAttribute('data-lng-destino');

// var map = L.map('map').setView([lat_origem, lng_origem], 13);

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
//     maxZoom: 10,
// }).addTo(map);

// var origemMarker = L.marker([lat_origem, lng_origem]).addTo(map);
// var destinoMarker = L.marker([lat_destino, lng_destino]).addTo(map);

// var rota = L.polyline([[lat_origem, lng_origem], [lat_destino, lng_destino]], { color: 'red' }).addTo(map);
