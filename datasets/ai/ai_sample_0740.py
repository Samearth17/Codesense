import requests
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Data(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(50), nullable=False)
 age = db.Column(db.Integer, nullable=False)

db.create_all()

@app.route('/fetch', methods=['GET'])
def fetch_data():
 r = requests.get('https://example.com/public-api/data')
 response = r.json()
 
 for item in response:
  data = Data(name=item['name'], age=item['age'])
  db.session.add(data)

 db.session.commit()
 return {'message': 'Data successfully fetched'}

if name == 'main':
 app.run(debug=True)