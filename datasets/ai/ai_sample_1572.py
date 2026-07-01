import flask
from flask import request, jsonify
import matplotlib.pyplot as plt

# create the Flask app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# function to generate the pie chart
def generate_pie_chart(data):
 fig, ax = plt.subplots()
 ax.pie(data, labels=['1', '2', '4', '6'], autopct='%1.1f%%')
 ax.axis('equal') 
 return fig

# home route
@app.route('/', methods=['GET'])
def home():
 return '''<h1>Pie Chart Generator</h1>
 <p>A web service to generate pie chart from input data.</p>'''

# route to generate the pie chart
@app.route('/api/v1/generate_pie_chart', methods=['POST'])
def generate_pie_chart_route():
 # get the input data
 data = request.json['data']
 
 # generate the pie chart 
 fig = generate_pie_chart(data)
 
 # save the figure as a png image
 figure_file = 'figure.png'
 fig.savefig(figure_file)
 
 # read the pie chart image
 data = open(figure_file, 'rb').read()
 
 # return the chart as response
 return data

# run the app
if __name__ == '__main__':
 app.run(debug=True)