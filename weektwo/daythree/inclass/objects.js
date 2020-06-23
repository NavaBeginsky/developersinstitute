let myObject = {
	username : "nava",
	password : "test123"
}

let database = [myObject];

let newsfeed = [ 
	{
		username: "1",
		timeline: 't1'
	}, {
		username: "2",
		timeline: 't2'

	}, {
		username: "3",
		timeline: 't3'

	} 
];

//exercise 2
for(i = 0; i <= 15; i++){
	if(i % 2 == 0){
		console.log(`${i} is even`);
	} else {
		console.log(`${i} is odd`);
	}
}

//impromptu exercise


// 1. Loop through the array of object
// 2. If the username is Sarah : say hello to her friends (display the name of her friends)
// 3. If the username is Dan : change his password to 567

let users = [
    {
        username: "Sarah",
        password: 123,
        friends: ["max", "tom"]
    },
    {
        username: "Dan",
        password: 433
    }
]

for(let object in users){
	if(users[object].username === "Sarah"){
		console.log('My friends are' + users[object].friends);
	} else if(users[object].username === "Dan") {
		users[object].password = 7362;
		console.log(users[object].password);
	}

}


//exercise 3

let names= ["john", "sarah", 23, "Rudolf",34]

for(let name in names){
	if(typeof names[name] == 'string'){
		let firstLetter = names[name].charCodeAt(0);
		if(firstLetter > 96){
			let firstLetterCapitalized = (names[name].charAt(0)).toUpperCase();
			names[name] = names[name].replace(names[name].charAt(0), firstLetterCapitalized);
		}
	}
}

for(let name of names){
	if(typeof name != 'string'){
		continue;
	} 
	console.log(name);
}
