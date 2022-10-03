from flask import render_template, request, redirect
from app import app
from models import book_list #is this overkill, models.book_list below?
from models import book
from models.book_list import books, add_new_book, delete_book
from models.book import *

@app.route("/books")
def index():
    return render_template("index.html", title="home", books=books)

@app.route("/books")
def contact():
    return render_template("contact.html")

@app.route("/books", methods=["POST"])
def add_new_book():
    author = request.form["author"]
    checked_out = True if "checked_out" in request.form else False
    title = request.form["title"]
    isbn = request.form["isbn"]
    genre = request.form["genre"]
    book_description = request.form["book_description"]
    newbook = book(author=author, title=title, isbn=isbn, genre=genre, book_description=book_description)
    add_new_book(newbook)
    return redirect("/books")

@app.route('/books/delete/<name>', methods=['POST'])#check /delete/<name>? remind myself<name>
def delete(book):  #had (title), perhaps too specific
  delete_book(book)
  return redirect('/books')

@app.route('/books/delete/<name>', methods=['POST'])
def checked_out(book):
    





