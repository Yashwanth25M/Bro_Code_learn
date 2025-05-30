# (04:45:56)

# list comprehensions
# Concise way to create  a list
# [expression for value in iterable if condition]

# Traditionall method
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2) 
# print(doubles)

# List comprahension
# doubles = [ x*2 for x in range(1,11)]
# print(doubles)

# Capitalizing every item
# fruits = [ "apple" , "orange" , "bannana" ]
# print(fruits)
# fruits = [ fruit.capitalize() for fruit in fruits]
# print(fruits)

# seperating  positive and negative numbers
# numbers = [ 1 ,-2 , 3 , -4 , 5 , -6]
# pos_num= [num for num in numbers if num > 0]
# neg_num= [num for num in numbers if num < 0]
# print(pos_num)
# print(neg_num)

# seprating even and odd numbers
# numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
# even_num = [num for num in numbers if num % 2 == 0]
# print(even_num)
# odd_num = [num for num in numbers if num % 2 != 0]
# print(odd_num)


# grades = [85 , 42 , 79 , 90 , 56 , 61 , 30]
# pass_grades = [grade for grade in grades if grade >= 60]
# print(pass_grades)

# # integraing if-else statement
# numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
# nde = ["even" if n % 2 == 0  else "odd" for n in numbers]
# print(nde)