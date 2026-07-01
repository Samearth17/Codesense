from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def dialog():
 # Get the user's input from the request
 user_input = request.json['user_input']

 # Define a response based on the user's input
 if user_input == 'Hi':
 response = 'Hello there!'
 # Add additional actions here

 # Return the response as JSON
 return jsonify({'response':response})

if __name__ == '__main__':
 app.run(port=5000, debug=True)