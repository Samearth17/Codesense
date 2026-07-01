import json
import requests

# Handler function
def handler(event, context):
 # Make request
 response = requests.get('https://api.example.com/data')
 
 # Parse response
 data = response.json()
 
 return {
 'statusCode': 200,
 'body': json.dumps(data)
 }