import requests
from bs4 import BeautifulSoup
url = "<website url>"

# Make request to website
r = requests.get(url)

# Get the HTML of the page
html = r.text

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract desired info from the page
data = soup.find_all('div', {'class': 'content'})

# Print the data
print(data)