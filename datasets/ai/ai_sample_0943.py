import requests
import json

def get_stock_price(ticker):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey=<Your_API_KEY>'.format(ticker=ticker)
    response = requests.get(url)
    data = json.loads(response.text)
    if data:
        ts = data['Time Series (1min)']
        latest_data_point = list(ts.values())[0]
        return latest_data_point['4. close']

if __name__ == '__main__':
    g_price = get_stock_price('GOOGL')
    m_price = get_stock_price('MSFT')
    print(f'Google stock price: {g_price}')
    print(f'Microsoft stock price: {m_price}')