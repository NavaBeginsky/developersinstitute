
// exercise 1
let addressNumber = "5";
let addressStreet = "Amnon Vetamar";
let country = "Israel";

let global_address = addressNumber + ' ' + addressStreet + ' ' + country;
console.log(`I live in ${global_address}\n`.repeat(5));


// exercise 2
const birthYear = 1993;
let futureYear = 2050;
let possibleAge = futureYear - birthYear;
console.log(`I will be ${possibleAge} in ${futureYear}`);

// exercise 3
let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow']
console.log(pets[1]);
pets.splice(3, 1, "horse");
console.log(pets);

console.log(pets.length);