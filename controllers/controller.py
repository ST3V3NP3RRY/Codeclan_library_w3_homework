from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.book_list import *


# Home page route
@app.route("/")
def index():
    return render_template("index.html")


# current books in library route
@app.route("/books")
def current_books():
    return render_template("books.html", books=books)


# New route for form data to add a book
@app.route("/books", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    # checked_out = request.form(["checked_out"])

    new_book = Book(title, author, genre)

    save_book(new_book)
    return redirect("/books")


# current books in library route
@app.route("/contact")
def contact():
    return render_template("contact.html")
