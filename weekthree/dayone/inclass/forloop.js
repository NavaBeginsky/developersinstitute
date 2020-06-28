let numbers = [10, 20, 30]
// --> Use 3 differents for loops to add 5 to each number
// --> console.log the Array
// --> the result is :  [15, 25, 35]
let lengthOfArray  = numbers.length;
for(let i = 0; i < lengthOfArray; i++){
    numbers[i] = numbers[i] + 5;
}
console.log(numbers);

for(let i in numbers){
    numbers[i] = numbers[i] + 5;
}
console.log(numbers);

for(let num of numbers){
    let index = numbers.indexOf(num);
    numbers[index] = num + 5;
}
console.log(numbers);

//exercise 2

let details = {
    phoneNumber: "03574847382",
    address: "menachem begin",
    level: 2,
    rooms: ["bathroom", 'livingroom'],
    married: true
}
// --> Use a for loop to display the name of the rooms

for(let room of details.rooms){
    console.log(room);
}


//Dom exercises
<html>
<body>
  <div id="users">Users:</div>
  <ul id="list">
    <li>John</li>
    <li id="pete">Pete</li>
  </ul>
</body>
</html>

// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?

// 2. The ul DOM node?

// 3. The second li (with Pete)?

document.html.body.firstElementChild
document.html.body.children[0]

document.html.body.lastElementChild
document.html.body.children[1];

document.html.body.ul.lastElementChild;
document.html.body.ul.children[1];

<html>
<body>
  <div id="container">Users:</div>
  <ul class="list">
    <li>John</li>
    <li>Pete</li>
  </ul>
  <ul class="list">
    <li>Sarah</li>
    <li>Dan</li>
  </ul>
</body>
</html>

// For each of the questions, find 2 PROPERTIES to access :

// 1. The div node

// 2. The ul nodes, and render all of it's children one by one

// 3. The first li of each ul

document.getElementById('container');
document.querySelector('#container');

let lists = document.getElementsByTagName('ul');
let lists = document.getElementsByClassName('list');
for(let list in lists){
    for(let i=0; i < lists[list].childElementCount; i++){
        console.log(lists[list].children[i]);

    }
}

let lists = document.getElementsByTagName('ul');
for(let list of lists){ 
    console.log(list.firstElementChild);
}

let lists = document.getElementsByClassName('list');
for(let list of lists){ 
    console.log(list.children[0]);
}