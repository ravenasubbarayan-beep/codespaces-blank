student = {}

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        reg = input("Enter Register Number: ")
        name = input("Enter Student Name: ")
        student[reg] = name
        print("Student Added Successfully")

    elif choice == 2:
        reg = input("Enter Register Number to Search: ")
        if reg in student:
            print("Name:", student[reg])
        else:
            print("Student Not Found")

    elif choice == 3:
        reg = input("Enter Register Number to Delete: ")
        if reg in student:
            del student[reg]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == 4:
        if student:
            print("\nStudent Details")
            for reg, name in student.items():
                print("Register No:", reg, " Name:", name)
        else:
            print("No Student Records")

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")