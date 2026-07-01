"""
Script to scrape photos and captions from a given website
"""

from bs4 import BeautifulSoup
import requests

# Get the HTML source code
url = 'https://example.com/webpage'
req = requests.get(url)
html = req.text

# Parse HTML source and extract photo and caption
soup = BeautifulSoup(html, features='lxml')
image_divs = soup.find_all('div', {'class': 'image-gallery__image'})

for image_div in image_divs:
    figure = image_div.find('figure')
    src = figure.find('img')['src']
    caption = figure.find('figcaption')
    print('Photo: ', src)
    if caption:
        print('Caption: ', caption.text)
    else:
        print('No caption')
    print('\n')