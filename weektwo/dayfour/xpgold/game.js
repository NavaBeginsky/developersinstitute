function playTheGame(){
	let confirmPlay = confirm('Do you want to play the game?');	
	if(confirmPlay == false){
		alert('No problem, Goodbye');
	} else{
		let userNum = Number(prompt('Enter a number between 0-10'));
		if(typeof userNum != 'number'){
			alert('Sorry Not a number, Goodbye');
		} else if(userNum > 10 || userNum < 0){
			alert('Sorry it’s not a good number, Goodbye');
		} else {
			let computerNumber = Math.floor(Math.random() * 11);
			test(userNum, computerNumber);
		}
		
	}

}

function test(userNumber, computerNumber){
	for(let i = 1; i < 3; i++){
		if(userNumber == computerNumber){
			alert('You win the game!');
			return;
		} else if(userNumber > computerNumber){
			userNumber = prompt('Your number was too big, guess again');
		} else if(userNumber < computerNumber){
			userNumber = prompt('Your number was too low, guess again');
		} 
	}
	if(userNumber == computerNumber){
			alert('You win the game!');
	} else {
	alert('You ran out of guesses! The computer\'s number was ' + computerNumber);
	}
}

