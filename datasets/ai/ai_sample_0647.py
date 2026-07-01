import re 
import random 

# define the bot 
class Bot: 
    def __init__(self): 
        self.greets = ['hey', 'hello', 'hi', 'greetings'] 
        self.responses = ['Hello!', 'Hi there!', 'Greetings!', 'Nice to meet you!']

    # process message using regular expression     
    def process_message(self, message): 
        pattern = re.search("(?:hey|hello|hi|greetings)(.*)", message) 

        if pattern: 
            # generate a random response 
            response = random.choice(self.responses) 
            # return the response 
            return response

# create an instance of the Bot class 
bot = Bot() 

while True:
    # enter the message 
    print('You:', end='') 
    message = input()

    # process the message 
    response = bot.process_message(message) 
    # print the response 
    print('Bot:', response)