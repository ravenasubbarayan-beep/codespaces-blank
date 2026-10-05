balance = 8000

while True:
    print("\n----- ATM SYSTEM -----")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("Available Balance:", balance)

    elif choice == "2":
        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:
            balance = balance + deposit
            print("Deposit Successful")
        else:
            print("Enter a valid amount")

    elif choice == "3":
        withdrawal = float(input("Enter withdrawal amount: "))

        if withdrawal > 5000:
            print("Daily withdrawal limit is Rs.5000")
        elif withdrawal <= 0:
            print("Invalid Amount")
        elif withdrawal > balance:
            print("Insufficient Balance")
        else:
            balance = balance - withdrawal
            print("Withdrawal Successful")
            print("Please collect your cash")

    elif choice == "4":
        print("Thank you. Visit Again!")
        break

    else:
        print("Invalid Option")