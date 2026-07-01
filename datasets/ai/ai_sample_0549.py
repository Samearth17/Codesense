import requests
from bs4 import BeautifulSoup

# Fetch HTML page
response = requests.get('http://example.com/table.html')

# Create BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Extract table
table = soup.find('table')

# Extract columns
columns = [col.text for col in table.find_all('td')]

# Extract rows
rows = [row.find_all('td') for row in table.find_all('tr')]

# Iterate over each row and store data in a dict
data = []
for row in rows:
     data.append([col.text for col in row])

# Print the data
print(data)
# [['Name', 'Email'], ['John Doe', 'john@example.com']]