from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.book_list import books

@app.route('/')
def start():
    return "Hello World"

@app.route('/books')
def library_index():
    return render_template('index.html', title = "Library", books = books)

@app.route('/books/new')
def new():
    return render_template('new.html')

@app.route('/books', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title,author,genre)
    books.append(new_book)
    return redirect('/books')
