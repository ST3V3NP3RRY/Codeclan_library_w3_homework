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
    checked_out = True if "checked_out" in request.form else False
    date = request.form["date"]
    split_date = date.split("-")
    # Reassign date variables value
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    new_book = Book(
        title=title,
        author=author,
        genre=genre,
        checked_out=checked_out,
        return_date=date,
    )

    save_book(new_book)
    return redirect("/books")


# Route to find a single book
@app.route("/books/<index>")
def single_book(index):
    chosen_book = books[int(index)]
    return render_template("single_book.html", book=chosen_book)


# Route to delete a book
@app.route("/books/delete/<title>", methods=["POST"])
def delete(title):
    delete_book(title)
    return redirect("/books")


# current books in library route
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def thanks():
    return render_template("thanks.html")
