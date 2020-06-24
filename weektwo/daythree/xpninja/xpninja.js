function divisibleByThree(string){
	let arr = string.split('');
	let total = arr.reduce(add);
	return (total % 3 == 0 ? true : false);
}

function add(total, num){
	return total + num;
}

let string = '9999933366';
divisibleByThree(string);

//exercise 2
let average = {
	calcAverage(){
		return this.grade * this.coefficient / this.grade.length;
	}
};

function getCourseInfo(){
	do {
	let course = {};
	let name = prompt('What is your name?');
	do {
		course.nameOfCourse = prompt('What is the name of the course?');
	}
	while(!course.nameOfCourse)
	do {
		course.grade = prompt('What do you think the grade you will receive is?');
	}
	while(!course.grade)
	do {
		course.coefficient = prompt('What is the coefficient of the course?');
	}
	while(!course.coefficient);

	average = course;

	} while (prompt('Would you like to add another course?') == 'yes');

	alert(name + ', your semester average is' + average.calcAverage());

}

getCourseInfo();
console.log(average);