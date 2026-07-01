import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# Database functionality
# classes used to represent the objects
class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# lists of books
books = []

# endpoints
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        books.append(Book(post_data.get('title'), post_data.get('author'), post_data.get('isbn')))
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = [book.__dict__ for book in books] 

    return jsonify(response_object)

@app.route('/books/<int:isbn>', methods=['PUT', 'DELETE'])
def single_book(isbn):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        book = next(filter(lambda x: x.isbn == isbn, books), None)
        if book:
            book.title = post_data.get('title')
            book.author = post_data.get('author')
            response_object['message'] = 'Book updated'
        else:
            response_object['message'] = 'Book does not exist'
    if request.method == 'DELETE':
        global books
        books = list(filter(lambda x: x.isbn != isbn, books))
        response_object['message'] = 'Book deleted'
    return jsonify(response_object)

# Run the application
if __name__ == '__main__':
    app.run()