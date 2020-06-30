let sectionElement = document.getElementById('section');
let divElement = document.getElementById('div');
let btnElement = document.getElementById('btn');

function changeBackground(e){
    e.target.classList.add('aqua');
    e.target.style.color = 'red';
}

function changeTextColor(e){
    e.target.style.color = 'yellow';
}

function moveRight(e){
    e.target.style.position = 'relative';
    e.target.style.left = '40px';
}

function disappear(e){
    e.target.style.display = 'none';
}

function reappear(){
    btnElement.style.display = 'block';
}

sectionElement.addEventListener('mouseover', changeBackground);
divElement.addEventListener('click', moveRight);
btnElement.addEventListener('click', changeTextColor);
btnElement.addEventListener('mouseout', disappear);
divElement.addEventListener('mouseover', reappear);

