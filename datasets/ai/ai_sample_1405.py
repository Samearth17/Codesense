import yfinance as yf

# Get stock data
tsla = yf.Ticker("TSLA")

# Get maximum stock price
max_price = max(tsla.history(period="1d")["Close"])

# Get opening stock price
open_price = tsla.history(period="1d")["Open"][0]

# Print whether it closed higher or lower
if max_price > open_price:
 print("TSLA closed higher than its opening price.")
else:
 print("TSLA closed lower than its opening price.")