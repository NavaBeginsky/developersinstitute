let me = ["my","favorite","color","is","blue"]

//turn array to string
me = me.toString();

//my own ocd turning it to a sentence
me.replace(/,/g, ' ');

//exercise 2
let str1 = "this is";
let str2 = "nonsense";

let concat = str2.slice(0, 1) + str1.slice(1) + " " + str1.slice(0, 1) + str2.slice(1);

//exercise 3
let firstNum = prompt("Enter a first number");
let operator = prompt("Would you like to add, subtract, multiply, or divide?");
let secondNum = prompt("Enter a second number");


if (firstNum && secondNum != null) {

	switch (operator) {
		case 'add':
			document.getElementById("sum").innerHTML = Number(firstNum) + Number(secondNum);
			break;
		case 'subtract':
			document.getElementById("sum").innerHTML = Number(firstNum) - Number(secondNum);
			break;
		case 'multiply':
			document.getElementById("sum").innerHTML = Number(firstNum) * Number(secondNum);
			break;
		case 'divide':
			document.getElementById("sum").innerHTML = Number(firstNum) / Number(secondNum);
			break;
		default:
		document.getElementById("sum").innerHTML = "You need to enter a valid option ('add', 'subtract', 'multiply', 'divide')";

		}
	}
else {
	document.getElementById("sum").innerHTML = "Please enter a valid number";
}