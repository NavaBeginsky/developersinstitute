

function computeYear() {
	let birth1 = document.getElementById('date1').value;
	let birth2 = document.getElementById('date2').value;
	let ageDiff = Math.abs(birth1 - birth2);
	let doubleYear;

	if (birth1 > birth2) {
		doubleYear = Number(birth1) + Number(ageDiff);
		
	} else {
		doubleYear = Number(birth2) + Number(ageDiff);
	}

	
	document.getElementById("results").innerHTML = doubleYear;
	
}





//exercise 2
let string = "purple";

if(string.length >= 3){

	if(string.endsWith('ing')) {
		string = string + "ly";
	} else {
	
		string = string + "ing";

	}
}