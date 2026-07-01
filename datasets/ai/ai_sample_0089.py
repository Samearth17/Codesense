from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
 name = request.form.get('name')
 email = request.form.get('email')
 phone = request.form.get('phone')
 
 conn = sqlite3.connect('data.db')
 cur = conn.cursor()
 
 cur.execute("INSERT INTO data (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
 conn.commit()
 
 return redirect('/')
	
if __name__ == '__main__':
 app.run(debug=True)