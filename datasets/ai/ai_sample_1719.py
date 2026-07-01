import requests
from bs4 import BeautifulSoup
import json
 
url = '<Your URL>'
 
# Get the page
page = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')
 
# Scrape the content
data = {
 'title': soup.find(id='firstHeading').text,
 'content': soup.find(id='mw-content-text').text
}
 
# Save as JSON
with open('data.json', 'w') as outfile:
   json.dump(data, outfile)