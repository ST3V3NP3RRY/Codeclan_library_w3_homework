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


# current books in library route
@app.route("/contact")
def contact():
    return render_template("contact.html")
