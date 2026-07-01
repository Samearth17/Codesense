from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token,
 jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret'
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
 username = request.json.get('username', None)
 password = request.json.get('password', None)

 # Register user here

 access_token = create_access_token(identity=username)
 refresh_token = create_refresh_token(identity=username)
 return jsonify(message='User created', access_token=access_token, refresh_token=refresh_token)
 
@app.route('/login', methods=['POST'])
def login():
 username = request.json.get('username', None)
 password = request.json.get('password', None)

 # Validate user here

 access_token = create_access_token(identity=username)
 refresh_token = create_refresh_token(identity=username)
 return jsonify(message='Logged in', access_token=access_token, refresh_token=refresh_token)

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
 username = get_jwt_identity()
 return jsonify(message='Welcome %s' % username)

if __name__ == '__main__':
 app.run()