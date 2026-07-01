import mysql.connector
from flask import Flask, request

app = Flask(__name__)

db = mysql.connector.connect(
 host='localhost',
 user='user',
 database='database',
)

cursor = db.cursor()

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
 user = request.get_json()
 try:
  cursor.execute(
   'UPDATE users SET name = %s, email = %s WHERE id = %s',
   (user['name'], user['email'], user_id)
  )
  db.commit()
  return {'message': 'User updated'}
 except mysql.connector.Error as err:
  db.rollback()
  return {'error': err.msg}, 500

if __name__ == '__main__':
 app.run(debug=True)