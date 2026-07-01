from bs4 import BeautifulSoup
import requests
import re


def getTopSites():
 url = 'https://www.alexa.com/topsites'
 response = requests.get(url)
 soup = BeautifulSoup(response.text, 'html.parser')
 
 table = soup.find('table')
 
 table_rows = table.find_all('tr')
 
 top_websites = []
 
 for row in table_rows:
 
 cols = row.find_all('td')
 
 if cols != []:
 website_name = cols[1].text
 website_rank = re.sub('[^0-9]', '', cols[0].text) 
 
 top_websites.append({
 'name': website_name,
 'alexa_rank': website_rank
 })
 
 return top_websites
 
 
if __name__ == '__main__':
 print(getTopSites())