import requests
import json

# Define endpoint
endpoint = 'https://api.nytimes.com/svc/topstories/v2/home.json?'

# Pass API key
payload = {'api-key': 'INSERT-KEY-HERE'}

# Make request to endpoint
req = requests.get(endpoint, params=payload)

# Parse the response
data = json.loads(req.text)

# Iterate over results and print headline
for result in data['results'][:10]:
    print(result['title'])