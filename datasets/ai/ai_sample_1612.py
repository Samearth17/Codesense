import requests 
from bs4 import BeautifulSoup 
import re

# Fetch the web page 
page = requests.get("THE_WEBPAGE_URL") 
# Parse the content of the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all visible text in the page 
text = soup.find_all(text=True)

# Remove text inside scripts and style tags
for t in text: 
    if t.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: 
        text.remove(t)

# Remove extra spaces
text_string = " ".join(text)
text_string = re.sub('\s+', ' ', text_string)

# Count the total number of words 
word_count = len(text_string.split()) 

print("Total number of words:", word_count)