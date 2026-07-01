import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/ocean-creatures", methods=["GET"])
def get_ocean_creatures():
 query = request.args.get("q","")
 url = "https://en.wikipedia.org/w/api.php"
 params = {
 'action': 'query',
 'list':'search',
 'srsearch': query + ' ocean',
 'format': 'json',
 }
 res = requests.get(url, params=params).json()
 return jsonify(res)

if __name__ == '__main__':
 app.run(debug=True)