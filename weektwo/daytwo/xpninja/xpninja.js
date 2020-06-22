// let birth1; //older
// let birth2;//younger

function getFormData() {
	let birth1 = document.getElementById('date1').value;
	let birth2 = document.getElementById('date2').value;
	let ageDiff = birth2 - birth1;
	console.log(ageDiff);
	document.getElementById('results').innerHTML = "birth2 + ageDiff";
	
}

// function getHalfAge(birth1, birth2) {
// 	let ageDiff = birth2 - birth1;
// 	document.getElementById('results').innerHTML = birth2 + ageDiff;
// 	return birth2 + ageDiff;
// }




//exercise 2
let string = "purple";

if(string.length >= 3){

	if(string.endsWith('ing')) {
		string = string + "ly";
	} else {
	
		string = string + "ing";

	}
}