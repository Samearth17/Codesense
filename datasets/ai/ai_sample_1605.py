import re
import random

class Chatbot:
    # constructor
    def __init__(self):
        self.responses = {
            # greetings
            "hi": ["Hello!", "Hi!", "Hey!", "Hi there!"],
            "hello": ["Howdy!", "Hey!", "Hey there!"],
            # farewells
            "bye": ["Goodbye!", "Bye!", "See you later!"],
            "goodbye": ["Bye!", "Farewell!", "See you later!"],
            # general
            "thanks": ["You're welcome!", "It was my pleasure!", "No problem!"]
        }
    
    # tokenizes the input
    def tokenize_input(self, input_text):
        return re.split(" ", input_text.lower())
    
    # checks if a given word exists in the responses
    def is_valid_input(self, word):
        return word in self.responses
    
    # main rule-based chatbot logic
    def chatbot_response(self, input_text):
        tokenized_input = self.tokenize_input(input_text)
        
        if any([self.is_valid_input(word) for word in tokenized_input]):
            # select a random valid response
            random_index = random.randint(0, len(self.responses[tokenized_input[0]]) - 1)
            return self.responses[tokenized_input[0]][random_index]
        else:
            return "I'm sorry, I don't understand."