import requests
from bs4 import BeautifulSoup

url = 'https://example.com/articles.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# get the title
title = soup.find("h1", class_="article-title")
title_text = title.text.strip()

# get the date
date = soup.find("div", class_="article-date")
date_text = date.text

# get the article text
text = soup.find("div", class_="article-text")
text_text = text.text.strip()
 
 # save the information in the file
with open('article.txt', 'w') as file:
 file.write(title_text+'\n')
 file.write(date_text+'\n')
 file.write(text_text)