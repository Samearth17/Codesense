from flask import Flask, jsonify, request
 
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_all_products():
    # query database
    products = []
    # format result
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # query database
    product = {}
    # format result
    return jsonify(product)

@app.route('/products', methods=['POST'])
def create_product():
    # get data from request
    data = request.get_json()
    # save to database
    # format result
    return jsonify({'message': 'Product added successfully.'}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # get data from the request
    data = request.get_json()
    # update data in the database
    # format the result
    return jsonify({'message': 'Product successfully updated.'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # delete data from the database
    # format the result
    return jsonify({'message': 'Product successfully deleted.'})