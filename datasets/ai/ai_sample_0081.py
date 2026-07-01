from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///test.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200))
  content = db.Column(db.Text)

  def __repr__(self):
    return '<BlogPost %r>' % self.title

@app.route('/post', methods=['POST'])
def create_post():
  data = request.get_json()
  post = BlogPost(title=data['title'], content=data['content'])
  db.session.add(post)
  db.session.commit()
  return jsonify(post.id)

@app.route('/posts', methods=['GET'])
def get_posts():
  posts = BlogPost.query.all()
  return jsonify([post.serialize() for post in posts])

@app.route('/post/<id>', methods=['GET'])
def get_post(id):
  post = BlogPost.query.filter_by(id=id).first()
  return jsonify(post.serialize())

@app.route('/post/<id>', methods=['PUT'])
def edit_post(id):
  data = request.get_json()
  post = BlogPost.query.filter_by(id=id).first()
  post.title = data['title']
  post.content = data['content']
  db.session.commit()
  return jsonify(post.serialize())

@app.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
  post = BlogPost.query.filter_by(id=id).first()
  db.session.delete(post)
  db.session.commit()
  return jsonify({ 'message' : 'Post deleted' })

if __name__ == '__main__':
  app.run(debug=True)