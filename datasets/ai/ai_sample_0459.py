import sqlite3

# create database connection
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# create database table
c.execute('''CREATE TABLE users
       (name TEXT, age INTEGER, city TEXT)''')

# add user data
c.execute("INSERT INTO users VALUES ('John', 24, 'New York')")
c.execute("INSERT INTO users VALUES ('Thomas', 28, 'Chicago')")
c.execute("INSERT INTO users VALUES ('Emily', 32, 'Los Angeles')")

# save and close database connection
conn.commit()
conn.close()