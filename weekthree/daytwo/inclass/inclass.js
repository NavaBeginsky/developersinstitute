let shoppingList = ['banana', 'apple', 'orange'];

function shopping(list, currency, amountOfMoney){
    let item;
    for(item of list){
        console.log(item);
    }
    console.log(amountOfMoney * 3 + currency);
}

shopping(shoppingList, '$', 10);


function insert_Row(){
    let row = document.createElement('tr');
    let table = document.getElementById('sampleTable').children[0];
    let i = 0;
    while(i < 2){
        let column = document.createElement('td');
        column.innerHTML = `column ${i}`;
        row.appendChild(column);
        i++
    }
    table.appendChild(row);
}

let button = document.getElementById('jsstyle');
button.addEventListener('click', changeColor);
button.addEventListener('mouseover', changeText);
function changeColor(e){
    e.target.style.backgroundColor = 'blue'
}
function changeText(e){
    e.target.innerHTML = 'hover';
}