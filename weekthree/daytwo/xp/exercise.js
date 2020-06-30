//Give to all paragraphs inside the <article> tag the class of para_article.

let paragraphs = document.querySelectorAll('article p');
for (let p of paragraphs) {
    p.classList.add('para_article');
}

//Remove the last paragraph in the article.
let article = document.querySelector('article');
let numOfParagraphs = paragraphs.length;
paragraphs[numOfParagraphs - 1].remove();

//Add an event listener so that when you click on the h2, it is removed from the DOM.
let secondHeader = document.querySelector('h2');
secondHeader.addEventListener('click', remove);
function remove(e){
    e.target.remove();
}

//Set the font size of the h1 to be a random pixel size from 0 to 100.
let firstHeader = document.querySelector('h1');
let randomNumber = Math.floor(Math.random() * 100);
firstHeader.style.fontSize = randomNumber + 'px';

//Hide the 1st paragraph, when it’s clicked.
paragraphs[0].addEventListener('click', hide);
function hide(e){
    e.target.style.display = 'none';
}

//Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.
function fadeOut(e){
    e.target.style.transition = 'opacity 2s';
    e.target.style.opacity = '0';
}

paragraphs[1].addEventListener('click', fadeOut);

//Get the values from the inputs and append them to the end of the html, inside a table.
let inputs = document.querySelectorAll('input');
let table = document.createElement('table');
document.body.appendChild(table);
function createTableContent(input){
    let row = document.createElement('tr');
    let column = document.createElement('td');
    column.innerHTML = input.value;
    row.appendChild(column);
    table.appendChild(row);
}

inputs[0].onchange = function(){createTableContent(inputs[0])};
inputs[1].onchange = function(){createTableContent(inputs[1])};


//Create a function called : getBold_items() that takes no parameter. This function has to collect all the bold items inside the paragraph.
function getBoldItems(){
    return document.getElementsByTagName('strong');
}

function highlight(items){
    for(let item of items){
        item.style.color = 'blue';
    }
}

function return_normal(items){
    for(let item of items){
        item.style.color = 'black';
    }
}

let boldParagraph = document.body.children[5];
boldParagraph.onmouseover = function(){highlight(getBoldItems())};
boldParagraph.onmouseout = function(){return_normal(getBoldItems())};