import requests
from bs4 import BeautifulSoup

# Get HTML content from target website
r = requests.get('URL')
html_doc = r.text

# Create a beautiful soup object
soup = BeautifulSoup(html_doc)

# Find and extract desired data
data = soup.select('SELECTOR') 

# Print extracted data
for x in data: 
 print(x.text)