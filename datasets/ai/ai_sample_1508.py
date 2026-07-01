from flask import Flask
from flask_restful import Resource, Api
from nltk.corpus import wordnet

app = Flask(__name__)
api = Api(app)

class SynAntonyms(Resource):
 def get(self, word):
 syns = wordnet.synsets(word)
 synonyms = []
 antonyms = []
 for s in syns:
 for l in s.lemmas():
 synonyms.append(l.name())
 if l.antonyms():
 antonyms.append(l.antonyms()[0].name())
 return {
 'synonyms': list(set(synonyms)),
 'antonyms': list(set(antonyms))
 }

api.add_resource(SynAntonyms, '/synantonyms/<string:word>')

if __name__ == '__main__':
 app.run(debug=True)