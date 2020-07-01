let imageSection = document.getElementById('imageSection');
let numberOfImages;
let numbersOnPage;
let resetNumber;

function chooseRandomImage(){
    let images = [
        {
            'name': 'apples',
            'url': "images/apple.png"
        }, 
        {
            'name': 'cats',
            'url': 'images/cat.png'
        }, 
        {
            'name': 'cotton candies',
            'url': 'images/cottoncandy.png'
        }, 
        {
            'name': 'pictures of Olaf',
            'url': 'images/olaf.png'
        },
        {
            'name': 'tractors',
            'url': 'images/tractor.png'
        }
    ]

    let randomNumber = Math.floor(Math.random() * 5);
    return images[randomNumber];

}

function displayImages(){
    let image = chooseRandomImage();
    numberOfImages = Math.ceil(Math.random() * 5);
    let imageSection = document.getElementById('imageSection');
    let i = 0;
    while(i < numberOfImages){
        let imageDisplay = document.createElement('img');
        imageDisplay.setAttribute('src', image['url']);
        imageSection.appendChild(imageDisplay);
        i++
    }
    return image;
}

function displayInstructions(image){
    let instructionSection = document.getElementById('instructions');
    instructionSection.innerHTML = `How many ${image['name']} do you see?`
}

function getNumberChosen(numberLocation){
    let numChosen = numberLocation.getAttribute('id');
    return turnNumberIdToNum(numChosen); 
}

function turnNumberIdToNum(numString){
    let numArray = numString.split('');
    let lastItem = numArray.length - 1;
    return Number(numArray[lastItem]);
}

function checkIfCorrectNumberChosen(){
    let numChosen = getNumberChosen(event.target);
    if(typeof resetNumber == 'object'){
        resetNumber.style.color = 'black';
    }
    if(numChosen == numberOfImages){
        event.target.style.color = 'green';
        imageSection.innerHTML = '';
        playGame();

    } else {
        event.target.style.color = 'red';
    }
    resetNumber = event.target;

}

function trackNumberClickandValidate(){
    numbersOnPage = document.getElementsByClassName('number');
    for(let number of numbersOnPage){
        number.addEventListener('click', checkIfCorrectNumberChosen);
    }
}

function playGame(){
    let image = displayImages();
    displayInstructions(image);
    trackNumberClickandValidate();
}

playGame();


