// const GUEST_LIST = {
//   Randy: "Germany",
//   Karla: "France",
//   Wendy: "Japan",
//   Norman: "England",
//   Sam: "Argentina"
// }

// let name = prompt('What is your name');
// if (GUEST_LIST[name]) {
// 	console.log(`Hi! I'm ${name}, and I'm from ${GUEST_LIST[name]}`);
// } else {
// 	console.log("Hi! I'm a guest");
// }

// //exercise 2
// let family = {
// 	lastName: 'Beginsky',
// 	numberOfMembers: 3,
// 	city: 'Netanya'
// }
// for (let property in family) {
// 	console.log(property);
// }

// for (let property in family) {
// 	console.log(family[property]);
// }

// //exercise 3

// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan":  [4, 1000],
//         "David": [1, 10],
//     },
// }
// //Display the number of levels in the building
// console.log(building.number_levels);
// //Display how many apartments are on level 1 and 3.
// console.log(`There are ${building.number_of_apt_by_level[1]} apartments on level one and ${building.number_of_apt_by_level[3]} on level three.`);
// //Display the name of the second tenant and the number of rooms he has in his apartment
// console.log(`${building.name_of_tenants[1]} has ${building.number_of_rooms_and_rent.Dan[0]} rooms in his apartment`);

// /*Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
// If it is than inform the owner that he has to increase Dan’s rent, and ask him for a new amount.
// Change the rent of Dan accordingly inside the object.*/
// if(building.number_of_rooms_and_rent.David[1] + building.number_of_rooms_and_rent.Sarah[1] > building.number_of_rooms_and_rent.Dan[1]){
// 	let newAmount = prompt("It's time to raise Dan's rent. What is his new rent price?");
// 	building.number_of_rooms_and_rent.Dan[1] = newAmount;
// }

//exercise 4
let karen = {
	fullName: 'Karen Gross',
	mass: 80,
	height: 1.70,
	bmiCalc() {
	return this.mass / (Math.pow(this.height, 2));
}
};

let mary = {
	fullName: 'Mary Allen',
	mass: 95,
	height: 1.70,
	bmiCalc() {
	return this.mass / (Math.pow(this.height, 2));
}
};

function compareBmi(person, person2){
	if(person.bmiCalc() > person2.bmiCalc()){
		alert(person.fullName + ' is bigger');
	} else {
		alert(`${person2.fullName} is bigger`);
	}
	
}

compareBmi(karen, mary);

