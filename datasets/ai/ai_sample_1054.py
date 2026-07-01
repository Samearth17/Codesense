import requests

api_url = 'http://example.com/api'

# Make a get request
response = requests.get(api_url)

# Check status code
if response.status_code == 200:
 # Get the response data as JSON
 data = response.json()

 # Do something with the data
 print(data)

# Make a post request
data = {
 'name': 'John Doe'
}

response = requests.post(api_url, data=data)

# Check status code
if response.status_code == 201:
 # Get the reponse data as JSON
 data = response.json()

 # Do something with the data
 print(data)