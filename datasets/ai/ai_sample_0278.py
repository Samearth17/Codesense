# main.py
# The Google App Engine entry point with requests and responses

from google.appengine.ext import ndb
from flask import Flask

# Define the Flask application
app = Flask(__name__)

@app.route('/api/v1/ persons/<id>', methods=['GET'])
def get_person_by_id(id):
    person = ndb.Key("Person", id).get()
    if person is not None:
        data = person.to_dict()
        return json.dumps(data)
    else:
        # Return an error code if person with the provided ID was not found
        return '{"error": "Person not found"}'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)

# app.yaml

# [START gae_python_app]
runtime: python27
api_version: 1
threadsafe: true

# app.yaml
env_variables:
  # Replace the placeholder below with your GCP project ID and make sure
  # the variable is named `GCP_PROJECT`
  GCP_PROJECT: <YOUR_PROJECT_ID>

# app.yaml
handlers:
- url: /.*
  script: main.app

# [END gae_python_app]