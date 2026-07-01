import requests
from bs4 import BeautifulSoup

def webcrawler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for url in soup.find_all('a'):
        url = url.get('href')
        if url is not None and url not in visited:
            visited.add(url)
            print(url)
            webcrawler(url)
            
webcrawler('https://www.example.com')