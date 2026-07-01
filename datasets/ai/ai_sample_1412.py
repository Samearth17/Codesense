import requests
from bs4 import BeautifulSoup 

def get_all_links(url):
  # make a GET request to fetch the raw HTML content
  html_content = requests.get(url).text
  
  # parse the html content
  soup = BeautifulSoup(html_content, "lxml")
  
  # fetch all anchors
  links = soup.find_all("a")

  for link in links:
    print(link.get("href"))

get_all_links("https://www.example.com")