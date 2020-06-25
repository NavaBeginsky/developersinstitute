function createSong(startNum){
    let song = '';
    let newNum;
    for(let num = startNum, numRemoved = 0; num > 0; num -= numRemoved){
        numRemoved++;
        newNum = num - numRemoved;
        if(newNum <= 0){
            song = song + `${num} bottles of beer on the wall <br> ${num} bottles of beer <br> Take ${num} down, pass them around <br> No more bottles of beer on the wall <br>`; 
        } else if(numRemoved == 1){
            song = song + `${num} bottles of beer on the wall <br> ${num} bottles of beer <br> Take ${numRemoved} down, pass it around <br> ${newNum} bottles of beer on the wall <br>`;
        } else {
            song = song + `${num} bottles of beer on the wall <br> ${num} bottles of beer <br> Take ${numRemoved} down, pass them around <br> ${newNum} bottles of beer on the wall <br>`; 
        }
        
        
        
    } 
    return song;
}
document.getElementById('beer').innerHTML = createSong(prompt('How many bottles of beer should we start with?'));