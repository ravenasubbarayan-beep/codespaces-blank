balance = 20000
correct_pin = "5678"
attempts = 3

while attempts > 0:
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful")

        while True:
            print("\n===== ATM MENU =====")
            print("1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Available Balance: Rs.", balance)

            elif choice == 2:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    print("Deposit Successful")
                    print("Balance: Rs.", balance)
                else:
                    print("Invalid Amount")

            elif choice == 3:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid Amount")
                elif amount > balance:
                    print("Insufficient Balance")
                else:
                    balance -= amount
                    print("Withdrawal Successful")
                    print("Balance: Rs.", balance)

            elif choice == 4:
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid Choice")

        break

    else:
        attempts -= 1
        print("Incorrect PIN")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("ATM Card Blocked. Too many incorrect attempts.")