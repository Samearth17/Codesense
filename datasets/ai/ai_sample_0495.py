import requests
from bs4 import BeautifulSoup

# define the url
url = "https://www.example.com/titles"

# send the request and get the response
response = requests.get(url)

# parse the response
soup = BeautifulSoup(response.content, 'html.parser')

# find all the <h3> elements in the page
h3_elements = soup.find_all('h3')

# extract the titles from the <h3> elements and print them
for element in h3_elements:
 print(element.text)