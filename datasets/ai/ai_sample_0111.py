from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(name)

# Mysql configuration
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'users'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/users', methods=['POST'])
def create_user():
 name = request.json['name']
 email = request.json['email']

 cur = mysql.connection.cursor()
 cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
 mysql.connection.commit()
 cur.close()

 return jsonify({'message': 'User created'})

@app.route('/users', methods=['GET'])
def get_users():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM users")
 users = cur.fetchall()
 cur.close()

 return jsonify(users)

@app.route('/users/int:id', methods=['GET'])
def get_user(id):
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM users WHERE id=%s", (id))
 user = cur.fetchone()
 cur.close()

 return jsonify(user)

if name == "main":
 app.run(debug=True)