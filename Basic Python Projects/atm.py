#ATM Balance Simulation
balance = 2000
#Display a menu
def menu():
    print("Choose the menus:")
    print("1. Check Balance")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Exit ")
    
#Ask user to do input
def inp():
    while True:
        try:
            option = int(input("Choose: "))
            return option
        
        except ValueError:
            print("Invalid amount")

#Go into underchoice
def choose(option):
    global balance
    while True:
        try:
            if option == 1:
                print(balance)
                    
            elif option == 2:
                deposit = int(input("Input deposit: "))
                if deposit >= 0:
                    balance += deposit
                    print(f"Enter deposit: ${deposit :=.2f}")
            
            elif option == 3:
                withdraw = int(input("Input Withdraw: "))
                check = print(balance)
                if balance >= withdraw:
                    balance -= withdraw
                    print(f"Enter withdraw: ${withdraw :=.2f}")
                else:
                    print("Insufficient amount")
            
            elif option == 4:
                break
                
            else:
                print("Invalid number")
        
        except ValueError:
            print("Insufficient amount")

def main():
    menu()
    option = inp()
    choose(option)
    
main()

#ATM Balance Fixed
balance = 1000.0

def check_balance():
    print(f"Current balance is: ${balance :=.2f}")
    
def deposit():
    global balance
    try:
        deposit = float(input("Input deposit: $"))
        if deposit >= 0:
            balance += deposit
            print(f"Succesfully deposited ${deposit :=.2f}")
        else:
            print("Insufficient amount.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def withdraw():
    global balance
    try:
        withdraw = float(input("Input withdrawal: $"))
        
        if withdraw <= 0:
            print("Insufficient amount.")
        elif withdraw > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw
            print(f"Succesfully withdraw: ${withdraw :=.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def main():
    while True:
        print("\n===== Choose the menus =====")
        print("1. Check Balance")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")
    
        try:
            option = int(input("Choose: "))
            
            if option == 1:
                check_balance()
            elif option == 2:
                deposit()
            elif option == 3:
                withdraw()
            elif option == 4:
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice. Please enter number 1-4.")
            
        except ValueError:
            print("Invalid number")

main()