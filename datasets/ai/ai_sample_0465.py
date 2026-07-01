# Import relevant modules
import requests
import json

# Url for API
URL = "https://api.example.com/geocode"

# Create function to fetche location information
def get_location_info(lat, lon):
    PARAMS = {'lat': lat, 'lon': lon}
    response = requests.get(url=URL, params=PARAMS)
    output = json.loads(response.text)
    return output

# Call the function
location_info = get_location_info(lat, lon)