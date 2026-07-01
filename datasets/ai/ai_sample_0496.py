import requests
from bs4 import BeautifulSoup

# fetch the html from the BBC news website
html = requests.get('https://www.bbc.co.uk/news').content
soup = BeautifulSoup(html, 'html.parser')

# extract the titles and URLs of the trending news stories
trending_stories = soup.find('div', {'aria-label': 'Top stories'})
stories = trending_stories.find_all('div', class_='gs-container gs-u-ph-')

titles = [s.find('h3', {'class': 'gs-u-mb-0'}).get_text() for s in stories]
urls = [s.find('a')['href'] for s in stories]

# print the titles and URLs
for title, url in zip(titles, urls):
 print(title, url)