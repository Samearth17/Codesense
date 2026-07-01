import requests 
from bs4 import BeautifulSoup 
  
# URL to scrap 
URL = 'http://example.com/news'
  
# get the source code 
html_content = requests.get(URL).text 
  
# parse the html content 
soup = BeautifulSoup(html_content, "lxml") 
  
# get all the articles  
articles = soup.find_all('article') 
  
# print the first 10 articles 
for article in articles[:10]: 
    print(article.text)