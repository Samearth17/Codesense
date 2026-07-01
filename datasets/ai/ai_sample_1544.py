import requests 
from bs4 import BeautifulSoup
  
def crawl(url): 
    page = requests.get(url) 
    soup = BeautifulSoup(page.text, 'html.parser') 
  
    # retrieve all of the anchor tags
    # We are going to find all links out of the page
    tags = soup('a')
    for tag in tags:  
        link = tag.get('href', None) 
        if link != None: 
            print(link) 
            
# Driver code 
if __name__ == "__main__": 
    URL = "http://example.com"   # type your address instead of example.com
    crawl(URL)