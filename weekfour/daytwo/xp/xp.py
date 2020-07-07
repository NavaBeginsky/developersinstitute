my_fav_numbers = set()
my_fav_numbers.update([1,27])
my_fav_numbers.remove(27)
friend_fav_number = {1, 2, 5}
our_fav_numbers = my_fav_numbers.union(friend_fav_number)
print(our_fav_numbers)

#exercise 2
my_fav_numbers = ()
my_fav_numbers_list = list(my_fav_numbers)
my_fav_numbers_list.extend([1, 27])
my_fav_numbers_list.pop()
my_fav_numbers = tuple(my_fav_numbers_list)

friend_fav_number = (1, 2, 5)
our_fav_numbers = list(friend_fav_number) + my_fav_numbers_list
our_fav_numbers = tuple(our_fav_numbers)
print(our_fav_numbers)

#exercise 3
import numpy
for num in numpy.arange(1.5, 5.5, 0.5):
    print(num)

#exercise 4
for num in range(1, 21):
    print(num)

#exercise 5
more_toppings = True
while more_toppings:
    current_topping = input('What Toppings would you like? If you are finished, enter "quit"')
    if current_topping == 'quit':
        more_toppings = False
    else :
        print(f'Ok, adding {current_topping} to your pizza.')

#exercise 6
def costOfTicket(age):
    if 12 >= int(age) >= 3:
        return 10
    elif int(age) > 12:
        return 15
    else :
        return 0

def get_total_ticket_cost_family():
    age_of_family_members = input('How old are all the members of your family? (seperated by commas)')
    list_of_ages = age_of_family_members.split(',')
    total_cost = 0
    for age in list_of_ages:
        total_cost += costOfTicket(age)
    print(f'The total ticket cost is {total_cost}')

get_total_ticket_cost_family()

def oldEnoughToSeeMovie():
    people_allowed_to_see = []
    while True:
        name = input('What is your name? (If there are no more people, type "quit")')
        if name == 'quit':
            break
        age = input('How old are you?')
        print(name)
        if 21 > int(age) > 16:
            print('You are too young to see the movie')
        else :
            print('You can see the movie')
            people_allowed_to_see.append(name)
    print(people_allowed_to_see)

oldEnoughToSeeMovie()

#exercise 7
users = ['nava', 'rafael', 'maya', 'chava', 'nonny']

for user in reversed(users):
    age = input(f'{user}, what is your age?')
    if int(age) < 16:
        users.remove(user)
    else :
        continue
    
print(users)

#exercise 8
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove('Blueberries')
basket.extend("Kiwi")
basket.insert(0, "Apples")
number_of_apples = basket.count('Apples')
basket.clear()
print(basket)

#exercise 9
def printListItems(my_list):
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 1

my_list = ['here', 'is', 'my', 'list']
printListItems(my_list)


#exercise 10
def printEvenIndexItems(my_list):
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 2

my_list = ['here', 'is', 'my', 'list']
printEvenIndexItems(my_list)