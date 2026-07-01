import requests

# list of cities for which we want the weather forecast
cities = ["New York", "London", "Beijing", "Los Angeles", "Berlin", "Tokyo", "Mumbai", "Moscow"]

# api key
api_key = YOUR_API_KEY

# base url for the weather api
url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=" + api_key

# create an empty list to store weather data
weather_data = []

# loop through the cities and get the weather data
for city in cities:
	# make a request to the api
	r = requests.get(url.format(city)).json()
	# store the weather data in the list
	weather_data.append(r)

# print the weather data
print(weather_data)