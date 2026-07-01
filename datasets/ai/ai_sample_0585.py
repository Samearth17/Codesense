from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/wikipedia', methods=['GET'])
def search_wikipedia():
 query = request.args.get('query')
 response = requests.get(
 'https://en.wikipedia.org/w/api.php',
 params={
 'action': 'query',
 'list': 'search',
 'format': 'json',
 'srsearch': query
}).json()

 return response

if __name__ == '__main__':
 app.run()