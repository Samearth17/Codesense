# import libraries
import requests
from bs4 import BeautifulSoup
 
# define the search url
url = 'https://www.quora.com/search'
 
# create a payload for the query parameters
payload = {'q': 'machine learning'}
 
# get the content from the specified url
r = requests.get(url, params=payload)
 
# parse the content
soup = BeautifulSoup(r.content, 'html.parser')
 
# collect data from all the elements with class 'question_link'
results = soup.find_all('a', class_='question_link')
 
# print the results
for result in results:
    print(result.text)