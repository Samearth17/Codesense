import requests
from bs4 import BeautifulSoup

# define url
url = "https://www.example.com/news"

# send GET request to the specified url
page = requests.get(url)

# create BeautifulSoup object for parsing
soup = BeautifulSoup(page.text, 'html.parser')

# extract all article titles, publication dates, and authors
items = soup.find_all('article')
for item in items:
    title = item.find('h2').text
    pub_date = item.find('time').text
    author = item.find('span').text
    print(title + ' | ' + pub_date + ' | ' + author)