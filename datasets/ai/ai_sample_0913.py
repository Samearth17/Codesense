import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.example.com'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
total_words = 0

for link in soup.find_all('a'):
    new_url = link.get('href')
    new_html = urllib.request.urlopen(url + new_url).read()
    soup2 = BeautifulSoup(new_html, 'html.parser')

    words = soup2.get_text().split(' ')
    total_words += len(words)

print(total_words)