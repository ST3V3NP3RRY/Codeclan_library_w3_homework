import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Dune", "Frank Herbert", "Sci-Fi")

    def test_book_has_title(self):
        self.assertEqual("Dune", self.book.title)

    def test_book_has_author(self):
        self.assertEqual("Frank Herbert", self.book.author)

    def test_book_has_genre(self):
        self.assertEqual("Sci-Fi", self.book.genre)
