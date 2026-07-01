import requests
from bs4 import BeautifulSoup

# Input web address of the book
url = 'https://www.example.com/book.html'

# Download the page
page = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Extract the text
text = soup.find_all('p')
for p in text:
 print(p.text)