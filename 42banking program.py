# (05:23:34)

# banking program

# 1.Show balance
# 2.deposit
# 3.withdraw


def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    dep = int(input("Enter an amount to be deposited :"))
    return dep

def withdraw(balance):
    wit = int(input("Enter an amount to be withdrawed:"))
    if (wit > balance):
        print("Insufficent funds")
        return 0
    else :
        return wit

def main():

    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.exit")
        print("***************")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit(balance)
            show_balance(balance)
        elif choice == 3:
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Invalid choice")
    print("Thank you !! Have a nice day")

if __name__ == "__main__":
    main()