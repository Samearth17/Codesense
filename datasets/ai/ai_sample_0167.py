import datetime, pyodbc

# Establish a connection to the database
conn = pyodbc.connect("<connection details>")
cursor = conn.cursor()

# Get the year of the order date
sql = "SELECT * FROM orders"
query_date = datetime.date.today().year
where_clause = "WHERE YEAR(order_date) = ?"

# Execute the query
cursor.execute(sql + " " + where_clause, query_date)
results = cursor.fetchall()

# Output the results
for result in results:
    print(result)