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
competitors = ', '.join(store['international_competitors'])
print(f'Zara clients are similar to the clients who shop at {competitors}' )
store['country_creation'] = 'Spain'
if store['international_competitors'] :
    store['international_competitors'].append('Desigual')
del store['creation_date']
print(store['international_competitors'][-1])
major_colors = ' and '.join(store['major_color']['US'])
print(f'The major clothes colors in the US are {major_colors}')
print(len(store))
print(store.keys())

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

store.update(more_on_zara)
print(store['number_stores'])

#Just a note that the bonus instructions are not clear at all, happy to do it if someone will clarify

#exercise 3
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
current_index = 0
disney_users1 = {name: index for index, name in enumerate(users)}
print(disney_users1)

index2 = 0
disney_users2 = {index: name for index, name in enumerate(users)}
print(disney_users2)

disney_users3 = {i: disney_users1[i] for i in sorted(disney_users1)}

disney_users4 = {}
for name in users :
    if 'i' in name or name[0] == 'M' or name[0] == 'P':
        disney_users4[name] = current_index
        current_index += 1
  