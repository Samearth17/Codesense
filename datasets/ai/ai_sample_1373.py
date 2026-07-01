# import required modules
import requests
import json

# set the base url
base_url = 'http://api.datapoint.metoffice.gov.uk/'

# set the query parameters
params = {
    'key': 'YOUR_API_KEY',
    'res': 'sport'
}

# get the response from API
response = requests.get(base_url, params=params)

# parse the response
data = json.loads(response.text)

# get list of all sports data sets
data_sets = [d['name'] for d in data['resources']]

# print all data sets
for d in data_sets:
    print(d)