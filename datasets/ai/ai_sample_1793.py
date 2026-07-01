import requests
from bs4 import BeautifulSoup

# Specify the URL
url = 'website.com'

# Get the response
response = requests.get(url)

# Parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all the articles on the front page
articles = soup.find_all('article', class_='front-page-article')

# Iterate through each article and print its text
for article in articles:
 print(article.find('h2').text)