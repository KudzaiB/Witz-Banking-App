#22544762 Project: Fundamentals of Programming Banking Program
#Witz App


from random import choice
USERNAME = "admin"
PASSWORD = "password"

def login():
    print("===================================")
    print("         Welcome to Witz App    ")
    print("===================================")

    while True:
        username = input("Enter Username:\n")
        password = input("Enter Password:\n")
        if username == USERNAME and password == PASSWORD:
            print("Login Successful!\n")
            break
        else:
            print("Invalid credentials. Try again.\n")

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited:\n "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:\n "))

    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    login()
    balance = 0
    is_running = True

    while is_running:
        print("===================================")
        print("             Main Menu             ")
        print("===================================")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Logout")
        print("====================================")

        choice = input("Enter your choice (1-4):\n ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("====================================")
            print("This is not a valid choice")
            print("====================================")

    print("====================================")
    print("Thank you, have a nice day.")
    print("====================================")

if __name__ == '__main__' :
    main()