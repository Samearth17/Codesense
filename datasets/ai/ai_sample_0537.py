import requests
from bs4 import BeautifulSoup

# Make a GET request to fetch the raw HTML content
url = "https://www.example.com/"
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Find all links in the page
titles_list = soup.find_all("a")
titles_urls = [(title.text, title["href"]) for title in titles_list]

# Print all titles and their corresponding links
for title, url in titles_urls:
    print("Title:", title)
    print("URL:", url)
    print()