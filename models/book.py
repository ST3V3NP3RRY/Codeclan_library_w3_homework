# MVP - create a book class with Tile, Author and genre properties
# Extension - add a check_out property to book class
# Remember - test class properties and any functions.
class Book:
    def __init__(self, title, author, genre, checked_out):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.books = []

    # Add a book to book list
    def save_book(self, new_book):
        self.books.append(new_book)

    # Remove a book from the book list
    def delete_book(self, book_name):
        self.books.remove(book_name)

    # Count books in the list
    def count_books(self):
        return len(self.books)
