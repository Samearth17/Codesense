import requests
from lxml import html
import openpyxl

# Setup the web page URL
url = 'https://example.com/data.html'

# Scrape the web page
response = requests.get(url)
html_data = html.fromstring(response.text)

# Create an Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Read the data from the web page and store it in the workbook
data_table = html_data.xpath('//table')
for i, row in enumerate(data_table[0].xpath('./tbody/tr'), 1):
 for j, cell in enumerate(row.xpath('./td'), 1):
 sheet.cell(row=i, column=j, value=cell.text_content().strip())

# Save the workbook
wb.save("data.xlsx")