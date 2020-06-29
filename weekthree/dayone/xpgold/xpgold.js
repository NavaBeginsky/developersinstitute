
// Change the background color of the div to lightblue and increase its padding
let myDiv = document.getElementsByTagName('div');
myDiv = myDiv[0];

myDiv.style.backgroundColor = 'lightblue';
myDiv.style.padding = '2em';

//Don’t display the first name (John) and give a border to the second name (Pete)
let names = document.getElementsByTagName('li');
let john = names[0];
let pete = names[1];

john.style.display = 'none';
pete.style.border = '2px solid red';

//Change the font size of the whole HTML
document.body.style.fontSize = '30px';

//Check if the background color of the div is lightblue, if yes alert “Hello x and y” (x and y are the users : John and Pete)
if(myDiv.style.backgroundColor == 'lightblue'){
    alert('Hello ' + john.textContent + ' and ' + pete.textContent);
}

