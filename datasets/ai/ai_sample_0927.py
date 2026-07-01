import flask from flask
import sqlite3

app = flask.Flask(__name__)

# create the database
conn = sqlite3.connect('data.db')
cur = conn.cursor()

# create the table for your data
cur.execute('''CREATE TABLE IF NOT EXISTS search 
(query TEXT, results TEXT)''')

@app.route('/search', methods = ['GET', 'POST'])
def search():
 if flask.request.method == 'POST':
 # get the search term from the form
 query = flask.request.form['query']

 # search the database for the query
 cur.execute('''SELECT results FROM search 
 WHERE query=?''', (query,))
 results = cur.fetchall()

 # return the results
 return flask.render_template('results.html', 
query = query, results = results)

# the search form
@app.route('/')
def index():
 return flask.render_template('search.html')

if __name__ == '__main__':
 app.run(debug = True)