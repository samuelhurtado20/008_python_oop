import  random

class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.isPopular = False
        self.loaned_count = 0

    def __str__(self):
        return f"Book => Title: {self.title} - Author: {self.author} - ISBN: {self.isbn} - Available: {self.available} - Is Popular: {self.isPopular}"

    def lend_book(self):
        if self.available:
            self.available = False
            self.loaned_count += 1
            if self.loaned_count >= 5:
                self.isPopular = True
            return  f"the title {self.title} was successfully loaned"
        return None

    def return_book(self):
        if not self.available:
            self.available = True
            return f"the title {self.title} was successfully returned"
        return None


my_book = Book("Cien Años de Soledad", "Gabriel García Márquez", random.randint(900_000_000_000, 999_999_999_999),  True)
other_book = Book("El Principito", "Saint-Exupéry", random.randint(900_000_000_000, 999_999_999_999), True)

catalog = [my_book, other_book]
for book in catalog:
    print(book)

print("========================")
print(my_book.lend_book())
print(my_book)

print("========================")
print(my_book.return_book())
print(my_book)

print(my_book.lend_book())
print(my_book.return_book())
print(my_book.lend_book())
print(my_book.return_book())
print(my_book.lend_book())
print(my_book.return_book())
print(my_book.lend_book())
print(my_book.return_book())
print(my_book)