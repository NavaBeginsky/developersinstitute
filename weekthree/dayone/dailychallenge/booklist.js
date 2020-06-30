let allBooks = [
    {
        title: 'Harry Potter',
        author: 'JK Rowling',
        image: 'https://images-na.ssl-images-amazon.com/images/I/81gvKPsewML._AC_SL1500_.jpg',
        alreadyRead: true
    }, 
    {
        title: 'Inferno',
        author: 'Dan Brown',
        image: 'https://images-na.ssl-images-amazon.com/images/I/915mr+JhBGL.jpg',
        alreadyRead: false
    }

]

let table = document.createElement('table');
for(let index in allBooks){
    let row = document.createElement('tr');
    
    for(let i=0; i<3; i++){
        let column = document.createElement('td');
        let text;
        let image;
        if(i == 0){
            text = document.createElement('P');
            text.innerHTML = allBooks[index].title;
            if(allBooks[index].alreadyRead == true){

                text.style.color = 'red';
            }
            column.appendChild(text);
            
        } else if (i == 1){
            text = document.createElement('P');
            text.innerHTML = 'Written by:' + allBooks[index].author;
            
            if(allBooks[index].alreadyRead == true){
                text.style.color = 'red';
            }
            column.appendChild(text);
        } else {
            image = document.createElement("img");
            image.setAttribute('src', allBooks[index].image);
            image.setAttribute('width', 100);
            column.appendChild(image);
            
        }
        row.appendChild(column);
        table.appendChild(row);
    }
   
    
}
document.body.appendChild(table);


