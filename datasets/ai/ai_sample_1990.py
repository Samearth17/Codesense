from flask import Flask 
import requests 

app = Flask(__name__)

@app.route('/zipcodes/<city>', methods=['GET'])
def get_zipcodes_for_city(city: str):
  base_url = 'INSERT_API_ENDPOINT_HERE'
  r = requests.get(base_url + city) 
  response_data = r.json()
  zip_codes = response_data['data']
  return {'zip_codes': zip_codes}
  
if __name__ == '__main__':
    app.run()