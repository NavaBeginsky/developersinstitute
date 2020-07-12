class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, num_of_animal = 1):
        if animal_type in self.animals.keys():
            self.animals[animal_type] += num_of_animal
        else :
            self.animals[animal_type] = num_of_animal  

    def get_info(self):
        return self.name, self.animals.items()

    def get_animal_types(self):
        return sorted([animal for animal in self.animals.keys()])

    def get_short_info(self):
        animals = ', '.join(self.get_animal_types())
        return f"Mcdonald's farm has {animals}"
        
mcdonalds = Farm('MacDonald\'s farm')
mcdonalds.add_animal('cow', 5)
mcdonalds.add_animal('sheep')
mcdonalds.add_animal('sheep')
mcdonalds.add_animal('goat', 12)

farm_name, mcdonalds_animals = mcdonalds.get_info()
print(farm_name)
for animal in mcdonalds_animals:
    print(f'{animal[0]}      : {animal[1]}')
    
print(mcdonalds.get_short_info())
