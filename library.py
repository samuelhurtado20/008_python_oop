from books import Book, PhysicalBook, EBook

from library import Library, UserNotFoundError

from users import Student, Teacher, UserProtocol

from exceptions import LibraryError, BookNotAvailableError

from data import data_books, data_users

library = Library("City Library")

teacher1 = Teacher("Dr. Smith", "456", "Mathematics")

library.users = [teacher1] + data_users

library.books = data_books

print(f"\nLibrary: {library.name}\n")

print("📚 Books in library:")

for book in library.available_books():

    print(f" - {book}")

# Find a user by ID

id = input("Enter user ID to find: ")

try:

    user = library.find_user(id)

    print(f"Welcome, {user.name}, user {user.ide}!")

except UserNotFoundError as e:

    print(f"Library Error: {e},type: {type(e)}")

    print("Error: User not found in the library system.")

print("\n--- User Details ---")

print(user)

# Borrow a book

title = input("Enter book title to borrow: ")

try:

    book = library.find_book(title)

except LibraryError as e:

    print(f"Library Error: {e},type: {type(e)}")

    print("Error: Could not borrow the book.")

result = user.request_book(book.title)

print(result)

try:

    result_borrow = book.lend_book()

    print(f"\n{result_borrow}")

except BookNotAvailableError as e:

    print(f"Library Error: {e},type: {type(e)}")

    print("Error: Could not borrow the book.")