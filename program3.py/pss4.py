def validate_password(password):
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if not ch.isalnum():
            has_special = True

    return len(password) >= 8 and has_digit and has_special


def encrypt_password(password):
    encrypted = []

    for ch in password:
        encrypted.append(str(ord(ch) + 10))

    return "-".join(encrypted)


password = input("Enter password: ")

if validate_password(password):
    print("Password is Strong")

    encrypted = encrypt_password(password)

    with open("password_data.txt", "w") as file:
        file.write(encrypted)

    print("Encrypted Data:", encrypted)
    print("Stored successfully.")
else:
    print("Password is Weak")
    print("Use at least 8 characters, one number and one special character.")