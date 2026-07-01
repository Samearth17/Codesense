import requests
import bs4
 
# Make the request
url = 'https://example.com/store'
response = requests.get(url)
 
# Create the soup object
soup = bs4.BeautifulSoup(response.text, 'html.parser')
 
# Extract the prices
prices = []
for item in soup.find_all('div', {'class': 'product'}):
    price = item.find('div', {'class': 'price'}).text
    prices.append(price)
 
print(prices)