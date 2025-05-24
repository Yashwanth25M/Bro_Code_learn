# (01:46:35)

# format specifiers = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# (number) = allocate that many spacess
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print("display only 2 number after decimal")
print(f"price 1 is ${price1:.2f}")#display only 2 number after decimal
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")

print("To allocate empty spaces")
print(f"price 1 is ${price1:10}")#now this line in total using 10 spaces
print(f"price 2 is ${price2:15}")
print(f"price 3 is ${price3:20}")

print("Preceeding with zero")
print(f"price 1 is ${price1:010}")
print(f"price 2 is ${price2:015}")
print(f"price 3 is ${price3:020}")

print("Left justifier")
print(f"price 1 is ${price1:<10}")
print(f"price 2 is ${price2:<20}")
print(f"price 3 is ${price3:<20}")

print("right justifier")
print(f"price 1 is ${price1:>10}")
print(f"price 2 is ${price2:>15}")
print(f"price 3 is ${price3:>20}")

print("center justifier")
print(f"price 1 is ${price1:^10}")
print(f"price 2 is ${price2:^15}")
print(f"price 3 is ${price3:^20}")