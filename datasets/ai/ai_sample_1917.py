import requests
from bs4 import BeautifulSoup

def parse_html(url):
  # Send a get request
  response = requests.get(url)
  
  # Create a BeautifulSoup object
  soup = BeautifulSoup(response.text, 'lxml')

  # Find the required data
  data = soup.find_all('div', class_='content')

  # Return the data
  return data