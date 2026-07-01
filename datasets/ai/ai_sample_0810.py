import requests
from bs4 import BeautifulSoup

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Get all the comments of the HTML document
comments = soup.find_all('div', attrs={'class': 'comments'})

# Store the comments in a list
comment_list = []
for comment in comments:
    comment_list.append(comment.text)