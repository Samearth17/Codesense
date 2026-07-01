class Library:
  def __init__(self, name, books):
     self.name = name
     self.books = books
     
  def show_checked_out_books(self):
    for book in self.books:
      if book.checked_out:
        print ("Name: {}, Author: {}".format(book.name, book.author))

class Book:
  def __init__(self, name, author, checked_out):
    self.name = name
    self.author = author
    self.checked_out = checked_out
    
library = Library("My Library", [Book("Harry Potter", "JK Rowling", True), 
  Book("Lord of the Rings", "JRR Tolkien", False)])

library.show_checked_out_books()