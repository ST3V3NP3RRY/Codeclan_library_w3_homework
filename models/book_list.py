from models.book import *

book1 = Book("The Lord of the Rings", "J R R Tolkien", "Fantasy")
book2 = Book("The Hitchhiker's Guide to The Galaxy", "Douglas Adams", "Sci-Fi")
book3 = Book("Dune", "Frank Herbert", "Sci-Fi")
book4 = Book("Wolf Hall", "Hilary Mantel", "Historical Fiction")
book5 = Book("1984", "George Orwell", "Dystopian")
book6 = Book("The Shining", "Stephen King", "Horror")


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
