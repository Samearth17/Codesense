import json 
import sqlite3
from flask import Flask, request, jsonify 

app = Flask(__name__) 
  
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d 
  
@app.route('/', methods=['GET'])
def index(): 
    connection = sqlite3.connect('database.db')
    connection.row_factory = dict_factory
    cur = connection.cursor() 
    all_users = cur.execute('SELECT * FROM users;').fetchall() 
    return jsonify(all_users) 
  
if __name__ == '__main__': 
    app.run(debug = True)