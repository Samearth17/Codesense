import requests

THRESHOLD = 10
CITY = 'New York'

def check_temp():
 url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=<API_KEY>'.format(CITY)
 r = requests.get(url).json()
 temp = r['temp']
 if temp < THRESHOLD:
  send_email(f'The temperature is {temp} in {CITY}')

def send_email(message):
 # Code to send an email
 pass

check_temp()