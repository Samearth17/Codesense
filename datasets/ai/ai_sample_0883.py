import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response  = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

all_articles = soup.findAll("div", {"class": "css-1l4spti"})

for article in all_articles:
    title = article.find("h2").text
    published_date = article.find("time")["datetime"]
    
    print(title)
    print(published_date)