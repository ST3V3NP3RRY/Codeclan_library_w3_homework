# MVP - create a book class with Tile, Author and genre properties
# Extension - add a check_out property to book class
# Remember - test class properties and any functions.
class Book:
    def __init__(self, title, author, genre, checked_out, return_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.return_date = return_date
        self.books = []

    # Add a book to book list
    def save_book(self, new_book):
        self.books.append(new_book)

    # Remove a book from the book list
    def delete_book(self, book):
        self.books.remove(book)

    # Count books in the list
    def count_books(self):
        return len(self.books)

    def find_book_by_title(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
            return None

    def remove_book_by_title(self, book_title):
        for book in self.books:
            if book_title == book.title:
                self.books.remove(book)
