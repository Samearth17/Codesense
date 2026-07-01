import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
 url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=xxx"
 response = requests.get(url)
 if response.status_code == 200:
  data = response.json()
  return jsonify({
   'current_temperature': data['main']['temp']
  })
 else:
  return jsonify({'message': 'Error connecting to openweathermap API'}), 400

if __name__ == '__main__':
 app.run(debug=True)