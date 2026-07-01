import requests
import json
import sqlite3

# Request data from the API
r = requests.get('https://api.weather.com/v2/profiles/YOUR_APPID/forecast/hourly/48hour?units=m&language=en-US&format=json')

# Parse the response as a JSON object
data = json.loads(r.text)

# Connect to the database
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Create the database if it doesn't exist
c.execute('CREATE TABLE IF NOT EXISTS forecasts (time INTEGER, temperature REAL, humidity REAL, visibility REAL, wind_speed REAL)')

# Add the forecast data to the database
for hour in data["forecastGroup"]["forecast"]:
 c.execute('INSERT INTO forecasts VALUES (?, ?, ?, ?, ?)', (hour['fcst_valid'], hour['temp'], hour['humidity'], hour['visibility'], hour['wspd']))

# Commit the changes to the database
conn.commit()