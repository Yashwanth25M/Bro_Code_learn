# (08:14:57)

# exception handling:event that nterupts flow of program
# (zerodivisionError[divide by zero] ,
#  TypeError[use incorrect datatype in operation] ,
#  ValueError[use correct type but inapprpriate value] )
# 1.try , 2.except 3.finally


# Errors

# 1. ZeroDivisionError
# a = 10
# b = 0
# print("Result of division:", a / b)  
# ❌ ZeroDivisionError: division by zero

# 2. TypeError
# name = "Yashwanth"
# age = 22
# print("Full Info:", name + age)      
# ❌ TypeError: can only concatenate str (not "int") to str

# 3. ValueError
# value = int("abc")                   
# ❌ ValueError: invalid literal for int() with base 10: 'abc'

"""
try:
    try some code

except Exception:
    handeles an exception

finally:
    do some clean up    
    """

try:
    number = int(input("Enter a number: "))
    print( 1 / number )

# except ZeroDivisionError:
#     print("You cannot divide by zero")  

# except ValueError:
#     print("Enter only numbers")

except Exception as e:
    print(f"Exception ({e})error")

finally:
    print("Finally block executed")