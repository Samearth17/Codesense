import requests
from bs4 import BeautifulSoup

# Fetch the website content
link = "https://example.com"
data = requests.get(link)

# Parse the HTML content
soup = BeautifulSoup(data.text, 'html.parser')

# Extract all the <p> tags
content = soup.find_all('p')

# Print the content
for item in content:
    print(item.text)