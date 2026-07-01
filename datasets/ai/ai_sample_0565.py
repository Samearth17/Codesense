import requests
from bs4 import BeautifulSoup

# Get the page
url = <provided_url>
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.text, ‘html.parser’)

# Find all links
links = []
for link in soup.find_all(‘a’):
    links.append(link.get(‘href’))

# Print out the list of links
for link in links:
    print(link)