import uuid
import flask

app = flask.Flask(__name__)

messages = []

@app.route('/message', methods=['POST'])
def add_message():
 data = flask.request.get_json()
 data['id'] = str(uuid.uuid4)
 messages.append(data)
 return {'message': 'Added message', 'data': data}, 200

if __name__ == '__main__':
 app.run()