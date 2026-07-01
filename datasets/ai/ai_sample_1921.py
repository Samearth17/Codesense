import json

from flask import Flask, request, jsonify

app = Flask(__name__)

messages = {}

@app.route('/messages', methods=['GET', 'POST'])
def all_messages():
 if request.method == 'POST':
 message = request.get_json()
 messages[message['id']] = message
 return jsonify(messages)
 
 elif request.method == 'GET':
 return jsonify(messages)
 

@app.route('/messages/<int:message_id>', methods=['GET', 'PUT', 'DELETE'])
def single_message(message_id):
 if request.method == 'GET':
 if message_id in messages:
 return jsonify(messages[message_id])
 
 elif request.method == 'PUT':
 message = request.get_json()
 messages[message_id] = message
 return jsonify(messages[message_id])
 
 elif request.method == 'DELETE':
 del messages[message_id]
 return jsonify({'message': 'Message deleted'})


if __name__ == '__main__':
 app.run(debug=True)