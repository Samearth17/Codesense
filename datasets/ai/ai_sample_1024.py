import requests 
from bs4 import BeautifulSoup

# URL of the site to scrape
url = 'https://www.example.com'

# Send the request to the URL
response = requests.get(url)

# Parse the html content
html_soup = BeautifulSoup(response.text, 'html.parser')

# Get all of the <div> elements with a class of 'content'
content = html_soup.find_all('div', class_ = 'content')

# Iterate over the content and print out the text
for item in content:
 print(item.text.strip())