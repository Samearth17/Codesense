import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com/movies'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
ratings = []
dates = []
descriptions = []

# Get the movie titles
all_titles = soup.find_all('h3', class_='title')
for title in all_titles:
 titles.append(title.text)

# Get the movie ratings
all_ratings = soup.find_all('span', class_='rating')
for rating in all_ratings:
 ratings.append(rating.text)

# Get the movie dates
all_dates = soup.find_all('span', class_='date')
for date in all_dates:
 dates.append(date.text)

# Get the movie descriptions
all_descriptions = soup.find_all('p', class_='desc')
for description in all_descriptions:
 descriptions.append(description.text)

# Print out the collected data
for i in range(len(titles)):
 print(f'Movie Title: {titles[i]}')
 print(f'Movie Rating: {ratings[i]}')
 print(f'Movie Date: {dates[i]}')
 print(f'Movie Description: {descriptions[i]}')