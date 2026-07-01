import requests
from bs4 import BeautifulSoup

def get_links(url):
    # Fetch the page
    res = requests.get(url)
    # Parse the HTML
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Extract all links from the page
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links