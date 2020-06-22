
// exercise 1
let x = 7;
let y = 3;

if (x > y) {
	alert(x);
} else {
	alert(y);
}

//exercise 2
let newDog = "Chihuahua";
alert(newDog.length);
alert(newDog.toUpperCase());
alert(newDog.toLowerCase());

if(newDog == 'Chihuahua'){
	alert('I LOVE Chihuahua, it\’s my favorite dog');

} else {
	console.log('I dont care, I prefer CATS')
}

//exercise 3
let num = prompt('Please enter a number');

if(num % 2 == 0){
	alert(`${num} is an even number`);
} else {
	alert(`${num} is not an even number`);
}

//exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let userCount = users.length;
switch(userCount) {
	case 0:
		console.log('no one online');
		break;
	case 1:
		console.log(`${users[0]} online`);
		break;
	case 2:
		console.log(`${users[0]} and ${users[1]} online`);
		break;
	default:
		let remaining = userCount - 2;
		console.log(`${users[0]} and ${users[1]} and ${remaining} more online`);
		break;

}