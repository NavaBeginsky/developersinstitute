function add(num, num2){
	console.log(num+num2);
}

sum(3, 5);

function evenOrOdd(num){
	if(num % 2 == 0){
		console.log(`${num} is even`)
	} else {
		console.log(`${num} is odd`)	
	}
}

evenOrOdd(6);

function askForAge(){
	return prompt('What is your age?');
}

function doubleNumber(number){
	return number * 2;
}

let age = askForAge();
console.log(doubleNumber(age));
