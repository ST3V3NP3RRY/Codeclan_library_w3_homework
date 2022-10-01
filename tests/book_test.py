import unittest
from models.book import Book
from models.book_list import *
import datetime


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            "Dune", "Frank Herbert", "Sci-Fi", True, datetime.date(2022, 10, 14)
        )
        self.book1 = Book(
            "The Hitchhiker's Guide to The Galaxy",
            "Douglas Adams",
            "Sci-Fi",
            False,
            datetime.date(2022, 10, 7),
        )
        self.book2 = Book(
            "1984", "George Orwell", "Dystopian", True, datetime.date(2022, 10, 19)
        )

        self.books = []

    def test_book_has_title(self):
        self.assertEqual("Dune", self.book.title)

    def test_book_has_author(self):
        self.assertEqual("Frank Herbert", self.book.author)

    def test_book_has_genre(self):
        self.assertEqual("Sci-Fi", self.book.genre)

    def test_books_start_at_0(self):
        self.assertEqual(0, len(self.books))

    def test_can_add_book_to_list(self):
        self.book.save_book(self.book1)
        self.assertEqual(1, len(self.book.books))

    def test_can_remove_book_from_list(self):
        self.book.save_book(self.book1)
        self.book.delete_book(self.book1)
        self.assertEqual(0, len(self.books))

    def test_book_has_return_date(self):
        self.assertEqual(datetime.date(2022, 10, 14), self.book.return_date)

    @unittest.skip("delete this line to run the test")
    def test_can_remove_book_by_title(self):
        pass

    @unittest.skip("delete this line to run the test")
    def test_book_can_be_checked_out(self):
        pass
