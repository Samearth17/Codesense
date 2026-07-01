from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_wikipedia_page(url):
    # Retrieve the page
    html = urlopen(url)

    # Create an instance of the bs4 parser
    soup = BeautifulSoup(html, 'html.parser')

    # Extract content from the page
    page_content = soup.find_all('p')
    page_content_str = ''.join(str(p) for p in page_content)

    return page_content_str

page_content_str = scrape_wikipedia_page('https://en.wikipedia.org/wiki/Machine_learning')
print(page_content_str)