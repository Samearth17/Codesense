from flask import Flask, jsonify, request

app = Flask(__name__)

messages = []  # list to store customer messages

@app.route('/messages', methods=['POST', 'GET'])
def manage_messages():
    '''API endpoint to store and retrieve customer messages'''
    if request.method == 'POST':  # storing customer message
        customer_message = request.get_json()
        messages.append(customer_message)
        return jsonify(message='Message successfully stored'), 200

    elif request.method == 'GET':  # retrieving customer messages
        return jsonify(messages=messages), 200