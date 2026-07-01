from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
import hashlib

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
 # Get form data
 data = request.get_json()
 public_id = str(uuid.uuid4())
 username = data['username']
 password = data['password']
 hashed_password = hashlib.sha256(password.encode()).hexdigest()
 
 # Create new user
 user = User(public_id, username, hashed_password)
 db.session.add(user)
 db.session.commit()
 
 return jsonify({'public_id': public_id})

@app.route('/authenticate', methods=['POST'])
def authenticate():
 data = request.get_json()
 username = data['username']
 password = data['password']
 
 user = User.query.filter_by(username=username).first()
 
 if user and hashlib.sha256(password.encode()).hexdigest() == user.password:
  return jsonify({'public_id': user.public_id})

if name == 'main':
 app.run(debug=True)