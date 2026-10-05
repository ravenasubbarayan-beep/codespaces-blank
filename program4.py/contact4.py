contacts = []

def add():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    print("Contact added.")

def display():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        for c in contacts:
            print("\nName:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])

def search():
    key = input("Enter name: ")

    for c in contacts:
        if key.lower() in c["name"].lower():
            print(c)
            return

    print("Contact not found.")

def delete():
    key = input("Enter name to delete: ")

    for c in contacts:
        if c["name"].lower() == key.lower():
            contacts.remove(c)

            with open("deleted_contacts.txt", "a") as file:
                file.write(str(c) + "\n")

            print("Contact deleted.")
            return

    print("Contact not found.")

while True:
    print("\n--- CONTACT MANAGEMENT ---")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")