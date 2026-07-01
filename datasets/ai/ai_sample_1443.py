import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Gender_inequality"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract heading
heading_list = soup.findAll('h1')
heading = heading_list[0].text

# Extract paragraphs
paragraph_list = soup.findAll('p')

# Parse the paragraphs
data = []
for paragraph in paragraph_list:
    if any(x.isalpha() for x in paragraph.text):
        data.append(paragraph.text)

print(heading)
print(data)