# Import the necessary modules
from flask import Flask, request
import sqlite3

# Create the Flask application
app = Flask(__name__)

# Establish a connection to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a function to delete a record
@app.route('/delete_record/<int:id>', methods=['DELETE'])
def delete_record(id):
    c.execute("DELETE FROM records WHERE rowid = ?", (id,))
    conn.commit()
    return "Record deleted successfully"

if __name__ == '__main__':
    app.run(debug=True)