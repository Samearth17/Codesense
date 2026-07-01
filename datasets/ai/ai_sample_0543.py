import requests
from bs4 import BeautifulSoup
 
def get_page_word_count(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  words = soup.find_all(text=True)
  count = 0 
  for w in words:
    count += len(w.split())
  return count
  
url = "http://example.com"
word_count = get_page_word_count(url)
print("word count = ", word_count)