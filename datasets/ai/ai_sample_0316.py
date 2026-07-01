from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/calculate_average', methods=['POST'])
def calculate_average():
 numbers = request.json['numbers']

 # calculate the sum
 total = 0
 for number in numbers:
 total += number

 # calculate the average
 average = total / len(numbers)

 return jsonify({'average': average})

if name == 'main':
 app.run(debug=True)