#Create a Bank Program with these main features:-
# 1. show balane()
# 2. deposit()
# 3. withdraw()

print("#-----------Banking Program------------#")
def show_balance(balance):
    print(f"Your Balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount for deposit: "))
    if amount < 0:
        print("Amount should be greater than zero.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount for withdraw: "))
    if amount > balance:
        print("Insufficient Balance.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit---X")
        
        choice = input("Enter your choice(1-4): ")
        
        if choice == '1':
            show_balance(balance)
            
        elif choice == '2':
            balance += deposit()
            
        elif choice == '3':
            balance -= withdraw(balance)
            
        elif choice == '4':
            is_running = False
            
        else:
            print("Not a valid choice")
            
    print("Thank You Have a Nice Day.....!")
    
if __name__ == '__main__':
    main()