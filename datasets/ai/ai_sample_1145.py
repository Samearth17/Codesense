import sqlite3

# Create database
db = sqlite3.connect('test.db')

c = db.cursor() 
    
# Create table
c.execute('DROP TABLE IF EXISTS person')

c.execute('''
        CREATE TABLE person(
        name TEXT,
        age INTEGER,
        address TEXT
        )
        ''')