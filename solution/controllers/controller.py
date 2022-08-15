from flask import redirect, request, render_template

from app import app
from models.book import Book
from models.books import books, add_book, delete_book


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books_index():
    return render_template("books/index.html", books=books)


@app.route("/books/<index>")
def books_show(index):
    book = books[int(index)]
    return render_template("books/show.html", book=book, index=index)


@app.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre, False)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/new")
def books_new():
    return render_template("books/new.html")


@app.route("/books/delete/<index>", methods=["POST"])
def books_delete(index):
    delete_book(int(index))
    return redirect("/books")


@app.route("/books/<index>", methods=["POST"])
def books_update(index):
    book = books[int(index)]
    checked_out = "checked_out" in request.form
    book.toggle_check_out(checked_out)
    return redirect("/books/" + index)
