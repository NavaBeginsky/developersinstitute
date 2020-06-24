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
	
};


function getCourseInfo(){
	let coursecount = 0;
	let course = {};
	let coursename;
	let gradeXCoefficient = [];
	let name = prompt('What is your name?');

	do {

		do {
			course.nameOfCourse = prompt('What is the name of the course?');
			coursename = course.nameOfCourse; //store the name of the course in a seperate variable to use as the object we push to average
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

		average[coursename] = course; // add our local object to the global average object
		coursecount += 1; //increment course count
	
		gradeXCoefficient.push(course.grade * course.coefficient);

	} while (prompt('Would you like to add another course?') == 'yes');

	let average = gradeXCoefficient.reduce() / coursecount;
	console.log(average);
	alert(name + ', your semester average is' );

}

function add(total, current){
	return total + current
}


getCourseInfo();
