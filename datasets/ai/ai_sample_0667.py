from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    course = db.Column(db.String(20))

@app.route('/get_students')
def get_students():
    students = Student.query.all()
    students_list = []

    for student in students:
        student_data = {}
        student_data['name'] = student.name
        student_data['age'] = student.age
        student_data['course'] = student.course
        students_list.append(student_data)

    return json.dumps(students_list)