from models.book import *
import datetime

book1 = Book(
    "The Lord of the Rings",
    "J R R Tolkien",
    "Fantasy",
    True,
    datetime.date(2022, 10, 14),
)
book2 = Book(
    "The Hitchhiker's Guide to The Galaxy",
    "Douglas Adams",
    "Sci-Fi",
    False,
    datetime.date(2022, 10, 7),
)
book3 = Book("Dune", "Frank Herbert", "Sci-Fi", True, datetime.date(2022, 10, 2))
book4 = Book(
    "Wolf Hall",
    "Hilary Mantel",
    "Historical Fiction",
    False,
    datetime.date(2022, 10, 19),
)
book5 = Book("1984", "George Orwell", "Dystopian", True, datetime.date(2022, 10, 7))
book6 = Book("The Shining", "Stephen King", "Horror", True, datetime.date(2022, 10, 2))


books = [book1, book2, book3, book4, book5, book6]

# Function to add a new book to list
# REMEMBER - functions need to be tested
def save_book(new_book):
    books.append(new_book)


def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)
