from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(name)
mongo = PyMongo(app)
 
@app.route('/products', methods=['POST'])
def add_product():
 data = request.get_json()
 mongo.db.products.insert_one(data)
 return jsonify({'message': 'Product added successfully!'})
 
@app.route('/products/int:pid', methods=['GET'])
def get_product(pid):
 product = mongo.db.products.find_one({'pid': pid})
 return jsonify(product)