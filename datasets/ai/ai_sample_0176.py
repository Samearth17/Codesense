import requests
import json

from flask import Flask, request

app = Flask(name)

@app.route('/getTemp', methods=['POST'])
def get_temp():
 city = request.json['city']
 url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=xxxxxx'
 r = requests.get(url.format(city))
 weather = json.loads(r.text)
 return {'temperature': weather['main']['temp']}

if name == 'main':
 app.run(debug=True)