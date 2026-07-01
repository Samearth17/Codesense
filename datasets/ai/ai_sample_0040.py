import requests
from bs4 import BeautifulSoup

# Define the URL and the headers
url = '<url>'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

# Make a request and get HTML in response
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all reviews
reviews = soup.find_all('div', {'class': 'review-container'})

# Go through every review and extract the data
for review in reviews:
    # Get the title
    title = review.find('span', {'class': 'noQuotes'}).text

    # Get the text
    text = review.find('p', {'class': 'partial_entry'}).text

    # Print for demo
    print(title)
    print(text)
    print('-' * 50)