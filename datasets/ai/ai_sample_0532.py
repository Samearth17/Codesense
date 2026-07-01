import requests
from bs4 import BeautifulSoup

# Website URL
url = 'LINK'
 
# Make a request and get the HTML content
r = requests.get(url) 
html_content = r.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Price
price_tag = soup.find(class_='price')
price = price_tag.text

# Description
description_tag = soup.find(class_='product-description')
description = description_tag.text

print('Price:', price)
print('Description:', description)