contacts = []

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    contacts.append({
                        "name": data[0],
                        "phone": data[1],
                        "email": data[2]
                    })
    except FileNotFoundError:
        pass

def save_contacts():
    with open("contacts.txt", "w") as file:
        for c in contacts:
            file.write(
                c["name"] + "," +
                c["phone"] + "," +
                c["email"] + "\n"
            )

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts()
    print("Contact added successfully.")

def search_contact():
    name = input("Enter name to search: ")

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("\nContact Details")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            save_contacts()
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

load_contacts()

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        for c in contacts:
            print(c)

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")