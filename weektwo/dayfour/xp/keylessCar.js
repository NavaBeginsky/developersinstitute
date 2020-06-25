
function checkDriverAge(age){
	if (Number(age) < 18) {
	    console.log("Sorry, you are too yound to drive this car. Powering off");
	} else if (Number(age) > 18) {
	    console.log("Powering On. Enjoy the ride!");
	} else if (Number(age) === 18) {
	    console.log("Congratulations on your first year of driving. Enjoy the ride!");
	}
}

//exercise 2
amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(){
	let wantItem = prompt('What would you like to buy?');
	if(amazonBasket[wantItem]){
		console.log('Your item is already in the basket')
	} else {
		console.log('Your item is not in the basket');
	}
}

//exercise 3
function changeEnough(change, total){
	let totalChange = (change[0]*0.25) + (change[1] * 0.10) + (change[2] * 0.5) +(change[3] * 0.01);
	return totalChange >= total;
}

changeEnough([2, 0, 5, 7], 10);

//exercise 4
let shoppingList = ["banana", "orange", "apple"];

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

function adjustStock(item){
	stock[item] -= 1;
}

function myBill(shoppingList){
	let total = 0;
	for(let item of shoppingList){
		if(stock[item] > 0){
			total += prices[item];
			adjustStock(item);
		}
	}
	return total;
}

console.log(myBill(shoppingList));

//exercise 5
function hotel_cost(numNights){
	return 140 * numNights;
}

function plane_ride_cost(){
	let destination;
	do {
		destination = prompt('What is your destination?');
	} while (destination == "" || null || undefined);

	switch(destination){
		case "London":
			return 183;
			break;
		case "Paris":
			return 220;
			break;
		default :
			return 300;
			break;
	}
}

function rental_car_cost(numDays){
	if(numDays > 10){
		return (40 * numDays) * 0.95;
	} else {
		return 40 * numDays;
	}
}

function total_vacation_cost(numNights, numDays){
	return hotel_cost(numNights) + plane_ride_cost() + rental_car_cost(numDays);
}

let totalCost = total_vacation_cost(3,4);