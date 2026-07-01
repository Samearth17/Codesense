import random
import spacy
import nltk

# load the English language model
nlp = spacy.load('en_core_web_sm')

# define some sample conversations
conversations = [ 
       ['Hello', 'Hi there'], 
       ['How are you?', 'I am doing great!'], 
       ['Bye', 'Goodbye!'], 
]

# define an answer generator
def answer(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    for conversation in conversations:
        if conversation[0] in tokens:
            return random.choice(conversation[1:])
    return ''

# create a loop to run the chatbot
while True:
    text = input('You: ')
    response = answer(text)
    print('Bot: ', response)
    if response == 'Goodbye!':
        break