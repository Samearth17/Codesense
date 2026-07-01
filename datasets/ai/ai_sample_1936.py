import random

#GREETINGS
greetings  = ["Hi", "Hey", "Hello", "Hi there", "What's up?"]

#PROMPTS
prompts = ["how may I help you?", "want to talk about something?", "What do you want to talk about?"]

#Program
def respond(message):
    if any(greeting in message for greeting in greetings):
        index = random.randint(0, len(prompts)-1)
        return prompts[index]
    return ""

#Example test
user_message = "Hey"
bot_response = respond(user_message)
print(bot_response) # What do you want to talk about?