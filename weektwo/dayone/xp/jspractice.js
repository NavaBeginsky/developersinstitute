// exercise 1
console.log('Hi There! It\'s ' + '"sunny" outside');


// exercise 3 (first two were only in the console for the most part)
let string1 = "Here is my string, the word Nemo is included. Now I need to find it."
let array1 = string1.split(' ');
let nemoPosition = array1.indexOf('Nemo');

if(nemoPosition != -1) {
	console.log(`I found Nemo at ${nemoPosition}`);
}

else {
	console.log("I can't find nemo :(");
}
