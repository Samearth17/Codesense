import random

#list of possible answers 
answers = ["That's a great question!", 
    "I'm not sure, but I'll try to find out!", 
    "That sounds interesting, tell me more!", 
    "I have no idea, sorry!"]

def chatbot_response(user_input): 
    # get a random response from answers
    response = random.choice(answers)
    return response

# simple loop to keep the conversation going
while True:
    user_input = input('You: ')
    if user_input == 'Goodbye':
        print('Chatbot: Goodbye!')
        break
    else:
        print('Chatbot: ', chatbot_response(user_input))