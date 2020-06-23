let arr = [5,0,9,1,7,4,2,6,3,8];

for(let index in arr){
	let num1 = arr[index];
	let num2 = arr[Number(index) + Number(1)];
	if(num1 < num2){
		arr[index] = num2;
		arr[Number(index) + Number(1)] = num1;
	}
	for(let index in arr){
		let num1 = arr[index];
		let num2 = arr[Number(index) + Number(1)];
		if(num1 < num2){
			arr[index] = num2;
			arr[Number(index) + Number(1)] = num1;
		}
	}
}
console.log(arr);
let arrayString = arr.toString();
console.log(arrayString);
let joinArray = arr.join("");
console.log(joinArray);