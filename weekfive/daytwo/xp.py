class Family():
    def __init__(self, last_name, members):
        '''**members should be a list containing dictionaries that contain name, age, gender and is_child'''
        self.members = members
        self.last_name = last_name

    def born(self, **new_member_info):
        '''**member info should contain name and gender'''
        new_member_info['age'] = 0
        new_member_info['is_child'] = True
        self.members.append(new_member_info)
        print("Congratulations on the new baby!")

    def is_18(self, member_name):
        for person in self.members:
            if person['name'] == member_name:
                return person['age'] >= 18

    def __repr__(self):
        return self.members

    def get_family(self):
        print(self.members)
        print(repr(self.members))


beginsky = Family('Beginsky', [{'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}])
beginsky.born(name='Maya', gender = 'Female')
print(beginsky.is_18('Michael'))
beginsky.__repr__()


class TheIncredibles(Family):
    '''**members info to be passed to super class should be a list containing dictionaries that contain
     name, age, gender, is_child, power, and incredible_name'''
    def use_power(self, name):
        for person in self.members:
            if person['name'] == name:
                if person['age'] >= 18:
                    print(person['power'])
                else:
                    raise Exception('You have no power here!')
    
    def incredible_presentation(self):
        for person in self.members:
            print(f"{person['name']} your incredible name is {person['incredible_name']} and your incredible power is {person['power']}")
           

incredibles = TheIncredibles('Parr', [
    {'name': 'Bob', 'age': 40, 'gender': 'Male', 'is_child': False, 'power': 'super stregnth', 'incredible_name': 'Mr. Incredible'}, 
    {'name': 'Helen', 'age': 36, 'gender': 'Female', 'is_child': False, 'power': 'mutating body', 'incredible_name': 'Elastigirl'}, 
    {'name': 'Violet', 'age': 15, 'gender': 'Female', 'is_child': True, 'power': 'invisibility and force fields', 'incredible_name': 'Invisigirl'}, 
    {'name': 'Dash', 'age': 10, 'gender': 'Male', 'is_child': True, 'power': 'super speed', 'incredible_name': 'speedy'} 
    ])

incredibles.incredible_presentation()

incredibles.born(name = 'Baby Jack', gender = 'Male', power = 'Unknown', incredible_name = 'SuperJack')
incredibles.incredible_presentation()