import os
from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class SearchBooks(Resource):
 def get(self):
 query = request.args.get('q') 
 
 books = find_books(query) 
 
 return {'results': books}

api.add_resource(SearchBooks, '/search')

if __name__ == '__main__':
 app.run()

def find_books(term):
 # code for searching library here
 return []