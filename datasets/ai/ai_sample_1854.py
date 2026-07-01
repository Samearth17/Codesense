import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient("mongodb://localhost:27017")

# declare the database
db = client.stock_prices

# name the collection
collection = db.nasdaq

# get the data 
response = requests.get("https://www.nasdaq.com/symbol/aapl")

# parse it
soup = BeautifulSoup(response.text, 'html.parser')

# get the table 
table = soup.find('table', {'class': 'genTable'})

# get each row
for tr in table.find_all('tr')[1:]:
  # get each column
  td = tr.find_all('td')
  # data manipulation 
  date = td[0].text
  open_price = float(td[1].text)
  high_price = float(td[2].text)
  low_price = float(td[3].text)
  close_price = float(td[4].text)

  # define the document 
  doc = {
    'date': date,
    'open_price': open_price,
    'high_price': high_price,
    'low_price': low_price,
    'close_price': close_price
  }
  
  # insert
  collection.insert_one(doc)