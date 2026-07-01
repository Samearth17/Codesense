from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/items', methods=['GET', 'POST'])
def items():
 if request.method == 'GET':
 # Return all items
 # ...
 elif request.method == 'POST':
 # Create a new item
 # ...

@app.route('/items/<id>', methods=['GET', 'PUT', 'DELETE'])
def item(id):
 if request.method == 'GET':
 # Return item with given id
 # ...
 elif request.method == 'PUT':
 # Update item with given id
 # ...
 elif request.method == 'DELETE':
 # Delete item with given id
 # ...

if __name__ == '__main__': 
 app.run(debug=True)