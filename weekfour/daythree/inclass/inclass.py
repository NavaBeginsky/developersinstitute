countries = [{
        'name': 'Israel', 
        'capital': 'Jerusalem', 
        'continent': 'Asia'
    }, 
    {
        'name': 'England', 
        'capital': 'London', 
        'continent': 'Europe'
    }, 
    { 
        'name': 'Brazil', 
        'capital': 'Brazilia', 
        'continent': 'South America'
        }, 
    {
        'name': 'USA', 
        'capital': 'Washington DC', 
        'continent': 'North America'
    }, 
    {
        'name': 'Thailand', 
        'capital': 'Bangkok', 
        'continent': 'Asia'
    }]


names = ["jon", "tom", "jack"]
firstLetter = [name[0].upper() for name in names]
name_dict = dict(zip(firstLetter, names))
print(name_dict)