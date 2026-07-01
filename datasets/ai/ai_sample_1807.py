# Store API
# app.py
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

products = [
    {"name": "laptop", "category": "electronics", "price": 899.99},
    {"name": "iphone", "category": "electronics", "price": 999.99},
    {"name": "headphones", "category": "electronics", "price": 99.99}
]

# product
class Product(Resource):
    def get(self, name):
        for product in products:
            if name == product['name']:
                return product, 200
        return {"message": "Product not found"}, 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        parser.add_argument('price')
        args = parser.parse_args()

        for product in products:
            if product['name'] == name:
                return {"message": "Product with name {} already exists".format(name)}, 400

        product = {
            "name": name, 
            "category": args['category'],
            "price": args['price']
        }
        products.append(product)
        return products[-1], 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        parser.add_argument('price')
        args = parser.parse_args()

        for product in products:
            if product['name'] == name:
                product['category'] = args['category']
                product['price'] = args['price']
                return product, 200
        return {"message": "Product not found"}, 404

# products
class ProductList(Resource):
    def get(self):
        return products, 200

api.add_resource(Product, "/product/<string:name>")
api.add_resource(ProductList, "/products")

if __name__ == '__main__':
    app.run(debug=True)