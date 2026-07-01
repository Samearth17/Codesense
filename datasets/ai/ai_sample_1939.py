from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
 return 'Welcome to the API'

@app.route('/data', methods=['POST'])
def add_data():
 data = request.get_json()
 # Do something with data

 return jsonify({'message': 'Data added successfully'})

@app.route('/data/int:id', methods=['GET'])
def get_data(id):
 data = # Retrieve data from database
 return jsonify({'data': data})

if __name__ == '__main__':
 app.run()