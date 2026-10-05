class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(self.name, "issued successfully.")
        else:
            print(self.name, "is not available.")

    def return_book(self):
        self.available = True
        print(self.name, "returned successfully.")


class User:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        print(self.name, "is borrowing a book.")
        book.issue()

    def give_back(self, book):
        print(self.name, "is returning a book.")
        book.return_book()


class Student(User):
    def borrow(self, book):
        print("Student", self.name)
        super().borrow(book)


class Teacher(User):
    def borrow(self, book):
        print("Teacher", self.name)
        super().borrow(book)


book = Book("Data Structures")
student = Student("Anu")
teacher = Teacher("Priya")

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        student.borrow(book)
    elif choice == 2:
        student.give_back(book)
    elif choice == 3:
        print("Book:", book.name)
        print("Status:", "Available" if book.available else "Issued")
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")