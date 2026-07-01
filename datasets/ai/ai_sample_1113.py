#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/unique_count', methods=['POST'])
def unique_count():
 user_text = request.form['user_text']
 # Count number of unique characters
 characters = set()
 for char in user_text:
  characters.add(char)
 char_count = len(characters)
 # Render the count result
 return render_template('result.html', char_count=char_count)

if __name__ == '__main__':
app.run(debug=True)