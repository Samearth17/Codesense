import requests
from bs4 import BeautifulSoup

# get the html from the website
url = "https://www.example.com/stocks"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# find all table rows
table_rows = soup.find_all('tr')

# iterate through each table row
for row in table_rows:
 # get the table data
 stock_data = row.find_all('td')

 # extract the data from each table data element
 stock_symbol = stock_data[0].text
 stock_name = stock_data[1].text
 stock_price = stock_data[2].text

 # Print the data
 print("Stock Symbol:", stock_symbol)
 print("Stock Name:", stock_name)
 print("Stock Price:", stock_price)