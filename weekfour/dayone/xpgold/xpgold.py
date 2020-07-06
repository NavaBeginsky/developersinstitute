#exercise 3
print('Helloworld\n' * 4 + "I love python\n" * 4)

#exercise 4
def calculate_for_x(x):
    total = 0
    for num in range(1, 5):
        total = total + (int(x * num))
    print(total)

x = input('Give me a number')
calculate_for_x(x)

