"""
Scrape the current market price of Twitter stock and store the data into a MongoDB database
"""

import requests 
from pymongo import MongoClient 

def get_price(stock_name):
    # request the data 
    response = requests.get(f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}") 
    # parse the response 
    data = response.json() 
    # get the price 
    return data['chart']['result'][0]['meta']['regularMarketPrice'] 

if __name__ == "__main__":
    # connect to the MongoDB database 
    client = MongoClient() 
    db = client['stocks']
    # get the stock name from user
    stock_name = input("Stock Name: ").upper() 
    # get the stock price 
    price = get_price(stock_name) 
    # store the data into MongoDB   
    db.stocks.insert_one({'stock':stock_name, 'price':price}) 
    print('Data stored successfully!')