import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = "http://www.example.com"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Scrape data from the HTML using beautiful soup
data = soup.find_all('p')

# Print the scraped data
for item in data:
 print(item.text)