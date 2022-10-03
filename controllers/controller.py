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
    if date == "":
        pass
    else:
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    # -------------------------------------------------------------------------------------
    # Question1: There's a bug in my code. When the user inputs a book with a date left blank
    # I get a ValueError: invalid literal for int() with base 10: '' which I assume is because
    # I'm passing in an empty string. Is there a way to fix this?
    # -------------------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------------------
    # Question2: How could I output a summary of each book on the single book page based on
    # the index of the books list?
    # -------------------------------------------------------------------------------------

    summary_list = [
        # LOTR summary ---------------------------------------------------------------------
        "At 33, the age of adulthood among hobbits, Frodo Baggins receives a magic Ring of Invisibility from his uncle Bilbo. Frodo, a Christlike figure, learns that the ring has the power to control the entire world and, he discovers, to corrupt its owner. A fellowship of hobbits, elves, dwarfs, and men is formed to destroy the ring by casting it into the volcanic fires of the Crack of Doom, where it was forged. They are opposed on their harrowing mission by the evil Sauron and his Black Riders.",
        # HGTTG summary -------------------------------------------------------------------
        "The Hitchhiker's Guide to the Galaxy begins with contractors arriving at Arthur Dent's house, in order to demolish it to make way for a bypass. His friend, Ford Prefect, arrives while Arthur is lying in front of the bulldozers, to stop them from demolishing it. He tries to explain to Arthur that he is actually from a planet somewhere in the vicinity of Betelgeuse and that the Earth is about to be demolished. The Vogons, an alien race, intend to destroy Earth to make way for a hyperspace bypass.",
        # Dune summary -----------------------------------------------------------------------
        "Dune is a literary piece of science fiction that tells the story of humanity thousands of years into the future. In the novel, humanity becomes so advanced that it spreads across the known universe. With the spread of humans, noble houses are formed, with each governing a planetary system.Dune focuses on the story of Paul Atreides, the young heir to House Atreides whose father gets assigned by Shaddam IV, the Emperor, to govern the planet Arrakis, a desert world with a crucial commodity called Melange. Obeying the command, Paul's father, Leto, decides to leave Caladan, his home planet, for Arrakis. However, Leto is sure his enemies are plotting against him.",
    ]

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
