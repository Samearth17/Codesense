# Libraries
import requests
import json

# Get user input
user_input = input('Please enter your query: ')

# Process user input
if 'weather' in user_input:
 # Get weather data
 city = user_input.split()[-1] # extract city from user query 
 r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=YOUR_API_KEY')
 data = json.loads(r.text) 

# Output response
 if data['cod'] == '404':
 print('City not found!')
 else:
 print(f'The temperature in {city} is: {data["main"]["temp"]} °C')

elif 'population' in user_input:
 # Get population data
 country = user_input.split()[-1] # extract country from user query
 r = requests.get(f'https://restcountries.eu/rest/v2/name/{country}')
 data = json.loads(r.text)[0] # extract population from API response

# Output response
 print(f'The population of {country} is: {data["population"]}')

else:
 print("I'm sorry, I don't understand.")