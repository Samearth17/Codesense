import mysql.connector

# Connect to the database 
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    database="mydatabase"
)
# Create a cursor 
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT * FROM customers")

# Fetch all records 
records = mycursor.fetchall()

# Print records 
for record in records:
    print(record)