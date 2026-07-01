import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a connection to the database
conn = sqlite3.connect('example.db')

# Create an endpoint to handle creating data
@app.route('/', methods=['POST'])
def create_data():
 data = request.json
 conn.execute('INSERT INTO data (data) VALUES (?)', (data,))
 conn.commit()
 return jsonify({'inserted': data})

# Create an endpoint to handle reading data
@app.route('/<int:id>/', methods=['GET'])
def read_data(id):
 cursor = conn.execute('SELECT data FROM data WHERE id=?', (id,))
 row = cursor.fetchone()
 return jsonify({'id': id, 'data': row})

# Create an endpoint to handle updating data
@app.route('/<int:id>/', methods=['PUT'])
def update_data(id):
 data = request.json
 conn.execute('UPDATE data SET data=? WHERE id=?', (data, id))
 conn.commit()
 return jsonify({'updated': data})

# Create an endpoint to handle deleting data
@app.route('/<int:id>/', methods=['DELETE'])
def delete_data(id):
 conn.execute('DELETE FROM data WHERE id=?', (id,))
 conn.commit()
 return jsonify({'deleted': id})

if __name__ == '__main__':
 app.run()