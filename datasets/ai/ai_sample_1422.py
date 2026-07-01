import requests
from bs4 import BeautifulSoup
 
 
def scrape_web_page(url, keywords):
 keyword_found = False
 
 # Make a GET request to fetch the raw HTML content
 html_content = requests.get(url).text
 
 # Parse the html content
 soup = BeautifulSoup(html_content, "lxml")
 
 # Find all occurrences of the given keywords in the HTML document
 for keyword in keywords:
   if keyword in soup.text:
     keyword_found = True
 
 # Return a boolean to indicate if a keyword was found
 return keyword_found