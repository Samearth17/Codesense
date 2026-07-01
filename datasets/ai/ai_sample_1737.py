import json

data = json.loads(jsonString)

us_cities = []
europe_cities = []

for location in data['locations']:
 if location['continent'] == 'North America':
 us_cities.append(location['name'])
 elif location['continent'] == 'Europe':
 europe_cities.append(location['name'])

print(f'US cities: {us_cities}\n')
print(f'Europe cities: {europe_cities}\n')