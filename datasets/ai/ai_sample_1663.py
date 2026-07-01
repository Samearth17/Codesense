import sys
import Adafruit_DHT
import time
import requests

sensor = Adafruit_DHT.DHT11
pin = 23

while True:
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

 if humidity is not None and temperature is not None:
  payload = {'temperature': temperature, 'humidity': humidity}
  r = requests.post('http://mydatabase.url/api/data', json=payload, verify=False)

  print('Temp={0:0.1f}°C Humidity={1:0.1f}%'.format(temperature, humidity))
  time.sleep(60)

else:
 print('Failed to get reading. Try again!')
 sys.exit(1)