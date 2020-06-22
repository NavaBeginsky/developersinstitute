//exercise 1
let word = prompt('Please enter a word');
let wordArray = word.split("");

wordArray.forEach(replaceVowels);
	

function replaceVowels(letter){
	if(letter == "a" || letter == "e" || letter == "i" || letter ==  "o" || letter == "u"){
		let index = wordArray.indexOf(letter);
		wordArray.splice(index, 1, "t");
	}
}

let word2 = wordArray.toString();
word2.replace(/,/g, ' ');

console.log(word2);

//exercise 2
let lang = prompt("which language do you speak?");

switch(lang) {
	case "French":
		alert("Bonjour");
		break;
	case "English":
		alert("Hello");
		break;
	case "Hebrew":
		alert("Shalom");
		break;
	default:
		alert(':)');
}

//exercise 3

let grade = prompt('What is your grade?');

if(grade > 90){
	console.log('A');
} else if(grade > 80) {
	console.log('B');
} else if(grade > 70) {
	console.log('C');
} else if(grade < 70) {
	console.log('D');
} else {
	console.log('please enter a valid score');
}

//exercise 4

let zip = prompt("what is your zip code?");
let zipLen
if(zip.length === 5 && isNaN(zip) === false){
	console.log("good");
} else {
	console.log("error");
}