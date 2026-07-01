from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def calc_sum_average():
  json_data = request.get_json()
  numbers = json_data.get('numbers')
  sum = 0
  for x in numbers:
    sum += x

  average = sum / float(len(numbers))
  result = {'sum' :sum, 'average': average}
  return json.dumps(result)
  
if __name__ == '__main__':
  app.run(debug=True)