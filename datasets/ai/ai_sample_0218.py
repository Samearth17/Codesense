from flask import Flask, jsonify, request

# Class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/', methods=['GET', 'POST'])
def index():

    # POST request
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            return jsonify({'message': 'No input data provided'}), 400
        user_name = json_data['name']
        user_email = json_data['email']
        user = User(name=user_name, email=user_email)

        return jsonify({
            'name': user.name,
            'email': user.email
        })
    
    # GET request
    if request.method == 'GET':
        # Get user list
        users = [user.__dict__ for user in users]
        return jsonify({'users': users}), 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)