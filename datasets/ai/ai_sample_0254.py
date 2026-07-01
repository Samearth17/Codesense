import requests
from bs4 import BeautifulSoup

url = 'http://www.example.com'

# Use requests to get website HTML
resp = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')

# Extract data from HTML
data = []
for item in soup.find_all('div'):
 data.append(item.text)

# Print the data
for d in data:
 print(d)