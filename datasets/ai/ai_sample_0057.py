import requests
from bs4 import BeautifulSoup
 
# Make a GET request to fetch the raw HTML content
html_content = requests.get('http://web-store.com').text
 
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
 
# Get the product data
products = soup.find_all('div', attrs={"itemprop": "product"})
for product in products:
    name = product.find("span", attrs={"itemprop": "name"}).text
    price = product.find("span", attrs={"itemprop": "price"}).text
    description = product.find("span", attrs={"itemprop": "description"}).text
    print(name, price, description)