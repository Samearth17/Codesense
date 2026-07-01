import requests
from bs4 import BeautifulSoup
 
url = 'https://www.example.com/data'
 
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
 
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
 
# Storing data in list 
data = []
for tr_list in soup.find_all('tr'):
    # store data in list 
    data.append([td_list.text.strip() for td_list in tr_list.find_all('td')])
    
# printing fetched data
for tr_list in data:
    print(tr_list)