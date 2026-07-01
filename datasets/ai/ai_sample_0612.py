import mysql.connector

# Connect to local MySQL Server
conn = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='test'
)
cursor = conn.cursor()

# Execute SQL Query
sql = "SELECT * FROM users"
cursor.execute(sql)

# Fetch and print results
data = cursor.fetchall()
for record in data:
    print(record)