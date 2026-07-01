import requests
from bs4 import BeautifulSoup

# Make a GET request to fetch the raw HTML content
html_content = requests.get(URL).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Print all the articles on the page
print("All articles")
print("-----------")
articles = soup.find_all('p')
for article in articles:
    print(article.text)

# Print all the headlines
print("Headlines")
print("--------")
headlines = soup.find_all('h1')
for headline in headlines:
    print(headline.text)

# Print all the hyperlinks
print("Hyperlinks")
print("---------")
links = soup.find_all('a')
for link in links:
    print(link.get('href'))