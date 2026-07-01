import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

urls = []

for link in soup.find_all('a', href=True):
 if link['href'].startswith('http'):
 urls.append(link['href'])

print(urls)