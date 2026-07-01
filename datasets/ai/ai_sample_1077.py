from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
 {
 "title": "The Catcher in the Rye",
 "author": "JD Salinger"
 },
 {
 "title": "Lord of the Flies",
 "author": "William Golding"
 },
 {
 "title": "1984",
 "author": "George Orwell"
 }
]

@app.route('/books', methods=['GET'])
def get_books():
 args = request.args
 title = args.get('title')
 author = args.get('author')

 result = []

 for book in books:
 if title and author:
 if book['title'] == title and book['author'] == author:
 result.append(book)
 elif title:
 if book['title'] == title:
 result.append(book)
 elif author:
 if book['author'] == author:
 result.append(book)
 else:
 result.append(book)

 return jsonify(result)

if __name__ == '__main__':
 app.run(debug=True)