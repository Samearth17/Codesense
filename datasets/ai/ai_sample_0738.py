import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_list = []
for price in soup.find_all('span', class_='price'):
    price_list.append(price.text)

print(price_list)