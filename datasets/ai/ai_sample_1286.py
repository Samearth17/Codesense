import sqlite3
from flask import Flask, jsonify, request, abort

# Initial setup of a Flask application
app = Flask(__name__)
conn = sqlite3.connect('movies.db')

# SQL queries
# 1 - Create the tables in Database
sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
 id integer PRIMARY KEY,
 title text NOT NULL
); """

sql_create_actors_table = """CREATE TABLE IF NOT EXISTS actors (
 id integer PRIMARY KEY,
 name text NOT NULL,
 movie_id integer NOT NULL,
 FOREIGN KEY (movie_id) REFERENCES movies (id)
);"""

# 2 - Create two functions to insert Movie and Actor information into the Database
def create_new_movie(title):
 with conn:
 cur = conn.cursor()
 cur.execute("INSERT INTO movies (title) VALUES (?)", (title,))
 return cur.lastrowid

def create_new_actor(name, movie_id):
 with conn:
 cur = conn.cursor()
 cur.execute("INSERT INTO actors (name, movie_id) VALUES (?,?)", (name, movie_id))
 return cur.lastrowid

# 3 - Create a function to get a list of movies
def get_all_movies():
 cur = conn.cursor()
 cur.execute("SELECT * FROM movies")
 rows = cur.fetchall()
 return rows

# 4 - Create a function to get a list of actors for a given movie
def get_all_actors(movie_id):
 cur = conn.cursor()
 cur.execute("SELECT * FROM actors WHERE movie_id=?", (movie_id))
 rows = cur.fetchall()
 return rows

# 5 - Create two endpoints (POST and DELETE) to modify the actors of the movie
@app.route('/movies/<int:movie_id>/actors', methods=['POST'])
def add_actor(movie_id):
 error = None
 if not request.json:
 abort(400)
 if 'name' not in request.json:
 abort(400)
 if 'movie_id' not in request.json:
 abort(400)

 name = request.json['name']
 movie_id = request.json['movie_id']
 
 try:
 actor_id = create_new_actor(name, movie_id)
 return jsonify({'actor_id': actor_id}), 201
 except:
 error = 'Error inserting actor into the database.'

 return jsonify({'error': error}), 500

@app.route('/movies/<int:movie_id>/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(movie_id, actor_id):
 with conn:
 cur = conn.cursor()
 cur.execute("DELETE FROM actors WHERE id=?", (actor_id,))
 rows = cur.fetchall()
 return jsonify({'result': True})

if __name__ == '__main__':
 # Create tables
 conn.execute(sql_create_movies_table)
 conn.execute(sql_create_actors_table)
 # Run the applications
 app.run()