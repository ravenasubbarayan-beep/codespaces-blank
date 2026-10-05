def strength(password):
    if len(password) >= 8 and any(ch.isdigit() for ch in password):
        if any(not ch.isalnum() for ch in password):
            return "Strong"
        return "Medium"
    return "Weak"


def encrypt(password):
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) + 4)

    return encrypted


while True:
    print("\n--- PASSWORD SECURITY SYSTEM ---")
    print("1. Validate Password")
    print("2. Encrypt and Store")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter password: ")
        print("Password Strength:", strength(password))

    elif choice == "2":
        password = input("Enter password: ")

        if strength(password) == "Weak":
            print("Password is too weak.")
        else:
            encrypted = encrypt(password)

            with open("secure_password.txt", "w") as file:
                file.write(encrypted)

            print("Encrypted Password:", encrypted)
            print("Password stored successfully.")

    elif choice == "3":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")