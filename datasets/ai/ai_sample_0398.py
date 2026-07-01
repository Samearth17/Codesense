import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get articles
articles = soup.find_all('article')

# Download the articles
for article in articles:
    article_url = article.find('a')['href']
    article_response = requests.get(article_url)
    with open(article_url.split('/')[-1], 'wb') as f:
        f.write(article_response.content)