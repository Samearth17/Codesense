import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# query the database
c.execute('SELECT * FROM users LIMIT 5')

# fetch all records
records = c.fetchall()

# print all records
for record in records:
  print(record)

# close the connection
conn.close()