# (05:38:34)

# slot machine

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("****************")
    print("|".join(row))

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒" :
             return bet*3
        elif row[0] == "🍉":   
             return bet*5
        elif row[0] == "🍋":   
             return bet*7
        elif row[0] == "🔔":   
             return bet*9
        elif row[0] == "⭐":   
             return bet*11
    else :
         return 0
    

def main():
    balance = 1000
    print("****************")
    print("Welcome to Slots")
    print("****************")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("****************")
    while balance > 0 :
        print(f"Current balance: ${balance}")
        print("****************************")
        bet = (input("Place your bet amount : "))
        if  not bet.isdigit():
                print("Please enter valid number")
                continue
        
        bet = int(bet)
        if (bet > balance):
             print("Insuffficent funds")
             continue
        if bet <= 0 :
             print("That must be greater than zero")
             continue
        balance -= bet

        row = spin_row()
        print("Spinning.....")
        print_row(row)

        payout = get_payout(row , bet)
        if payout > 0 :
             print(f"You won ${payout}")
        else:
             print("Sorry you Lost this round")
        balance += payout

        play_again = input("Do you want to spin again?(Y/N)")

        if play_again.upper() != "Y":
             break
        
    print(f"Game Over ! Your balance is ${balance}")

if __name__ == "__main__":
    main()