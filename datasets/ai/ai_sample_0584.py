import requests
from bs4 import BeautifulSoup

# Get the webpage
url = input("Enter the URL of the webpage:")
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Get all the text
text = soup.get_text()

# Split text into words
words = text.split()

# Count words
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort word counts
sorted_words = sorted(word_count, key=word_count.get, reverse=True)

# Print top ten words
print(sorted_words[:10])