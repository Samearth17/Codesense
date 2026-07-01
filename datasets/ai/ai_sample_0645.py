import requests
from bs4 import BeautifulSoup

# Given a keyword and a website URL
def web_crawler(keyword, url):
    # Make a request to the given URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Loop through the pages
    visited = set()
    while True:
        # Get all the links on the page
        links = soup.find_all('a')
        for link in links:
            # Get the absolute URL for the link
            link_url = link.get('href')

            # If the URL is already visited, continue
            if link_url in visited:
                continue

            # If it is a valid URL, visit it
            if link_url.startswith('http'):
                visited.add(link_url)
                response = requests.get(link_url)
                soup = BeautifulSoup(response.content, 'html.parser')

                # Search for the keyword in the page
                if keyword in response.text:
                    print(f'Found keyword "{keyword}" in URL: {link_url}')

# Test
keyword = 'Python'
url = 'www.example.com'
web_crawler(keyword, url)