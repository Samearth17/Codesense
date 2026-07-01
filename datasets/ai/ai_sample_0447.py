import json

from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
 {
  "name": "book",
  "price": 15
 }, 
 {
  "name": "pen",
  "price": 5
 }, 
 {
  "name": "tablet",
  "price": 200
 }, 
 {
  "name": "chair",
  "price": 80
 }
]

@app.route("/top_three_products", methods=["GET"])
def get_top_three_products():
   # Sort the list of products by price in descending order
   sorted_products = sorted(products, key=lambda product: -product['price'])
   # Return only the top 3 products
   highest_priced_products = sorted_products[:3]
   return jsonify(highest_priced_products)

if __name__ == "__main__":
    app.run()