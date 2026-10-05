def check_strength(password):
    if len(password) < 8:
        return "Weak"
    elif password.isalnum():
        return "Medium"
    else:
        return "Strong"

def encrypt(password):
    result = ""
    for ch in password:
        result += chr(ord(ch) + 3)
    return result

password = input("Enter password: ")

strength = check_strength(password)
print("Password Strength:", strength)

encrypted = encrypt(password)

with open("password.txt", "w") as file:
    file.write(encrypted)

print("Encrypted Password:", encrypted)
print("Password stored successfully.")