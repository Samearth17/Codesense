import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/query', methods=['GET'])
def get_data():
 query = request.args['query']
 users = db.session.execute(query)
 users_list = [dict(user) for user in users]
 return json.dumps({ "users": users_list })

if name == 'main':
 app.run(debug=True)