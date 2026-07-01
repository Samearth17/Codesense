import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/List_of_gravitationally_rounded_objects_of_the_Solar_System')
soup = BeautifulSoup(page.content, 'lxml')

planets_table = soup.find('table', class_='wikitable sortable')

planets = []
for row in planets_table.find_all('tr'):
 if row.find('th'):
 continue
 cells = row.find_all('td')
 planets.append({
 'name': cells[0].text,
 'mass': cells[2].text,
 'distance_from_sun': cells[5].text
 })

print(planets)