from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(name)
api = Api(app)
 
employees = [
 {
 "name": "John Doe",
 "salary": 10000,
 "experience": 3
 },
 {
 "name": "Alice Smith",
 "salary": 12000,
 "experience": 4
 }
]
 
class Employee(Resource):
 def get(self, name):
 for employee in employees:
 if(name == employee["name"]):
 return employee, 200
 return "Employee not found", 404
 
 def post(self, name):
 parser = reqparse.RequestParser()
 parser.add_argument("salary")
 parser.add_argument("experience")
 args = parser.parse_args()
 
 for employee in employees:
 if(name == employee["name"]):
 return "Employee with name {} already exists".format(name), 400
 
 employee = {
 "name": name,
 "salary": args["salary"],
 "experience": args["experience"]
 }
 employees.append(employee)
 return employee, 201

def put(self, name):
 parser = reqparse.RequestParser()
 parser.add_argument("salary")
 parser.add_argument("experience")
 args = parser.parse_args()
 
 for employee in employees:
 if(name == employee["name"]):
 employee["salary"] = args["salary"]
 employee["experience"] = args["experience"]
 return employee, 200
 
 employee = {
 "name": name,
 "salary": args["salary"],
 "experience": args["experience"]
 }
 employees.append(employee)
 return employee, 201

def delete(self, name):
 global employees
 employees = [employee for employee in employees if employee["name"] != name]
 return "{} is deleted.".format(name), 200
 
api.add_resource(Employee, "/employee/<string:name>")
 
app.run(debug=True)