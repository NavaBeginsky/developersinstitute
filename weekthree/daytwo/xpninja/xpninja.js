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


//exercise 2
/*1. Add an input of type “email” to your form.
2. Write your own javascript validation function to check if the entered value is a valid email address.
I.e contains some valid characters, and @ sign, more characters a . (dot) and some more characters.
3. On “submit” click, the validation function should run and validate the email address.*/
let newForm = document.createElement('form');
let emailInput = document.createElement('input');
emailInput.setAttribute('type', 'text');
let emailSubmitButton = document.createElement('input');
emailSubmitButton.setAttribute('type', 'submit');
emailSubmitButton.setAttribute('value', 'submit');
newForm.appendChild(emailInput);
newForm.appendChild(emailSubmitButton);
document.body.appendChild(newForm);

function validateEmail(){
    let email = emailInput.value;
    let emailArray = email.split('@');
    console.log(emailArray);
    let emailArrayPeriod = email.split('.');
    console.log(emailArrayPeriod);
    console.log(emailArray[0]);
    if(emailArray.length == 1 || emailArray[0] == '' || emailArrayPeriod.length == 1 || emailArrayPeriod[0] == '' || email.indexOf('.') == email.length - 1){ //checks if @ is not present, second condition checks that there were characters before the @. Third condition checks if . is not present, fourth condition checks that there were characters before the . fifth condition checks the the . is not the last char
        alert('please enter a valid email');
    } 
    
}

emailSubmitButton.addEventListener('click', validateEmail);


//exercise 3
let userLocation = document.getElementById("location");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    userLocation.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  userLocation.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
