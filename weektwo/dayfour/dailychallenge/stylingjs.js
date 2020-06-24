let stringOfWords = prompt('Give me a string of words');
let arrayOfWords = stringOfWords.split(" ");
console.log('*'.repeat(stringOfWords.length));
for(let word of arrayOfWords){
	console.log(`* ${word}` + " ".repeat(stringOfWords.length - word.length - 3) + "*");
}
console.log('*'.repeat(stringOfWords.length));
