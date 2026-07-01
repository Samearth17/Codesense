import json
import requests

# Fetch data from OMDB API
def fetch_omdb_data(omdb_api_key):
 omdb_data = []

 # Query for movies
 omdb_url = f'http://www.omdbapi.com/?apikey={omdb_api_key}&s=movies'
 response = requests.get(omdb_url)
 data = response.json()
 for item in data['Search']:
    omdb_data.append( (item['Title'], item['Year'], item['Type'], item['imdbID']) )

# Fetch data from Football Data API
def fetch_football_data(football_api_key):
 football_data = []

 # Query for football matches
football_url = f'http://api.football-data.org/v2/matches?apikey={football_api_key}'
response = requests.get(football_url)
data = response.json()
for item in data['matches']:
 football_data.append( (item['competition']['name'], item['season']['startDate'], item['season']['endDate'], item['utcDate']) )

# Merge data from both APIs
merged_data = []
for omdb_row in omdb_data:
 for football_row in football_data:
 if (omdb_row[1] >= football_row[1] and omdb_row[1] <= football_row[2]):
 merged_data.append(( *omdb_row, *football_row ))

# Write merged data into JSON file
with open('merged_data.json', 'w') as outfile:
 json.dump(merged_data, outfile)

# Run functions
omdb_api_key = '12345678'
football_api_key = '87654321'
fetch_omdb_data(omdb_api_key)
fetch_football_data(football_api_key)