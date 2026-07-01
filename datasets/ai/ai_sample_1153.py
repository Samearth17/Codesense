import requests 
import sqlite3 

# Define the API endpoint 
API_ENDPOINT = "http://example.com/api"

# Connect to the Database 
conn = sqlite3.connect('MyData.db')
c = conn.cursor()

# Make sure we have the right schema 
c.execute("CREATE TABLE IF NOT EXISTS data (data TEXT)")

# Fetch the data from the API 
r = requests.get(API_ENDPOINT)
data = r.json()

# Save the data to the Database 
c.execute("INSERT INTO data VALUES (?)", (data,))
conn.commit()

# Close the connection 
conn.close()