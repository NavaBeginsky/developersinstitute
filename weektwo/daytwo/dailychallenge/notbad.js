let string1 = "This exercise is not so bad";
let notIndex = string1.indexOf("not");
let badIndex = string1.indexOf("bad");

if(notIndex < badIndex){
	let badRemoved = string1.slice(notIndex, badIndex + 3);
	console.log(string1.replace(badRemoved, 'good'));
} else {
	console.log(string1);
}