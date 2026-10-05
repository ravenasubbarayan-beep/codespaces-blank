balance = 15000

print("===== WELCOME TO ATM =====")

while True:
    print("\n1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = int(input("Enter option: "))

    if option == 1:
        print("Your balance is Rs.", balance)
