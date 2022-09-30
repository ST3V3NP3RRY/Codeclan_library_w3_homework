# MVP - create a book class with Tile, Author and genre properties
# Extension - add a check_out property to book class
# Remember - test class properties and any functions.
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.books = []

    # Add a book to book list
    def save_book(self, new_book):
        self.books.append(new_book)

    # Remove a book from the book list
    def delete_book(self, book_name):
        self.books.remove(book_name)

    def count_books(self):
        return len(self.books)
