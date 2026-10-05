class Book:
    def __init__(self, title):
        self.title = title
        self.status = "Available"

    def issue(self):
        self.status = "Issued"
        print(self.title, "has been issued.")

    def return_book(self):
        self.status = "Available"
        print(self.title, "has been returned.")


class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        book.issue()


class Student(User):
    def borrow_book(self, book):
        print("Student", self.name, "borrows the book.")
        super().borrow_book(book)


class Teacher(User):
    def borrow_book(self, book):
        print("Teacher", self.name, "borrows the book.")
        super().borrow_book(book)


class Librarian(User):
    def borrow_book(self, book):
        print("Librarian", self.name, "handles the book.")
        super().borrow_book(book)


book = Book("Computer Networks")

users = [
    Student("Arun"),
    Teacher("Meena"),
    Librarian("Ravi")
]

for user in users:
    print("\nUser Type:", type(user).__name__)
    user.borrow_book(book)
    book.return_book()