import L from 'leaflet';

const MAP = L.map('map')


async function fetchAPI(url){
    const response = await fetch(url)
    const data = await response.json()
    return data
}


async function createMap(){
    const ma = MAP.setView([-23.555, -46.635], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(ma);  

    const data = await fetchAPI("http://127.0.0.1:9000/accounts/api/v1/accounts/produtores")

    for(let i = 0; i < data.length; i++){
        const marker = L.marker([data[i].latitude, data[i].longitude]).addTo(ma);
        marker.bindPopup(`<b>${data[i].nome_fantasia}!</b><br>${data[i].logradouro} - ${data[i].numero}.`).openPopup();

    }
}

async function addSearchListener(){
    const botaoBuscar = document.getElementById('buscar-button');

    botaoBuscar.addEventListener('click', () =>{
        updateMap()
    })
}

async function updateMap(){
    const loader = document.getElementById('loader')

    MAP.unload()
    loader.style.display = 'block'



    loader.style.display = 'none'

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