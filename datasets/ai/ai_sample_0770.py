import json 
import requests 

#Get the URL for the website
url = 'https://example.com/blogpage'
r = requests.get(url)

#Check for errors
if r.status_code != 200:
 print('Error:', r.status_code)

#Parse the page content
page_content = r.text 

#Parse the page_content into a Key-Value format
dict = {}
for line in page_content.split('\n'):
  words = line.split()
  if len(words) > 1:
    key = words[0]
    value = words[1]
    dict[key] = value

#Create a new JSON 
data = json.dumps(dict);

#Print the JSON
print(data)