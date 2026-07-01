import requests
from bs4 import BeautifulSoup

# input
stocks = ["AAPL stocks", "MSFT stocks", "FB stocks", "GOOG stocks"]

# process
def get_stock_price(stock):
    url = f"https://finance.yahoo.com/quote/{stock}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

# output
for stock in stocks:
    price = get_stock_price(stock)
    print(f'The price of {stock} is {price}.')