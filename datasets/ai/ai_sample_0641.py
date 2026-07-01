import sqlite3

# Connect to database
conn = sqlite3.connect('my_database.db')

# Get cursor
c = conn.cursor()

# Print information about all tables
c.execute("SELECT name FROM sqlite_master WHERE type='table'")

print("List of tables:")
tables = c.fetchall()

for table in tables:
 print('\t',table[0])

# Close connection
conn.close()