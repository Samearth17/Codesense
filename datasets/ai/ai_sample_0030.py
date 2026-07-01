from flask import Flask, request
import json

app = Flask(__name__)
items = ["Apple", "Banana", "Orange"]

@app.route('/items', methods=["GET"])
def get_items():
 return json.dumps(items)

@app.route('/items/<item>', methods=["DELETE"])
def delete_item(item):
 if item in items:
  items.remove(item)
  message = "Item successfully deleted."
 else:
  message = "Item not found."
 return json.dumps({"message": message})