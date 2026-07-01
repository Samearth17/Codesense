# imports
from flask import Flask, render_template, request

# init app
app = Flask(__name__)

# set route
@app.route('/', methods=['POST', 'GET'])
def index():
 if request.method == 'POST':
  data = request.form['data']
  counts = {}
  for char in data:
   if char in counts:
    counts[char] += 1
   else:
    counts[char] = 1
  
  return render_template('index.html', counts=counts)
 else:
  return render_template('index.html')

# run app 
if __name__ == '__main__':
 app.run(debug=True)

And for the index.html template:
<html>
 <head>
  <title>Letter Counter</title>
 </head>
 <body>
  <h1>Letter Counter</h1>
  <form method="POST">
   <input type="text" name="data">
   <input type="submit" value="Submit">
  </form>
 
  {% if counts %}
   <h2>Results</h2>
   {% for key, val in counts.items() %}
    <p>{{ key }}: {{ val }}</p>
   {% endfor %}
  {% endif %}
 </body>
</html>