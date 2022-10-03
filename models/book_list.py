from models.book import *

book = Book("John le Carre", "Siverview", "Thriller", 978, "Trust", True)
book1 = Book("John Lennon", "Catcher in the Rye", "Adult Fiction", 498, "Coming of age", False)
book2 = Book("Yann Martel",  "Life of Pi", 234, "Psychological Fiction ","metaphisics", False)
book3 = Book("Giles Milton", "Nathaniels Nutmeg", 468, "History", "Adventures of a 16th century spice trader", False)

books = [book, book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book):
    delete_book = None
    for book in books:
        if book.title == ["title"]:
            delete_book = book
            break
    
    books.remove(delete_book)

def checked_out(book):
    checked_out = None
    for book in books:
        if book == [True]:
            return #thinking about whats returned
            #should be icon wk3/day_4
        

