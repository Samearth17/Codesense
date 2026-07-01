import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

todos = [
 {
 'id': 1,
 'title': 'buy groceries',
 'completed': False
 },
 {
 'id': 2,
 'title': 'clean room',
 'completed': False
 }
]

@app.route('/', methods=['GET'])
def home():
 return '''<h1>To-Do List API</h1>
 <p>A prototype API for a To-Do List application.</p>'''

@app.route('/api/v1/todos/', methods=['GET'])
def api_all():
 return flask.jsonify(todos)

@app.route('/api/v1/todos/', methods=['POST'])
def api_create():
 data = request.get_json()
 todos.append(data)
 return flask.jsonify(data)

@app.route('/api/v1/todos/<int:id>', methods=['PUT', 'PATCH'])
def api_update(id):
 for todo in todos:
 if todo['id'] == id:
 data = request.get_json()
 for key, value in data.items():
 todo[key] = value
 return flask.jsonify(todo)

@app.route('/api/v1/todos/<int:id>', methods=['DELETE'])
def api_delete(id):
 for i, todo in enumerate(todos):
 if todo['id'] == id:
 del todos[i]
 return flask.jsonify({'success': True})

app.run()