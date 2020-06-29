function createCalendar(year, month){
    let totalDays = new Date(year, month, 00).getDate();
    month = month - 1;
    let dayOfWeek = new Date(year, month).getDay();
    let table = document.createElement('table');
    let i = 0;
    let dayCount = 1;
    while(i < 7){
        let week = document.createElement('tr');
        let x = 0;
        if(i==0){
            while(x < 7){
                let days = document.createElement('th');
                let weekDays;
                switch (x){
                    case 0:
                        weekDays = document.createTextNode('SU');
                        break;
                    case 1:
                        weekDays = document.createTextNode('MO');
                        break;
                    case 2:
                        weekDays = document.createTextNode('TU');
                        break;
                    case 3:
                        weekDays = document.createTextNode('WE');
                        break;
                    case 4:
                        weekDays = document.createTextNode('TH');
                        break;
                    case 5:
                        weekDays = document.createTextNode('FR');
                        break;
                    case 6:
                        weekDays = document.createTextNode('SA');
                        break;
                    default:
                        break;

                }
                days.appendChild(weekDays);
                week.appendChild(days);
                x++
            }
        } else {
            while(x < 7){
                let days = document.createElement('td');
                if(i==1 && x == dayOfWeek){
                    let dayNum = document.createTextNode(dayCount);
                    days.appendChild(dayNum);
                    dayCount ++
                } else if(dayCount > 1 && dayCount <= totalDays) {
                    let dayNum = document.createTextNode(dayCount);
                    days.appendChild(dayNum);
                    
                    dayCount ++

                }
                
                week.appendChild(days);
                x++
            }
        }
        table.appendChild(week);
        i++
    }
    let body = document.querySelector('body');
    body.appendChild(table);
}
