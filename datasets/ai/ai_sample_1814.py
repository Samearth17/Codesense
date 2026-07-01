import urllib.request
from bs4 import BeautifulSoup

# target url
url = 'https://www.example.com/'

# create request and obtain html
page = urllib.request.urlopen(url)
html_doc = page.read()

soup = BeautifulSoup(html_doc, 'html.parser')
keywords = soup.find_all(string = lambda text: keyword in text)

# print all sites containing the given keyword
for keyword in keywords:
 print(keyword)