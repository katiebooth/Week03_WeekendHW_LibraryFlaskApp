from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.book_list import books

@app.route('/')
def start():
    return "Hello, welcome to the library! Please add '/books' in the URL to go to the homepage"

@app.route('/books')
def index():
    return render_template('index.html', title = "Library", books = books)

@app.route('/books/<index>')
def show(index):
    book_to_show = books[int(index)]
    return render_template('show.html',book=book_to_show)

#add new book
@app.route('/books/new')
def new():
    return render_template('new.html')

@app.route('/books', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title,author,genre,False)
    books.append(new_book)
    return redirect('/books')

#remove book
@app.route('/books/remove/<title>', methods=['POST'])
def remove(title):
    book_to_delete = None
    for book in books:
        if book.title == title:
            book_to_delete = book
            break
    books.remove(book_to_delete)
    return redirect('/books')
    
#Check out book
@app.route('/books/check_out/<title>', methods =['POST'])
def check_out(title):
    book_to_update = None
    for book in books:
        if book.title == title:
            book_to_update = book
            break
    book.checked_out = True
    return redirect('/books')

#Check in book
@app.route('/books/check_in/<title>', methods =['POST'])
def check_in(title):
    book_to_update = None
    for book in books:
        if book.title == title:
            book_to_update = book
            break
    book.checked_out = False
    return redirect('/books')


#Unused option - create a page with all books to check out, but how to update the /books page?
# @app.route('/books/check_out')
# def check_out():
#     return render_template('check_out.html', books=books)

#not used for the delete function
# @app.route('/books/remove')
# def delete():
#     return render_template('remove.html')