import requests
import json
 
# base url as given in Reddit API documentation
base_url = 'https://www.reddit.com/search.json'
 
# parameters for the search query. In our case - q is the query
params = {
 'q': 'Machine Learning'
}
 
# send get request
response = requests.get(base_url, params=params)
 
# extract data in json format
data = response.json()
 
# data is a nested dictionary. Get the list of results using the 'data' key
results = data['data']['children']
 
# iterate through the list and print each post
for post in results:
    print(post['data']['title'])