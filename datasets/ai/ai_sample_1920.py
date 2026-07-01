import requests
import sqlite3

# Connect to the database
conn = sqlite3.connect('urls.db')
c = conn.cursor()

# Scrape the website
r = requests.get('http://example.com')

# Extract all URLs from the webpage
links = r.html.absolute_links

# Insert the URLs into the database
for link in links:
 c.execute("INSERT INTO urls VALUES (?)", (link,))

# Save changes to the database
conn.commit() 
conn.close()