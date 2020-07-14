class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Bengal('fluffy', 5), Chartreux('princess', 2), Persian('cat', 7)]
my_pets = Pets(my_cats)
my_pets.walk()

#exercise 2
class Bank():
    def __init__(self):
        self.num_clients = 0

class BankAccount(Bank):
    def __init__(self, owner, balance):
        if self.num_clients < 10:
            self.owner = owner
            self.balance = balance
            self.num_clients += 1
        else :
            print('The bank is already at max capacity.')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('deposit successful')
        else :
            print('That is not a valid deposit amount')
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print('withdrew successfully')
        elif amount > self.balance:
            print('You don\'t have enough money in your account')
        else :
            print('Please enter a valid amount to withdraw')

    class Owner(BankAccount):
        def __init__(self, owner, balance, cc_num, password):
            super().__init__(owner, balance)
            self.cc_num = cc_num
            self.password = password
        
        def check_owner_info(self):
            user_cc = input('What is your credit card number?')
            user_pw = input('What is your password?')
            while user_cc != self.cc_num :
                user_cc = input('That was not correct, what is your credit card number?') 
            if user_pw != self.password:
                user_pw = input('What is your password?')
                if user_pw != self.password:
                    print("Wrong password, the card has been eaten by the machine")
                    del self.cc_num
                else:
                    deposit_or_withdraw = input('Would you like to make a "deposit" or "withraw"?')
                    self.deposit() if deposit_or_withdraw == 'deposit' else self.withdraw()


