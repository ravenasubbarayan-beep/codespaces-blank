def password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

def xor_encrypt(password, key=5):
    encrypted = ""
    
    for ch in password:
        encrypted += chr(ord(ch) ^ key)
    
    return encrypted

password = input("Enter password: ")

strength = password_strength(password)
print("Password Strength:", strength)

encrypted = xor_encrypt(password)

with open("encrypted_password.txt", "w") as file:
    file.write(encrypted)

print("Encrypted password stored in file.")