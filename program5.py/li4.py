class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title, "-", book.status)


class Book:
    def __init__(self, title):
        self.title = title
        self.status = "Available"

    def issue(self):
        self.status = "Issued"


class User:
    def __init__(self, name):
        self.name = name

    def operation(self, book):
        print(self.name, "performs library operation.")
        book.issue()


class Student(User):
    def operation(self, book):
        print("Student", self.name, "issues", book.title)
        book.issue()


class Teacher(User):
    def operation(self, book):
        print("Teacher", self.name, "issues", book.title)
        book.issue()


library = Library()

book1 = Book("Python")
book2 = Book("Java")

library.add_book(book1)
library.add_book(book2)

student = Student("Rahul")
teacher = Teacher("Anitha")

student.operation(book1)
teacher.operation(book2)

print("\nLibrary Books:")
library.show_books()