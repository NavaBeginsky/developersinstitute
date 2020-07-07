numbers = []
for i in range(3):
    numbers.append(input('Give me a number'))
print(f"The greatest number is:", max(numbers))

#exercise 2
letter = input('please enter a letter')
vowels = "aeiou"
if letter.lower() in vowels:
    print('This is a vowel')
else :
    print('this is a consonant')

#exercise 3
my_list = [1, 5, 23, 4, 23]
index_of_23 = my_list.index(23)
print(index_of_23)

#exercise 4
list_1 = [3, 6, 9] 
list_2 = [4, 5, 7]
list_1.extend(list_2)
print(list_1)

#exercise 5
list_of_everyone = []
while(True):
    personal_info = input('Please enter your name, age and score, seperated by commas. If there are no more, enter "quit"')
    if personal_info == 'quit':
        break
    else :
        personal_info_tuple = tuple(personal_info.split(', '))
        list_of_everyone.append(personal_info_tuple)
sorted_list = sorted(list_of_everyone, key=lambda tup: (tup[0], tup[1], tup[2]))
print(sorted_list)

#exercise 6
def createBill():
    customer_name = input('What is the customer name?')
    waiter = input('What is your name?')
    item_ordered = input('What did they order?')
    price_of_item = input("What is the price of the item?")
    amount_ordered = input("How many were ordered?")
    total_pre_VAT = float(price_of_item) * float(amount_ordered)
    vat = 0.17 * total_pre_VAT
    final_total = vat + total_pre_VAT

    print(f'''
     **************************
        customer: {customer_name}
        waiter/waitress: {waiter}
     **************************
     item  amount  price
     __________________________ 
     {item_ordered} * {amount_ordered}    {price_of_item}
     __________________________   
                total: {total_pre_VAT}
                tax: {vat}
                final total: {final_total}
    ****************************
     ''')
createBill()
    
#exercise 7
import random
print(random.randrange(1,10))    

#exercise 8
list_of_numbers = list(range(1, 1000001))
for number in list_of_numbers:
    print(number)

#exercise 9
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))