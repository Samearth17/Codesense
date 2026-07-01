import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
host="localhost",
user="yourusername",
passwd="yourpassword",
database="user_db"
)

# Get the cursor
my_cursor = mydb.cursor()

# Execute the query
query = 'SELECT * FROM users'
my_cursor.execute(query)

# Get the results
result = my_cursor.fetchall()

# Print the results
for row in result:
 print(row)