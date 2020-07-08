def display_message():
    print("I am learning about functions in this chapter")

display_message()

#exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book('Harry Potter')

#exercise 3
def make_shirt(size = 'large', text = 'I love Python'):
    print(f'The size of the shirt is {size} and {text} will be printed on it.')

make_shirt('large', 'Kale Yeah!')
make_shirt(text = 'Bitch, Peas', size = 'small')

make_shirt()
make_shirt('medium')
make_shirt(text = 'Message 2')

#exercise 4
magician_names = ['houdini', 'david blane', 'criss angel']

def show_magicians(magicians):
    for name in magicians:
        print(name)

def make_great(magicians):
    ''' creates new array with all the names preceded by "the great" and returns it '''
    magicians_made_great = ["The Great " + name for name in magicians]
    return magicians_made_great

magician_names = make_great(magician_names)
show_magicians(magician_names)

#exercise 5
def describe_city(city_name, country = 'Israel'):
    print(f'{city_name} is in {country}')

describe_city('london', 'England')
describe_city("Rome", "Italy")
describe_city('Tel Aviv')

#exercise 6
from datetime import datetime, timedelta

def get_age(year, month, day):
    current_date = datetime.today
    birthday = day + '/' + month + '/' + year
    birthday_convert_to_date = datetime.strptime(birthday, "%d/%m/%Y")
    age = int((current_date - birthday_convert_to_date) / 365 / timedelta (days=1))
    print(age)

get_age('1993', '3', '12')




    