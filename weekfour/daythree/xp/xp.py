#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

number_dictionary = dict(zip(keys, values))

#exercise 2
store = {
    'name': 'Zara', 
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': 7000, 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green'] 
    }
}

store['number_stores'] = 2
clients = ', '.join(store['type_of_clothes'])
print(f'Zara clients include people looking for clothing and house goods including, {clients}' )