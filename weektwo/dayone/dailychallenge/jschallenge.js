var array = ["Banana", "Apples", "Oranges", "Blueberries"];

// remove banana
array.splice(0, 1);

// sort the array in order
array.sort();

//add kiwi to the end
array.push('Kiwi');

//remove apples
array.splice(0, 1);

//reverse order
array.reverse();


//var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]; access oranges

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
array2[1][1][0];