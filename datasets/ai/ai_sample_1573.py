import requests
from bs4 import BeautifulSoup
 
# Make a GET request to fetch the raw HTML content
html_content = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)').text
 
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
 
# Find all the h2 tags and iterate through them
for h2_tag in soup.find_all("h2"):
    # Check if h2 tag has a 'tocsection' class
    if "tocsection" in h2_tag.attrs['class']:
        # Extract the article title from the h2 tag
        article_title = h2_tag.text.strip()
        # Print the article title
        print("Article Title:", article_title)
        print("-"*50)