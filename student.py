class User:
    def __init__(self, name, registration_number):
        self.name = name
        self.registration_number = registration_number
        self.__checked_out_books = []

    def get_checked_out_books(self):
        return self.__checked_out_books

    def set_checked_out_books(self, books):
        self.__checked_out_books = books

    def check_out_book(self, book_title):
        self.__checked_out_books.append(book_title)
        return f"{book_title} has been checked out"

    def check_in_book(self, book_title):
        if book_title in self.__checked_out_books:
            self.__checked_out_books.remove(book_title)
            return f"{book_title} has been checked in"
        else:
            return f"Didn't find {book_title} in the books list"


class Student(User):
    def __init__(self, name, registration_number, major):
        super().__init__(name, registration_number)
        self.major = major
        self.checked_out_books_limit = 3

    def check_out_book(self, book_title):
        if len(self.get_checked_out_books()) < self.checked_out_books_limit:
            return super().check_out_book(book_title)
        else:
            return f"Limit exceeded for checking out books. {book_title} couldn't be borrowed"


class Professor(User):
    pass


student = Student("Fran", "110011", "CS")
professor = Professor("Erick", "111011")

print(student.check_out_book("The Life of a Showgirl"))
print(student.check_out_book("The Tortured Poets Department"))
print(student.check_out_book("Midnights"))
print(student.check_out_book("Evermore"))
print("------------" * 10)
print(professor.check_out_book("The Life of a Showgirl"))
print(professor.check_out_book("The Tortured Poets Department"))
print(professor.check_out_book("Midnights"))
print(professor.check_out_book("Evermore"))