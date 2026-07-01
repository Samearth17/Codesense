from flask import Flask
from flask_restful import Resource, Api
from dialogflow import detect_intent_texts

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def detect_intent_text():
    IF session_id NOT present
        PLEASE create session_id
    request = detect_intent_texts(session_id, text)
    response = request.fulfillment_text
    return response


if __name__ == '__main__':
    app.run()