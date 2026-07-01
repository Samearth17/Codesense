import requests
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.bbc.co.uk/news/business/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for link in soup.find_all('a'):
    # Get the text of the link
    headline = link.get('title')
    if headline is not None and headline != "":
        print(headline)