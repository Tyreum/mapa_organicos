import * as L from 'leaflet/dist/leaflet';


const MAP = L.map('map')
var markersCluster = []

async function fetchAPI(url){
    const response = await fetch(url)
    const data = await response.json()
    return data
}

async function removeAllMarkers(){
    for(let j = 0; j < markersCluster.length; j++){
        markersCluster[j].remove()
    }
}

async function updateProdutorCardList(data, element){
    const cardsNode = document.getElementsByClassName('card-produtor');

    
}

async function setMarkerColor(marker, data){
    if(data.tipo_produtor === 'F'){
        marker._icon.classList.add("green-marker");
    }
    else if(data.tipo_produtor === 'P'){
        marker._icon.classList.add("green-marker");
    }
}

async function setMarkers(data, map){
    const marker = L.marker([data.latitude, data.longitude], {color:"red"}).addTo(map);
    marker.bindPopup(`<b>${data.nome_fantasia}!</b><br>${data.logradouro} - ${data.numero}.`).openPopup();
    await setMarkerColor(marker, data);
    markersCluster.push(marker)
}


async function createMap(){
    const ma = MAP.setView([-23.555, -46.635], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(ma);  

    const data = await fetchAPI("http://127.0.0.1:9000/accounts/api/v1/accounts/produtores")


    for(let i = 0; i < data.length; i++){
        setMarkers(data[i], ma);
        updateProdutorCardList(data, data)
    }
}

async function addSearchListener(){
    const botaoBuscar = document.getElementById('buscar-button');

    botaoBuscar.addEventListener('click', () =>{
        updateMap()
    })
}

async function getFilterValues(){
    try{
        const nomeProdutor = document.getElementById('value-filter-nome').innerHTML;
        const bairroProdutor = document.getElementById('value-filter-bairro').value;
        const url = `http://127.0.0.1:9000/accounts/api/v1/accounts/produtores?nomeProdutor=${nomeProdutor}&bairroProdutor=${bairroProdutor}`
        return url

    }catch{

    }  
}

async function updateMap(){
    removeAllMarkers()

    const data = await fetchAPI(await getFilterValues())
    for(let i = 0; i < data.length; i++){
        const marker = L.marker([data[i].latitude, data[i].longitude]).addTo(MAP);
        marker.bindPopup(`<b>${data[i].nome_fantasia}!</b><br>${data[i].logradouro} - ${data[i].numero}.`).openPopup();
        await setMarkerColor(marker, data[i]);
        markersCluster.push(marker)
    }
}


async function addRegisterButtonDropDown(){
    const registerButton = document.getElementById('registerButton');
    const registerOptions = document.getElementById('registerOptions')

    registerButton.addEventListener('click', () => {
        if(registerOptions.style.display === 'none'){
            registerOptions.style.display = 'flex';
        }else{
            registerOptions.style.display = 'none'
        }
    })
} 


addSearchListener()
addRegisterButtonDropDown()
createMap()