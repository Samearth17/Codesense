import requests
from bs4 import BeautifulSoup

url = "http://example.com"

# Get the HTML page
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Get all elements with the class "article-title"
titles = soup.find_all(class_="article-title")

# Store the titles in a list
titles_list = []
for title in titles: 
    titles_list.append(title.text)

# Print out the titles
for title in titles_list:
    print(title)