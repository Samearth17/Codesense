import requests

# Enter the city for which the forecast is required
city = 'Berlin'

# OpenWeatherMap API key
api_key = '<your_api_key>'

# Get the json data from API using the city name
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + api_key
weather_data = requests.get(url).json()

# Extract the temperature and wind forecast
temperature = round(weather_data['main']['temp'] - 273.15, 2)
wind_speed = round(weather_data['wind']['speed'], 2)

# Print the forecast
print('Temperature:', temperature, '°C')
print(' Wind Speed:', wind_speed, 'm/s')