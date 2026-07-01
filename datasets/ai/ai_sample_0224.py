import requests
import json
import sqlite3

# Make a GET request to the API
response = requests.get(url)
data = response.json()

# Save the data to a database
conn = sqlite3.connect('data.db')
c = conn.cursor()
for item in data:
    c.execute("INSERT INTO items VALUES (?, ?)", (item['id'], item['name']))
conn.commit()
conn.close()