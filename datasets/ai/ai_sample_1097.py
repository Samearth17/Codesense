import csv

# Define function
def generate_report(file):
  # Initialize variables
  start_date = ""
  end_date = ""
  opening_price = 0
  closing_price = 0
  high_price = 0
  low_price = 1000000

  # Open the file and read the data into a list
  f = open(file)
  csv_reader = csv.reader(f)
  rows = list(csv_reader)

  # Loop through the list
  for row in rows[1:]:
    # Get the date and price data
    date = row[0]
    price = float(row[1])

    # Set start and end date
    if start_date == "":
      start_date = date
    end_date = date

    # Set opening and closing prices
    if opening_price == 0:
      opening_price = price
    closing_price = price

    # Set high and low prices
    if price > high_price:
      high_price = price
    if price < low_price:
      low_price = price
  
  # Calculate average price
  average_price = (high_price + low_price) / 2

  # Return results
  report = [start_date, end_date, opening_price, closing_price, high_price, low_price, average_price]
  return report

# Call the function
results = generate_report('stock_data.csv')
print(results)