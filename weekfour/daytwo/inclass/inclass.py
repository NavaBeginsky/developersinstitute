list1 = [5, 10, 15, 20, 25, 50, 20]
index_of_20 = list1.index(20)
if  index_of_20 > -1:
    list1[index_of_20] = 200
print(list1)


#unpack
aTuple = (10, 20, 30, 40)
one, two, three, four = aTuple

#multiplication table
n = int(input('give me a number'))
multiplication_table = []
for num in range(1,11):
    multiplication_table.append(num * n)

print(multiplication_table)
    