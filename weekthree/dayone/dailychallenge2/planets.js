let solarSystem = {
    'Mercury' : {'moons' : 0}, 
    'Venus' : {'moons': 0}, 
    'Earth' : {'moons': 1}, 
    'Mars': {'moons' : 2}, 
    'Jupiter': {'moons' : 67}, 
    'Saturn' : {'moons': 62}, 
    'Uranus': {'moons' : 27}, 
    'Neptune': {'moons' : 14}
}

for(let planet in solarSystem){
    let planetDiv = document.createElement('div');
    planetDiv.classList.add('planet', planet.toLowerCase());
    let i = 1
    let moonDiv;
    while(i <= solarSystem[planet]['moons']){
        moonDiv = document.createElement('div');
        moonDiv.classList.add('moon', planet.toLowerCase());
        let moveMoon = (90 + (i * 30)) + 'px';
        moonDiv.style.left = moveMoon;
        changeColor(planet, moonDiv);
        planetDiv.appendChild(moonDiv);
        i++
    }
    changeColor(planet, planetDiv);
    document.body.appendChild(planetDiv);
}

function changeColor(planet, planetDiv){
    switch (planet) {
        case 'Mercury':
            planetDiv.style.backgroundColor = 'red';
            break;
        case 'Venus':
            planetDiv.style.backgroundColor = 'blue';
            break;
        case 'Earth':
            planetDiv.style.backgroundColor = 'orange';
            break;
        case 'Mars':
            planetDiv.style.backgroundColor = 'yellow';
            break;
        case 'Jupiter':
            planetDiv.style.backgroundColor = 'green';
            break;
        case 'Saturn':
            planetDiv.style.backgroundColor = 'purple';
            break;
        case 'Uranus':
            planetDiv.style.backgroundColor = 'pink';
            break;
        case 'Neptune':
            planetDiv.style.backgroundColor = 'brown';
            break;
        default :
            break;
    }
}