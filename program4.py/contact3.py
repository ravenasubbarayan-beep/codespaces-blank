contacts = []

def add_contact():
    contact = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "city": input("City: ")
    }

    contacts.append(contact)

    with open("contacts.txt", "a") as file:
        file.write(str(contact) + "\n")

    print("Contact added successfully.")

def search_contact():
    phone = input("Enter phone number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact Found")
            print(contact)
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter name: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return

    print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. Search by Phone")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")