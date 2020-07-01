let tipBlock = document.getElementById('totalTip');
function calculateTip(){
    let form = document.forms[0];
    let billamt = form.elements.billamt.value;
    let serviceQual = form.elements.serviceQual.value;
    let numOfPeople = document.getElementById('peopleamt').value;
    if(billamt == ''){
        alert('please enter a bill amount');
        return;
    } else if(serviceQual == '0'){
        alert('please select a service quality option');
        return;
    } else if (numOfPeople == '' || numOfPeople <= 1){
        numOfPeople = 1;
        let each = document.getElementById('each');
        each.style.display = 'none';
    }
    let total = billamt * serviceQual / numOfPeople;
    total = total.toFixed(2);
    tipBlock.style.display = 'block';
    document.getElementById('tip').innerHTML = total;
}
tipBlock.style.display = "none";
let submitButton = document.getElementById('calculate');
submitButton.addEventListener('click', calculateTip);