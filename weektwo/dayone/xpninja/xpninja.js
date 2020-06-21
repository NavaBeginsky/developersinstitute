let numbers = prompt("Please enter a string of numbers separated by a comma and space");

numbers = numbers.split(',');

if(numbers.length > 1){
	
	let sum = numbers.reduce((a, b) => a * b);
	console.log(sum);
}
else {
	console.log('Please Enter More Then One Number');
}

//exercise 2
let num = prompt("Please enter a number");
let boom;

if(num > 2) {
	boom = "b" + "o".repeat(num) + "m";
}
else {
	boom = "boom"
}

if(num % 2 == 0){
	boom = boom + "!";
}

if(num % 5 == 0) {
	boom = boom.toUpperCase();
}