import requests
from bs4 import BeautifulSoup

# Set the base URL
url = "https://www.example.com"

# Keep track of visited URLs
visited = set()

# Set of external URLs
urls_external = set()

# Perform the crawl
def crawl():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    internal_urls = set()

    # Find all links on the page
    for link in soup.find_all('a'):
        if url.startswith(url):
            internal_urls.add(link['href'])
        else:
            urls_external.add(link['href'])
    
    # Recursively crawl all internal URLs
    for internal_url in internal_urls:
        if internal_url not in visited:
            visited.add(internal_url)
            crawl(internal_url)

crawl()