# Python program to scrape a webpage
import requests as req 
from bs4 import BeautifulSoup 
  
URL = "http://www.example.com/"
  
# GET request 
r = req.get(URL) 
  
# parse the downloaded homepage and grab all text
soup = BeautifulSoup(r.text, "html.parser") 
  
# find and print all links 
links = soup.find_all('a') 
for link in links: 
    print(link.get('href'))