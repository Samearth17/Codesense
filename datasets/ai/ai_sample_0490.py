import requests
from bs4 import BeautifulSoup

# Get the HTML from the URL
url = "https://www.reddit.com/r/ProgrammerHumor/comments/hfpmoo/people_ask_me_why_i_learn_so_many_programming/"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Get all the comments from the page
comments = []
for comment in soup.find_all("div", class_="md"):
    comments.append(comment.text)

# Print all the comments
for comment in comments:
    print(comment)