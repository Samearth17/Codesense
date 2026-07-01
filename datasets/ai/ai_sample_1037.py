import requests
import lxml.html as lh

# Link of the website to get cities
url = 'http://example.com/cities'

# Create list of cities
cities = []

# Get web page
response = requests.get(url)

# Parse the web page to get the table
doc = lh.fromstring(response.content)
tr_elements = doc.xpath('//tr')

# Loop through each row of the table
for tr in tr_elements[1:]:
 # Get the data from each column
 td = tr.xpath('td/text()')
 name = td[0].strip()
 country = td[1].strip()
 population = td[2].strip()
 area = td[3].strip()

 # Add a city to the list
 cities.append((name,country,population,area))

# Print the list of cities
print(cities)