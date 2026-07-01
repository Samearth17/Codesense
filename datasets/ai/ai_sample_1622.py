import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # sending get request and saving the response as response object 
    r = requests.get(url) 
    
    # extracting data in json format 
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    
    contents = soup.find_all('p')
    for content in contents:
        print(content.text)

scrape_website("https://example.com")