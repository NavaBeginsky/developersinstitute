def even_numbers(my_list):
    evens = [num for num in my_list if num % 2 == 0]
    return evens

my_numbers = [2, 3, 4, 6, 7]

print(even_numbers(my_numbers))