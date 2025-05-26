# # (03:11:33)

# # concession stand program

# menu = {
#         "pizza" : 3.00 , 
#         "nachos" : 4.50,
#         "popcorn" : 6.00 , 
#         "fries" : 2.50 , 
#         "chips" : 1.00 , 
#         "pretzel" : 3.50 , 
#         "soda" : 3.00 , 
#         "lemonade" : 4.25
#         }

# cart = []
# Total = 0
# print("------Menu-------")
# print("Item       : Cost($)")
# print("==================")
# for key , value in menu.items():
#     print(f"{key:10} : ${value}")
# print("==================")

# while True:
#     food = input("Select an item(enter esc to escape): ").lower()
#     if food == "esc":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     print(f"{food} : ${menu[food]}")
#     temp = menu[food]
#     Total += temp 
# print("==================")

# print("Total cost is $",Total)