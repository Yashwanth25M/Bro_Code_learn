# (02:45:21)

# 2D collections

# fruits = ["Apple" , "Orange" , "Bannana" , "Kiwi"]
# vegetables = ["Tomato" , "Potato" , "Beans" , "Caroot"] 
# meats = ["Chicken" , "Fish" , "Red meat"]

# groceries = [fruits , vegetables , meats]

# print(groceries)
# print(groceries[0])
# print(groceries[0][0])
# print(groceries[0])
# groceries[0][0] = "Pomogranite"
# print(groceries[0])

# grocerie = [
#              ["Apple" , "Orange" , "Bannana" , "Kiwi"],
#              ["Tomato" , "Potato" , "Beans" , "Caroot"] ,
#              ["Chicken" , "Fish" , "Red meat"]
#                ]
# same as groceries
# print(grocerie)
# print(grocerie[0])
# print(grocerie[0][0])
# print(grocerie[0])
# grocerie[0][0] = "Pomogranite"
# print(grocerie[0])

# for item in grocerie:
#     for i in item:
#         print(i,end=" ")
#     print()

# Exercise 1 :2d keypad

# num_pad = (
#             ( 1 , 2 , 3 ),
#             ( 4 , 5 , 6 ),
#             ( 7 , 8 , 9 ),
#             ( "*" , 0 , "#")
# )

# for i in num_pad:
#     for j in i:
#         print(j,end=" ")
#     print()

# print("New approach\n\n\n")

# for i in range(1,4):
#     print(i,end=" ")
# print()
# for i in range(4,7):
#     print(i,end=" ")
# print()
# for i in range(7,10):
#     print(i,end=" ")
# print()
# print("* 0 #")