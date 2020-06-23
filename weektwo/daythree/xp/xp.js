let favColors = ['yellow', 'red', 'purple'];
for(let i = 0; i < favColors.length; i++){
	switch (i) {
		case 0:
			console.log(`My 1st choice is ${favColors[i]}`);
			break;
		case 1:
			console.log(`My 2st choice is ${favColors[i]}`);
			break;
		case 2:
			console.log(`My 3st choice is ${favColors[i]}`);
			break;
	}
}



//exercise 2
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let societyName = "";
for(name of names){
	societyName = societyName + name.charAt(0);
}
console.log(societyName);

//exercise 3
let num;
do {
	num = prompt('Give me a number');
}
while(num < 10);

//exercise 4
let people = ["Greg", "Mary", "Devon", "James"];

for(let name of people){
	console.log(name);
}
people.shift();
people[2] = "Jason";
people.push('Nava');

for(let name of people){
	if(name == "Mary"){
		console.log(name)
		break;
	}
	console.log(name);
}

let copy = people.slice(1, 3);

let marysLocation = people.indexOf('Mary');
let foosLocation = people.indexOf('Foo');

let last = people[people.length - 1];


//exercise 5
let age = [20,5,12,43,98,55];
let ageSum = age.reduce(add);

function add(total, num){
	return total + num;
}
console.log(ageSum);

for(let num of age){
	if(num % 2 == 0){
		console.log(num);
	}
}
console.log(Math.max.apply(null, age));