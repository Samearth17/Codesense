import flask
from flask import request, jsonify

# Creating the application app
app = flask.Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the input data from the user
    data = request.get_json()

    age = data['age']
    gender = data['gender']
    car_model = data['car_model']

    # Calculate the insurance price
    # ...
    insurance_price = 0.00

    # Return the calculated insurance price in JSON format
    return jsonify({'insurance_price': insurance_price})
	
app.run(host='0.0.0.0', port=8006)