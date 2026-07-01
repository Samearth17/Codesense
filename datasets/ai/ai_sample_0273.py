from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def math():
 if request.method == 'POST':
  num1 = int(request.form.get('num1'))
  num2 = int(request.form.get('num2'))
  operation = request.form.get('operation')

  if operation == 'add':
   result = num1 + num2
  elif operation == 'subtract':
   result = num1 - num2

  return {'result': result}

if __name__ == '__main__':
 app.run(debug=True)