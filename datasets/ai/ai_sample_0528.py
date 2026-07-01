import requests
from bs4 import BeautifulSoup

url = 'http://example.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
for li in soup.find_all('li'):
    data.append({
        'name': li.text.split(":")[0],
        'value': li.text.split(":")[1]
    })

print(data)
# Output: [{'name': 'Name', 'value': 'John Smith'}, {'name': 'Age', 'value': '38'}]