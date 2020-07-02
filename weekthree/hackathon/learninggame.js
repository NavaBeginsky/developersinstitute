let imageSection = document.getElementById('imageSection');
let numberOfImages;
let numbersOnPage;
let resetNumber;
let instructionSection = document.getElementById('instructions');
let incorrectBoxes = document.querySelectorAll('.incorrect .checkbox');
let correctBoxes = document.querySelectorAll('.correct .checkbox');
let numberSection = document.getElementById('numberSection');
let audioSection = document.getElementById('myAudio');
let currentLevel = 1;
let levelUpNumbers = document.querySelector('#numberSection .levelup');

function chooseRandomImage(){
    let images = [
        {
            'name': 'apples',
            'url': "images/apple.png",
            'sound': "recordings/apple.mp3"
        }, 
        {
            'name': 'cats',
            'url': 'images/cat.png',
            'sound': 'recordings/cats.mp3'
        }, 
        {
            'name': 'cotton candies',
            'url': 'images/cottoncandy.png',
            'sound': 'recordings/cottoncandy.mp3'
        }, 
        {
            'name': 'pictures of Olaf',
            'url': 'images/olaf.png',
            'sound': 'recordings/olaf.mp3'
        },
        {
            'name': 'tractors',
            'url': 'images/tractor.png',
            'sound': 'recordings/truck.mp3'
        }
    ]

    let randomNumber = Math.floor(Math.random() * 5);
    return images[randomNumber];

}

function displayImages(){
    let image = chooseRandomImage();
    if(currentLevel === 1){
        numberOfImages = Math.ceil(Math.random() * 5);
    } else {
        numberOfImages = Math.ceil(Math.random() * 10);
    }
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

function getNumberChosen(numberLocation){
    let numChosen = numberLocation.getAttribute('id');
    return turnNumberIdToNum(numChosen); 
}

function turnNumberIdToNum(numString){
    let numArray = numString.split('');
    let lastItem = numArray.length - 1;
    if (Number(numArray[lastItem]) === 0){
        return 10;
    } else {
        return Number(numArray[lastItem]);

    }
}

function checkIfCorrectNumberChosen(){
    let numChosen = getNumberChosen(event.target);
    if(typeof resetNumber == 'object'){
        resetNumber.style.color = 'black';
    }
    if(numChosen == numberOfImages){
        imageSection.innerHTML = '';
        result = markCorrect();
        if (result != "stop") {playGame()};

    } else {
        event.target.style.color = 'red';
        markIncorrect();
    }
    resetNumber = event.target;

}

function markCorrect(){
    let numOfBoxes = correctBoxes.length;
    for(let i=0; i < numOfBoxes; i++){
        if(correctBoxes[i].classList.contains('green')){
            continue;
        } else if (i == numOfBoxes-1){
            correctBoxes[i].classList.add('green');
            youWin();
            return "stop";
        } else {
            correctBoxes[i].classList.add('green');
            break;
        }
    }
}

function markIncorrect(){
    let numOfBoxes = incorrectBoxes.length;
    for(let i=0; i < numOfBoxes; i++){
        if(incorrectBoxes[i].classList.contains('red')){
            continue;
        } else if (i == numOfBoxes-1){
            incorrectBoxes[i].classList.add('red');
            gameOver();
            return;
        } else {
            incorrectBoxes[i].classList.add('red');
            break;
        }
    }
}

function trackNumberClickandValidate(){
    numbersOnPage = document.getElementsByClassName('number');
    for(let number of numbersOnPage){
        number.addEventListener('click', checkIfCorrectNumberChosen);
    }
}

function playGame(){
    let playButton = document.getElementById('playTheGame');
    if(playButton != null){
        playButton.remove();
    }    
    let image = displayImages();
    instructionSection.innerHTML = `How many ${image['name']} do you see?`;
    playAudio(image);
    trackNumberClickandValidate();
}

function gameOver(){
    instructionSection.innerHTML = "You lose! Want to play again?";
    restartButton();
}

function youWin(){
    confetti.start(3000);
    if(currentLevel === 1){
        levelUp();
    } else{
        instructionSection.innerHTML = "You win! Want to play again?";
        restartButton();
    }
}

function levelUp(){
    for(let box of correctBoxes){
        box.classList.remove('green');
    }
    currentLevel++
    levelUpNumbers.style.display = 'inline-block';
    playGame();
}

function resetGame(){
    imageSection.innerHTML = '';
    currentLevel = 1;
    levelUpNumbers.style.display = 'none';
    for(let box of incorrectBoxes){
        box.classList.remove('red');
    }
    for(let box of correctBoxes){
        box.classList.remove('green');
    }
    numberSection.style.display = 'block';
    if(typeof resetNumber == 'object'){
        resetNumber.style.color = 'black';
    }
    playGame();
}

function restartButton(){
    let restartButton = document.createElement('button');
    imageSection.innerHTML = '';
    restartButton.innerText = 'Play Again!';
    imageSection.appendChild(restartButton);
    restartButton.setAttribute('onclick', 'resetGame()'); 
    numberSection.style.display = 'none';
}

function playAudio(imageChosen){
    // let audio = document.getElementById('audio');
    // audio.setAttribute('src', imageChosen['sound']);
    console.log(audio);
    audioSection.play();

}
