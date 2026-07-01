# importing libraries
import requests
from bs4 import BeautifulSoup

# making the request
url = "https://www.example.com/products"
r = requests.get(url)

# extracting the data with BeautifulSoup
soup = BeautifulSoup(r.content)
products = soup.find_all("div", {"class": "product"})

for product in products:
    product_name = product.find("h3").text
    product_price = product.find("span", {"class": "price"}).text
    print("Found product: %s %s" % (product_name, product_price))