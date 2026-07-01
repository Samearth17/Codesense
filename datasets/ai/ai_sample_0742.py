# imports
from flask import Flask, jsonify, request

# setting up the application
app = Flask(__name__)

# defining the data
blog_posts = [
 {
 'id': '1',
 'title': 'Introducing my blog',
 'content': 'This blog is all about my journey as a software developer.'
 },
 {
 'id': '2',
 'title': 'My First day',
 'content': 'Today I created a website and wrote a few lines of code!'
 }
]

# routes
@app.route('/posts', methods=['GET'])
def get_all_posts():
 return jsonify({'posts': blog_posts})

@app.route('/posts/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
 post = next((item for item in blog_posts if item['id'] == post_id), None)
 return jsonify({'post': post})

@app.route('/posts', methods=['POST'])
def create_post():
 data = request.get_json()
 blog_posts.append(data)
 return jsonify({'posts': blog_posts})

@app.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
 data = request.get_json()
 for item in blog_posts:
 if item['id'] == data['id']:
 item['title'] = data['title']
 item['content'] = data['content']
 return jsonify({'posts': blog_posts})

@app.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
 data = request.get_json()
 for item in blog_posts:
 if item['id'] == data['id']:
 blog_posts.remove(item)
 return jsonify({'posts': blog_posts})

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8000)