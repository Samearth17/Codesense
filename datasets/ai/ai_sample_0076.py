The web scraper should utilize the Python package BeautifulSoup to parse webpages and extract the required data. BeautifulSoup will allow us to find HTML elements on the webpage using tags and attributes. Once the data is found, it can be converted into the desired format and stored.

For example, to extract the URL from a list of webpages, the following code snippet can be used:

import requests
from bs4 import BeautifulSoup

# Get the web page
webpage = requests.get("<url_of_webpage>")

# Parse the web page
soup = BeautifulSoup(webpage.content, 'html.parser')

# Find all 'a' tags
links = soup.find_all('a')

# Extract the URLs in the 'href' attribute
for link in links:
    print(link.get('href'))