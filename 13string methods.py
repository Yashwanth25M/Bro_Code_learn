# (01:27:03) 

# # string methods

# name = input("Enter you full name:")
# print(f"The length of your name is {len(name)}")
# print(f"The first occurence of 'Y' is at {name.find("Y")}")#if it does not find , it returns '-1'
# print(f"The last occurence of 'Y' is at {name.rfind("Y")}")
# print(f"The capitalzation of {name} is {name.capitalize()}")
# print(f"The Upper case of {name} is {name.upper()}")
# print(f"The Lower case of {name} is {name.lower()}")
# print(f"The name {name} contains digit : {name.isdigit()}")
# print(f"The name {name} contains numeric : {name.isnumeric()}")
# print(f"The name {name} contains alphabtes : {name.isalpha()}")
# print(f"The name {name} contains alphabtes and numerics : {name.isalnum()}")
# print(f"The number of occurences of 'a' in {name} is {name.count("a")}")
# print(f"Replacing 'a' in {name} with 'o' {name.replace("a" , "o")}")

# Exercise 1 : Validate user input
# 1.username is no more than 12 character
# 2.username must not contain spaces
# 3.username must nor contain digits

# username = input("Enter a username:")
# if len(username) > 12:
#     print(f"Your name {username} exceeded length defined by admin")
# elif(not username.find(" ") == -1):
#     print(f"Your name {username} contains spaces")
# elif(username.isalpha() == False):
#     print(f"Your name {username} contains numbers")
# else:
#     print(f"Welcome {username}")