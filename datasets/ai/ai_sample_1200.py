import re

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/emailcheck/<string:email>", methods=['GET'])
def validate_email(email):

 if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
  return jsonify({'email': email, 'valid': True})
 else:
  return jsonify({'email': email, 'valid': False})

if __name__ == '__main__':
 app.run(debug=True)