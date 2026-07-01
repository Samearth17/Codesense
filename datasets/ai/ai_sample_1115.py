import requests
from bs4 import BeautifulSoup

# Fetch the webpages 
response = requests.get('https://example.com/page1.html')
#response2 = requests.get('https://example.com/page2.html')
#..
#responseN = requests.get('https://example.com/pageN.html')

# Parse the HTML contents  
soup = BeautifulSoup(response.text, 'lxml')
#soup2 = BeautifulSoup(response2.text, 'lxml')
#..
#soupN = BeautifulSoup(responseN.text, 'lxml')

# Extract the text content of each webpage 
text_content = soup.get_text()
#text_content2 = soup2.get_text()
#.
#text_contentN = soupN.get_text()