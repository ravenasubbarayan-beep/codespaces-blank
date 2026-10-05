balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    while True:
        print("\n===== ATM =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = float(input("Enter amount: "))
            if amount > 0:
                balance += amount
                print("Deposited Successfully")
                print("Balance:", balance)
            else:
                print("Invalid Amount")

        elif choice == 3:
            amount = float(input("Enter amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("Balance:", balance)
            else:
                print("Insufficient Balance or Invalid Amount")

        elif choice == 4:
            print("Session Ended")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")