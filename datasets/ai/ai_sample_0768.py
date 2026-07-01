import pymongo
import requests
from bs4 import BeautifulSoup


# mongodb connection
client = pymongo.MongoClient(
'mongodb+srv://username:password@mycluster.mongodb.net/pubmed')
db = client.pubmed

# configure request headers
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# get the html from the page
res = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=covid-19', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# parse the html and extract the articles 
articles = soup.find_all('div', {'class': 'docsum-content'})
for article in articles:
    # article title
    title = article.find('p', {'class': 'title'}).text
    # link to article
    link = article.find('p', {'class':'links'}).find('a')['href']

    # insert article into DB
    db.articles.insert_one({'title': title, 'link': link})

client.close()