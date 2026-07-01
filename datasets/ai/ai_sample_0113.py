from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

app = Flask(name)
api = Api(app)

# Setup JWT authentication
app.secret_key = 'super-secret-key'
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
 @jwt_required()
 def get(self, name):
 for item in items:
 if item['name'] == name:
 return item
 return {'item': None}, 404

 def post(self, name):
 new_item = {'name': name, 'price': 12.00}
 items.append(new_item)
 return new_item, 201


class ItemList(Resource):
 def get(self):
 return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if name == 'main':
 app.run(port=5000, debug=True)