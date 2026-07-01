import requests
import json

# Get access token
url = 'https://accounts.spotify.com/api/token'
data = {'grant_type': 'client_credentials'}
auth = ('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')
response = requests.post(url, data=data, auth=auth)
token = json.loads(response.text)['access_token']

# Search for artist
url = 'https://api.spotify.com/v1/search'
params = { 'q': 'The Beatles', 'type': 'artist' }
header = { 'Authorization': f'Bearer {token}' }
response = requests.get(url, params=params, headers=header)
artist = json.loads(response.text)['artists']['items'][0]

# Get artist information
url = artist['href']
response = requests.get(url, headers=header)
artist_info = json.loads(response.text)

print(artist_info)