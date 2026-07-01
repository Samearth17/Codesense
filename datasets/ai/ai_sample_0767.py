import requests
from bs4 import BeautifulSoup

# Make the request
url = f'https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Get the official language for each country
languages = []
for table in soup.find_all('table'):
    headings = table.find('th').text
    if headings == 'Official language(s)':
        rows = table.find_all('td')
        for row in rows:
            lang = row.find('a')
            if lang.text.lower() == 'english':
                languages.append(lang.text)

# Print out the list of languages
print(languages)