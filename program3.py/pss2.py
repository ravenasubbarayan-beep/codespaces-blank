def validate(password):
    if len(password) >= 8 and not password.isalpha():
        return True
    return False

def encrypt(password):
    password = password[::-1]
    encrypted = ""
    
    for ch in password:
        encrypted += chr(ord(ch) + 2)
    
    return encrypted

password = input("Enter password: ")

if validate(password):
    print("Password Strength: Strong")
    
    encrypted = encrypt(password)

    with open("secure_data.txt", "w") as file:
        file.write(encrypted)

    print("Encrypted Password:", encrypted)
    print("Data saved successfully.")
else:
    print("Password Strength: Weak")
    print("Password must contain at least 8 characters and numbers/symbols.")