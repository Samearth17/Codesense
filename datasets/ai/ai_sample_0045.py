import requests
from bs4 import BeautifulSoup 

# url of the website you want to scrape 
url = "https://www.news.com/" 

# get the response in the form of html
r = requests.get(url) 

# create a beautifulsoup object to parse contents 
soup = BeautifulSoup(r.content, 'html5lib') 

# find headlines from the parsed page  
headlines = soup.find_all('h2') 

# Print the headlines 
for headline in headlines: 
    print(headline.text)