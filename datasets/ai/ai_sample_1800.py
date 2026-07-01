import requests
from bs4 import BeautifulSoup
import json

url = 'http://example.com/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get the information
information = {}    
information['title'] = soup.title.string
information['h1'] = soup.h1.string
information['description'] = soup.find('meta', attrs={'name':'description'})['content']

# Save the information
with open('information.json', 'w') as f:
    json.dump(information, f)
print('Data saved!')