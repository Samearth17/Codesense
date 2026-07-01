from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Task(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 description = db.Column(db.String(120), unique=True)

db.create_all()

@app.route('/tasks', methods=['POST'])
def create_task():
 task = Task(description=request.json['description'])
 db.session.add(task)
 db.session.commit()
 return {'id': task.id}

@app.route('/tasks', methods=['GET'])
def get_tasks():
 tasks = Task.query.all()
 return {'tasks': [task.description for task in tasks]}

@app.route('/tasks/int:id', methods=['GET'])
def get_task_info(id):
 task = Task.query.get(id)
 return {'id': task.id, 'description': task.description}

@app.route('/tasks/int:id', methods=['PUT'])
def update_task(id):
 task = Task.query.get(id)
 task.description = request.json['description']
 db.session.commit()
 return {'message': 'Task updated'}

@app.route('/tasks/int:id', methods=['DELETE'])
def delete_task(id):
 Task.query.filter_by(id=id).delete()
 db.session.commit()
 return {'message': 'Task deleted'}

if name == 'main':
 app.run(debug=True)