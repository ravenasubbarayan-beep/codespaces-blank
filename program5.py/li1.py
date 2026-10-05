class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Issued" if self.issued else "Available")


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(self.name, "issued", book.title)
        else:
            print("Book is already issued.")

    def return_book(self, book):
        book.issued = False
        print(self.name, "returned", book.title)


class Student(User):
    def issue_book(self, book):
        print("Student:", self.name)
        super().issue_book(book)


class Teacher(User):
    def issue_book(self, book):
        print("Teacher:", self.name)
        super().issue_book(book)


book1 = Book("Python Programming", "Guido van Rossum")
student = Student("Ravi")
teacher = Teacher("Kumar")

student.issue_book(book1)
book1.display()

student.return_book(book1)
book1.display()

teacher.issue_book(book1)
book1.display()