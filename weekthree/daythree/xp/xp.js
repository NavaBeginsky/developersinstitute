function myMove(){
    let box = document.getElementById('animate');
    let currentPostition = 0;
    let int = setInterval(() => {
        if(currentPostition < 350){
            currentPostition++;
            box.style.left = currentPostition + 'px';
        } else {
            clearInterval(int);
        }
    }, 50);
}

function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("redbox", ev.target.id);
  }
  
  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("redbox");
    ev.target.appendChild(document.getElementById(data));
  }