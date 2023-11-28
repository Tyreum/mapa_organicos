import L from 'leaflet';
// import 'leaflet/dist/leaflet.css'


function teste(){
    const ma = L.map('map').setView([-23.555, -46.635], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(ma);  
}



teste()