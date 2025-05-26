# (02:23:03)

# shopping cart program

Foods = []#normal food
prices = []#Total price 
Quantity = []
Price = []#price of each item

while True:
    food = input("Enter a food  to purchas:")
    if(food.lower() == "esc"):
        break
    else:
        price = float(input(f"Enter a price of {food} :$"))
        quantity = int(input(f"Enter quantity of {food}:"))
        Foods.append(food)
        Quantity.append(quantity)
        Price.append(price)
        prices.append(price*quantity)

print("====CHECKOUT====")
print("Your order")
print("Item : Quantity X Price : cost($)")

for i in range (0,len(Foods)):
    print(f"{Foods[i]} : {Quantity[i]}'s X ${Price[i]} = ${prices[i]}")
print(f"Total amount : ${sum(prices)}")
print("Thankyou for your purchase.")