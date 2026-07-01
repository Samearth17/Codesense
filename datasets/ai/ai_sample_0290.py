import requests
from bs4 import BeautifulSoup

def get_keywords_from_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    keywords = soup.find('meta', attrs={'name':'keywords'})
    if keywords:
        return keywords['content']
    else:
        return ""

# Optimize search queries by finding keywords from a given website
def optimize_query(url):
    keywords = get_keywords_from_page(url)
    if keywords:
        return keywords
    else:
        return url