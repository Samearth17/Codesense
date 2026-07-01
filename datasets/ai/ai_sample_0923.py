from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__) # create a Flask app
api = Api(app) # initialize Flask-RESTplus

# This is a dummy list of user posts.
# In a real application these would
# be pulled from a database.
posts = [
 {'user_id': 123, 'title': 'My post 1', 'content': 'Lorem ipsum dolor sit amet...'},
 {'user_id': 123, 'title': 'My post 2', 'content': 'Lorem ipsum dolor sit amet...'},
 {'user_id': 123, 'title': 'My post 3', 'content': 'Lorem ipsum dolor sit amet...'},
]

@api.route('/posts')
class Posts(Resource):
 def get(self):
 user_id = request.args.get('user_id')
 posts = [post for post in posts if post['user_id'] == user_id]
 return posts

if __name__ == '__main__':
 app.run(debug=True)