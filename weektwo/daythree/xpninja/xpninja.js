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


function calcAverage(grade, coefficient, numOfGrades=1){
		return grade * coefficient / numOfGrades;
	}


function getCourseInfo(){
	let coursecount = 0;
	let course = {};
	let coursename;
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

		if(!average[course.courseName]){// if the course name is not already added to average
			average[coursename] = course; // add our local object to the global average object
			coursecount += 1; //increment course count
		} else { //if the course is already in the average variable, we just need to adjust the grade
			average.courseName.grade = course.grade ;
		}

	} while (prompt('Would you like to add another course?') == 'yes');

	alert(name + ', your semester average is' + calcAverage(course.grade, course.coefficient, average.grade.length));

}


getCourseInfo();
console.log(average);