# (04:15:40)

# *args & **kwargs

# *args(arguements) :allows to passs multiple non-key arguements
# **kwargs(key-word arguements):allows to passs multiple key arguements

# def add(a,b):
#     return a+b
# print(add(1,2))
##print(add(1,2,3))#Throws an error as funcion cable of only 2 arguements

# def add(*args):
#     print(type(args))
# add(1,2,3,4)

# Addition by passing n number of arguements
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(total)
# add(1,2,3,4)

# Multiplication by passing n number of arguements
# def mul(*args):
#     total = 1
#     for arg in args:
#         total *= arg
#     print(total)
# mul(1,2,3,4)

# def display_name(*args):
#     for arg in args:
#         arg.capitalize()
#         print(f"Heloo {arg}")
# display_name("varun", "anup" , "varun" , "karan")

# **kwargs

# def print_address(**kwargs):
#     print(type(kwargs))
# print_address(street ="fake street" , city ="Fake city" ,state ="fake state" ,zip =123456 )

# def print_address(**kwargs):
#     for key , value in kwargs.items():
#         print(key , ":",value)
# print_address(street ="fake street", apt = 1000 , city ="Fake city" ,state ="fake state" ,zip =123456 )

# # /Program to print shipping label
# def shipping_label(*args , **kwargs):
#     for arg in args:
#         print(arg,end = " ")
#     print("")
#     print(f"{kwargs.get('street')} {kwargs.get('apt')} {kwargs.get('zip')}")
# shipping_label("Dr.","spongebob", "squarepants" , "!!!" ,
#                 street = 1234 ,
#                 apt = 234 , 
#                 city = "a",
#                state = "b" ,
#                  zip = 9876544)