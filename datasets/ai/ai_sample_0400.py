from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Book(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 title = db.Column(db.String(80), unique=True)
 author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
 publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

class Author(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(80), unique=True)

class Publisher(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(80), unique=True)

db.create_all()

if __name__ == '__main__':
 app.run(debug=True)