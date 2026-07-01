import csv
import requests
from bs4 import BeautifulSoup

url = 'https://example.com/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

csv_file = open('data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'description'])

for article in soup.find_all('article'):
 title = article.h2.a.text
 description = article.find('div', class_='entry-content').p.text
 csv_writer.writerow([title, description])

csv_file.close()