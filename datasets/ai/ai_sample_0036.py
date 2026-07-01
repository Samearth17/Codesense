import requests
from bs4 import BeautifulSoup
import re

def crawl(url):
 visited = set()
 queue = [url] 
 
 while queue:
 curr = queue.pop(0)
 visited.add(curr) 
 response = requests.get(curr)
 
 if response.ok:
 soup = BeautifulSoup(response.text, 'html.parser')

# scrape the page here 

# find all the links
 links = soup.find_all('a', href=re.compile('^http')) 
 
 for link in links:
 if link['href'] not in visited:
 queue.append(link['href'])