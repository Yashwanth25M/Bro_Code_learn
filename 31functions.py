# (03:52:12) 

# functions
# Block of reusable code

# to say happy birthday 3times
# print("happy birhday")
# print("happy birhday")
# print("happy birhday")

# for performing same task 100 times its hectic

# def wish():
#     print("Happy birthday!!")
# for i in range(1,101):
#     print(f"count {i}")
#     wish()

# passing a arguments

# def wish(name):
#     print(f"Happy birthday {name}!!")
# wish("vishu")
# wish("lag")

# Passing a multiple arguements

# def display_invoice(username , amount , due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due : {due_date}")
# display_invoice('Vishu',300,"01/01/2026")
# display_invoice('Kishan',24.356789,"05/03/2026")


# Return statement
# statement used to end a function and send result to caller

# def add(a,b):
#     y = a + b
#     return y
# add(3,6)#no result because we are not printing
# print(add(3,4))

# def create_name(first , last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first+" "+ last
# full_name=create_name("bRo" , "cODE")
# print(full_name)