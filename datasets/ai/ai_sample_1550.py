import nltk
import random

responses = {
 'question': [
 "I don't know :(",
 'you tell me!'
 ],
 'statement': [
 'tell me more!',
 'why do you think that?',
 'how long have you felt this way?',
 'I find that extremely interesting',
 'can you back that up?',
 'oh wow!',
 ':)'
 ]
}

def respond(message):
 # check for a question mark
 if message.endswith('?'):
 # return a random question
 return random.choice(responses['question'])
 # return a random statement
 return random.choice(responses['statement'])

# create a dictionary for our bag of words
dictionary = []
for key, value in responses.items():
 for string in value:
 # tokenize each string and add to our bag of words
 tokens = nltk.tokenize.word_tokenize(string)
 dictionary += tokens
 
# preprocessing
def preprocess(message):
 # tokenize the message
 tokens = nltk.tokenize.word_tokenize(message)
 # convert message to lowercase
 tokens = [w.lower() for w in tokens]
 # remove punctuation from each word
 import string
 table = str.maketrans('','',string.punctuation)
 stripped = [w.translate(table) for w in tokens]
 # remove remaining tokens that are not alphabetic
 words = [word for word in stripped if word.isalpha()]
 # filter out stop words
 from nltk.corpus import stopwords
 stop_words = set(stopwords.words('english'))
 words = [w for w in words if not w in stop_words]
 # join filtered tokens back into a string sentence
 return ' '.join(words)

# check for a greeting
def greetingCheck(message):
 message = message.lower()
 for string in responses['greeting']:
 if message.startswith(string):
 return True

# main function
def main():
 while True:
 message = input('INPUT :\t')
 if greetingCheck(message):
 print('OUTPUT :\t')
 print(random.choice(responses['greeting']))
 else:
 message_processed = preprocess(message).lower()
 print('OUTPUT :\t', respond(message_processed))
 
main()