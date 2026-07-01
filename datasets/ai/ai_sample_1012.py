import requests
from bs4 import BeautifulSoup

URL = "https://www.nba.com/scores"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('li', class_="score")

scores = []
for result in results:
    data=result.find_all("span", {'class': 'scoreboardScore'})
    scores.append([d.text for d in data])

with open("scores.txt", "w") as f:
    for score in scores:
        f.write(" ".join(score) + "\n")