# exercise 1
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


fluffy = Cat('Fluffy', 5)
princess = Cat('Princess', 2)
garfeild = Cat('Garfield', 10)


def oldest_cat(*args):
    return max(args)


oldest_cat_age = oldest_cat(fluffy.age, princess.age, garfeild.age)
print(f'The oldest cat is {oldest_cat_age} years old')

# exercise 2


class Dog:
    def __init__(self, nameDog, heightDog):
        self.name = nameDog
        self.height = heightDog

    def talk(self):
        print('woof')

    def jump(self):
        print(self.height * 2)


Davids_dog = Dog('Rex', 50)
print(Davids_dog.name)
print(Davids_dog.height)

Sarahs_dog = Dog('Teacup', 20)
print(Sarahs_dog.name)
print(Sarahs_dog.height)


def biggest_dog(*args):
    biggest_dog = None
    for dog in args:
        if biggest_dog == None or biggest_dog.height < dog.height:
            biggest_dog = dog
    biggest_dog.winner = True


biggest_dog(Sarahs_dog, Davids_dog)


# exercise 3
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric_line in self.lyrics:
            print(lyric_line)


happy_bday = Songs(["Have a sunshine on you,",
                    "Happy Birthday to you !"])
happy_bday.sing_me_a_song()

# exercise 4


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animals(self, animal_sold):
        print(f'Bye, {animal_sold}')
        self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        print(self.animals)
        first_letter_of_animals = set(animal[0] for animal in self.animals)
        animal_pens = {}
        animals_index = 0
        for i in range(1, len(first_letter_of_animals) + 1):
            animal_pens[i] = []
            animal_pens[i].append(self.animals[animals_index])
            '''if we are not already on the last animal in the list (otherwise I get out of range error) and if the next animal has the same first letter 
            as the last one, then add it to the current pen and increase the animals index'''
            while animals_index != len(self.animals) - 1 and self.animals[animals_index][0] == self.animals[animals_index + 1][0]:
                animals_index += 1
                animal_pens[i].append(self.animals[animals_index])

            animals_index += 1

        self.animal_pens = animal_pens

    def get_pen(self):
        for pen in self.animal_pens.items():
            print(pen)


ramatGanSafari = Zoo('Ramat Gan Safari')
ramatGanSafari.add_animal('monkey')
ramatGanSafari.add_animal('giraffe')
ramatGanSafari.add_animal('elephant')
ramatGanSafari.add_animal('lion')
ramatGanSafari.add_animal('gorillas')
ramatGanSafari.add_animal('koala')
ramatGanSafari.get_animals()
ramatGanSafari.sell_animals('lion')
ramatGanSafari.sort_animals()
ramatGanSafari.get_pen()
