let age = prompt("How Old Are You?");

if (age < 18) {
	alert("Sorry, you are too young to drive this car. Powering off");
} else if(age == 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!");
} else if (age > 18) {
	alert("Powering On. Enjoy the ride!");
} else {
	alert("Please enter a valid age");
}


//exercise 2 Write as comments the steps of the resolution of this piece of code
let a = 2 + 2;

switch (a) { //checking value of a against upcoming values
  case 3: //if a ==3, display alert
    alert( 'Too small' );
    break;
  case 4: // if a ==4, display the following alert  This is the correct answer
    alert( 'Exactly!' );
    break;
  case 5: // if a == 5 display the following alert 
    alert( 'Too large' );
    break;
  default: //if a was none of the previous values, display the following alert
    alert( "I don't know such values" );
}


//exercise 3 Write as comments the steps of the resolution of this piece of code

let a = 2 + 2;

switch (a) {//checking value of a against upcoming values
  case 4: //if a == 4, display the following alert
    alert('Right!');
    break;

  case 3: // (*) grouped two cases, if a==3 or a==5 it will display the two following alerts
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default: //if it was none of the previous values, it will display the following alert.
    alert('The result is strange. Really.');
}

//improptu challenge posed by Lise

/* 1. get the numberPets
2. get the 2nd type of pet
3; What is the favorite food of the cat
​*/
let users = [
    {
        username: "Sarah",
        password: 123,
        friends: ["max", "tom"],
        pets : {
            numberPets : 2,
            typePets : ["dog", "cat"],
            favoriteFood : {
                dog : "candy",
                cat : "milk"
            }
        }
    }
]

users[0]['pets']['numberPets'];
users[0]['pets']['typePets'][1];
users[0]['pets']['favoriteFood']['cat'];