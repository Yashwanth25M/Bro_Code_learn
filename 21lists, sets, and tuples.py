# (02:23:03)

# lists, sets, and tuples

# List = [] Ordered and changeable . Duplicates OK
# Set = {} unordered and immutable . but add/remove OK . NO duplicates
# tuple = () Ordered and unchangeable . Duplicate OK . FASTER

# fruits = ["Apple" , "Orange" , "Bannana"]
# print(fruits)#accessing an list
# print(fruits[0])#Accessing a particular element
# print(fruits[1])
# print(fruits[2])

# for fruit in fruits:
#     print(f"I like {fruit}")

# List methods

# print(len(fruits))
# print("Bannana" in fruits)#returns true 
# fruits[1] = "oreo"
# print(fruits)
# fruits.append("Orange")
# print(fruits)
# fruits.remove("Orange")
# print(fruits)
# fruits.insert(2,"Kiwi")
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# print(fruits.index("Kiwi"))
# print(fruits.count("Bannana"))
# fruits.clear()
# print(fruits)

# Set

# fruits = {"Apple" , "Orange" , "Bannana" , "Bannana"}
# print(type(fruits))
# print(f"Unordered:{fruits}")
# print(len(fruits))
# print("Bannana" in fruits)
# print(fruits)
# # print(fruits[0])#Throws an error a immutable
# fruits.add("Oreo")
# print(fruits)
# fruits.remove("Oreo")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.clear()
# print(fruits)

# Tuples

# fruits = ("Apple" , "Orange" , "Bannana" , "Bannana")
# print(type(fruits))
# print(len(fruits))
# print("Bannana" in fruits)
# print(fruits.index("Apple"))
# print(fruits.count("bannana"))

# for fruit in fruits:
#     print(fruit)