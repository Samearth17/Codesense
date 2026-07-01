import requests
from bs4 import BeautifulSoup

urls = [
 'https://www.amazon.com/Cup-Stars-Novel-Alex-Awards-ebook/dp/B07PWNWS3G',
 'https://www.amazon.com/Life-Will-Dark-Novel/dp/B07KY7P1SR'
]

for url in urls:
 page = requests.get(url)
 soup = BeautifulSoup(page.content, 'html.parser')
 
 title = soup.find(id="productTitle").get_text()
 author = soup.find(class_="author notFaded").get_text()
 
 print('Title: ', title)
 print('Author: ', author)