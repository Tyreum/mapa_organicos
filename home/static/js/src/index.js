import L from 'leaflet';


function createMap(){
    const ma = L.map('map').setView([-23.555, -46.635], 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(ma);  
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

async function addUserButtonDropDown(){
    const registerButton = document.getElementById('userIcon');
    const registerOptions = document.getElementById('userOptions')

    registerButton.addEventListener('click', () => {
        if(registerOptions.style.display === 'none'){
            registerOptions.style.display = 'flex';
        }else{
            registerOptions.style.display = 'none'
        }
    })
} 



addRegisterButtonDropDown()
createMap()