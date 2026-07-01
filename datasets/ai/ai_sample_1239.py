# Importing the necessary libraries
import random

# Defining the responses for the bot
questions = ["What is your favorite movie?", "What is your favorite color?"]
responses = ["My favorite movie is 'The Godfather'. I love the classic vibe of the movie.", 
             "My favorite color is blue. It's soothing and calming to me."]

# Function to respond to the questions
def respond(user_input):
    if user_input in questions:
        return random.choice(responses)
    else:
        return "I'm sorry, I don't understand."

# Driver code
print("Bot: Hi! What can I help you with?")
user_input = input("User: ")

while user_input != "bye":
    print("Bot: " + respond(user_input))
    user_input = input("User: ")

print("Bot: Bye! It was nice talking to you!")