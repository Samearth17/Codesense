"""
Construct a web crawler in Python to retrieve the URL of all the articles posted on a given page
"""

import requests
from bs4 import BeautifulSoup

def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    articles = set()
    for article in soup.find_all('a', attrs={'class':'article-link'}):
        articles.add(article['href'])
    return articles

if __name__ == '__main__':
    url = 'https://www.example.com/'
    print(get_urls(url))