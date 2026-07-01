class Book:
 def __init__(self, title, author, year):
 self.title = title
 self.author = author
 self.year = year

 def __str__(self):
 return f'{self.title} by {self.author} ({self.year})'

class BookDB:
 def __init__(self):
 self.books = []

 def add_book(self, book):
 self.books.append(book)

 def delete_book(self, title):
 self.books = [book for book in self.books if book.title != title]

 def search_book(self, title):
 for book in self.books:
 if book.title == title:
 return book

 return None