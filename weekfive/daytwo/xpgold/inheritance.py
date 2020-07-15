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
    num_clients = 0

class BankAccount(Bank):
    def __init__(self, owner, balance):
        if self.num_clients < 10:
            self.owner = owner
            self.balance = int(balance)
            self.num_clients += 1
        else :
            print('The bank is already at max capacity.')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('deposit successful')
            print(self.balance)
        else :
            print('That is not a valid deposit amount')
            print(self.balance)
    
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
        user_cc = int(input('What is your credit card number?'))
        user_pw = input('What is your password?')
        while user_cc != self.cc_num :
            user_cc = int(input('That was not correct, what is your credit card number?')) 
        if user_pw != self.password:
            user_pw = input('Incorrect password, what is your password?')
            if user_pw != self.password:
                print("Wrong password, the card has been eaten by the machine")
                del self.cc_num
                return
        deposit_or_withdraw = input('Would you like to make a "deposit" or "withraw"?')
        self.deposit() if deposit_or_withdraw == 'deposit' else self.withdraw()

    def deposit(self):
        bills = {
            20: 0,
            50: 0,
            100: 0, 
            }
        while True:    
            bill = int(input("The machine only accepts bills in the amount of 20, 50 and 100. Which bill would you like to deposit"))
            quantity = int(input(f'How many {bill} would you like to deposit?'))
            if bill == 20 or bill == 50 or bill == 100 and quantity > 0:
                bills[bill] += quantity
                print('successfully deposited', bill * quantity, 'dollars')
                more_bills = input('Would you like to deposit more bills?')
                if more_bills == 'no':
                    amount = calculate_total(bills)
                    super().deposit(amount)
                    break


    def withdraw(self):
        bills = {
            20: 0,
            50: 0,
            100: 0
        }
        while True:
            bill = int(input("The machine only gives 20s and 50s. Which bill would you like to withdraw?"))
            quantity = int(input('How many would you like?'))
            if bill == 20 or bill == 50 and quantity > 0:
                bills[bill] += quantity
                more_bills = input('Would you like to withdraw more bills?')
                if more_bills == 'no':
                    amount = calculate_total(bills)
                    super().withdraw(amount)
                    break
            else :
                print('please choose a valid bill')

def calculate_total(bills_dict):
    return bills_dict[20] * 20 + bills_dict[50] * 50 + bills_dict[100] * 100

nava = Owner('nava', '50', 34, 'blah')
nava.check_owner_info()
