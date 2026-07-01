from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self, userId):
        # return user object with userId
        pass

    def post(self):
        # create new user
        pass

    def put(self, userId):
        # update user object with userId
        pass

    def delete(self, userId):
        # delete user object with userId
        pass

class Courses(Resource):
    def get(self,courseId):
        # return course object with courseId
        pass

    def post(self):
        # create new course
        pass

    def put(self,courseId):
        # update course object with courseId
        pass

    def delete(self,courseId):
        # delete course object with courseId
        pass

class Grades(Resource):
    def get(self,courseId):
        # return grade object with courseId
        pass

    def post(self):
        # create new grade
        pass

    def put(self,courseId):
        # update grade object with courseId
        pass

    def delete(self,courseId):
        # delete grade object with courseId
        pass

api.add_resource(Users, '/users/<userId>')
api.add_resource(Courses, '/courses/<courseId>')
api.add_resource(Grades, '/courses/<courseId>/grades')

if __name__ == '__main__':
    app.run(debug=True)