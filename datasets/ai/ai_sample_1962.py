import requests
from bs4 import BeautifulSoup

# Set the URL
url = 'https://www.instagram.com/{username}'

# Make a request
response = requests.get(url)

# Parse the response
soup = BeautifulSoup(response.text, 'lxml')

# Extract the followers
followers = soup.find('span', {'class': 'g47SY'}).next_sibling.text

# Print the followers
print(f'Number of followers of the user: {followers}')