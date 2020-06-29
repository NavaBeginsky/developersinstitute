//exercise 1
/*Use the setAttribute method to change the value of the identity attribute (id) from navBar to socialNetworkNavigation.
Create a new element of type li. Create a new text node with the contents “Logout.” Append the text node to the newly created list node. Finally, append this updated list node to the unordered list using the appendChild method.
Bonus:
Use the firstChild and the lastChild properties to get hold of the first and last li elements under the parent ul node. Display the contents between the anchor tags for both the children (Hint: nodeValue property).*/

// let navbar = document.getElementById('navBar');
// navbar.setAttribute('id', 'socialNetworkNavigation');

// let newLi = document.createElement('LI');
// let liText = document.createTextNode('Logout');
// newLi.appendChild(liText);
// let list = document.querySelector('ul');
// list.appendChild(newLi);

// console.log(list.firstElementChild.childNodes[0].childNodes[0].nodeValue);
// console.log(list.lastElementChild.childNodes[0].nodeValue);


/*exercise 2 - you have to comment out html from exercise 1 for exercise two to work, 
I wasn't sure if I should do it as an isolated exercise or adapt them all to work together*/
let peteLocation = document.querySelector("ul li:last-child");
peteLocation.innerHTML = "Richard";

let firstName = document.querySelectorAll("ul li:first-child");
for(let name of firstName){
    name.innerHTML = 'Nava';
}

let lists = document.getElementsByTagName('ul');
let list;
for(list of lists){
    let newLi = document.createElement('li');
    let newLiContent = document.createTextNode('Hey Students!');
    newLi.appendChild(newLiContent);
    list.appendChild(newLi);
}

let sarah = document.querySelector('ul:last-of-type li:nth-of-type(2)');
let secondList = document.querySelector('ul:last-of-type');
secondList.removeChild(sarah);

for(list of lists){
    list.classList.add('studentList');
}
lists[0].classList.add('university', 'attendance');

//exercise 3
