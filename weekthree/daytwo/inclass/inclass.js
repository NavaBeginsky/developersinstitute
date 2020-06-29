let shoppingList = ['banana', 'apple', 'orange'];

function shopping(list, currency, amountOfMoney){
    let item;
    for(item of list){
        console.log(item);
    }
    console.log(amountOfMoney * 3 + currency);
}

shopping(shoppingList, '$', 10);