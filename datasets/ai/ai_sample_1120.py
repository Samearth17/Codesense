import requests
from bs4 import BeautifulSoup

# Make the request
url = '<URL HERE>'
resp = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(resp.text, 'html.parser')

# Get all product prices
prices = soup.find_all('span', 'price')

# Extract the prices
product_prices = []
for price in prices:
 product_prices.append(price.text)

# Print the prices
for price in product_prices:
 print(price)