from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(db='mydb', user='root', passwd='', host='localhost')

@app.route('/records', methods=['GET'])
def get_records():
 cur = db.cursor()
 sql = 'SELECT * from records'
 cur.execute(sql)
 result = cur.fetchall()

 records = []
 for row in result:
 records.append(
 {
 'id': row[0],
 'name': row[1],
 'age': row[2]
 })

 return jsonify({'records': records})

@app.route('/records', methods=['POST'])
def create_record():
 name = request.form['name']
 age = request.form['age']

 cur = db.cursor()
 sql = (f"INSERT INTO records (name, age) VALUES('{name}', {age})")
 cur.execute(sql)
 db.commit()
 return jsonify(
 {
 'message': 'Record successfully created!'
 }
 )

@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
 name = request.form['name']
 age = request.form['age']

 cur = db.cursor()
 sql = (
 f"UPDATE records SET name = '{name}', age = {age} WHERE id={id}")
 cur.execute(sql)
 db.commit()
 return jsonify(
 {
 'message': 'Record successfully updated!'
 }
 )

@app.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
 cur = db.cursor()
 sql = (f"DELETE FROM records WHERE id={id}")
 cur.execute(sql)
 db.commit()
 return jsonify(
 {
 'message': 'Record successfully deleted!'
 }
 )

if __name__ == '__main__':
 app.run(debug=True)