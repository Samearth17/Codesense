import requests
from bs4 import BeautifulSoup

# Make a GET request to fetch the raw HTML content
html_content = requests.get('http://www.example.com').text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Scrape the content
content = soup.p

# Save the content in a text file
with open('content.txt', 'w') as file:
    file.write(content)