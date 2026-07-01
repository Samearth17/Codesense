import requests
from bs4 import BeautifulSoup

url = "https://www.example.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("title")
descriptions = soup.find_all("meta", {"name": "description"})

for title in titles:
 print(title.string)

for description in descriptions:
 print(description.attrs["content"])