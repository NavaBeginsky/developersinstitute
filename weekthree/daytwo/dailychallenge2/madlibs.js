let userInput = [];
let libButton = document.getElementById('lib-button');

let libIt = function() {
    saveUserInput();
    let storyDiv = document.getElementById("story");
    storyDiv.innerHTML = `Once there was a ${userInput[0]}. It was incredibly ${userInput[1]}. It looked just like ${userInput[2]}`;
};

libButton.addEventListener('click', libIt);

function saveUserInput(){
    userInput[0] = saveNoun();
    userInput[1] = saveAdjective();
    userInput[2] = saveName();
}

function saveNoun(){
    let nounLocation = document.getElementById('noun');
    return nounLocation.value;
}
function saveAdjective(){
    let adjectiveLocation = document.getElementById('adjective');
    return adjectiveLocation.value;
}
function saveName(){
    let personLocation = document.getElementById('person');
    return personLocation.value;
}