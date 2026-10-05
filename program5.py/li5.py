class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = None

    def issue(self, user):
        if self.issued_to is None:
            self.issued_to = user.name
            print(self.title, "issued to", user.name)
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.issued_to:
            print(self.title, "returned by", self.issued_to)
            self.issued_to = None
        else:
            print("Book is already available.")

    def display(self):
        status = self.issued_to if self.issued_to else "Available"
        print(self.book_id, self.title, self.author, status)


class User:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        book.issue(self)

    def return_book(self, book):
        book.return_book()


class Student(User):
    def borrow(self, book):
        print("Student borrowing...")
        super().borrow(book)


class Teacher(User):
    def borrow(self, book):
        print("Teacher borrowing...")
        super().borrow(book)


book1 = Book(101, "Python Programming", "Guido van Rossum")
book2 = Book(102, "Data Structures", "Mark Allen")

student = Student("Ravi")
teacher = Teacher("Kumar")

print("LIBRARY BOOKS")
book1.display()
book2.display()

print("\nOperations:")
student.borrow(book1)
teacher.borrow(book2)

print("\nUpdated Details:")
book1.display()
book2.display()

print("\nReturning Books:")
student.return_book(book1)
teacher.return_book(book2)

print("\nFinal Details:")
book1.display()
book2.display()