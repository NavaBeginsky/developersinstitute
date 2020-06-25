let calculatorNumber = [];
let operator = [];
let onScreen = [];

function calculatorInput(input){
    if(input == '='){
        onScreen.length = 0;
        calculatorNumber.push('&');
        calculate(calculatorNumber, operator);
        operator.length = 0;
        return;
    } else if (typeof input == 'string' && input != '.') {
        onScreen.length = 0;
        operator.push(input);
        calculatorNumber.push('&');
        document.getElementById('total').innerHTML = input;
    }  else {
        if(calculatorNumber.length == 1 && calculatorNumber[0] == total && operator.length == 0){
            reset();
        }
        calculatorNumber.push(input);
        onScreen.push(input);
        document.getElementById('total').innerHTML = onScreen.join('');
    }

}

let total;

function calculate(calculatorInput, operator){
    let endOfNumber = calculatorInput.indexOf('&'); //get index of where number ends
    let number = Number(calculatorInput.slice(0, endOfNumber).join('')); //store first number
    total = number; //set total equal to the first number
    let currentNumber;
    let operatorUse;

    for(let i = 0; i < operator.length; i++){
        calculatorInput = calculatorInput.slice(endOfNumber + 1); //reset calculator input variable to the current remaining string
        endOfNumber = calculatorInput.indexOf('&');//find index of where number ends
        currentNumber = Number(calculatorInput.slice(0, endOfNumber).join(''));//turn the array into a number
        operatorUse = operator[i];
        total = doMath[operatorUse](total, currentNumber);//do the math to get current total
    }
    
    document.getElementById('total').innerHTML = total;
    calculatorNumber = [total];


}

function reset(){
    calculatorNumber = [];
    operator = [];
    document.getElementById('total').innerHTML = '';
}

const doMath = {
    '+' : function(x, y) {return x + y},
    '-' : function(x, y) {return x - y},
    '*' : function(x, y) {return x * y},
    '/' : function(x, y) {return x / y}
}

