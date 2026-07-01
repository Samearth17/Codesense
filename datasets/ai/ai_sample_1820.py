import requests 
from bs4 import BeautifulSoup 

# Get the webpage
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url) 

# Create the soup
soup = BeautifulSoup(response.text, 'html.parser') 

# Extract the text
text = soup.get_text() 

# Output the text
print(text)