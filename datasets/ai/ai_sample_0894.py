import nltk 
import numpy as np 
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_chatbot():
  greetings = ["hi", "hey", "hello", "hola", "greetings", "wassup", "yo"]
  greet_response = ["hey there friend!", "hi there! How can I help you?", "hello! What would you like to know?"]

  question_responses = {
    "what is python?": "Python is a widely-used general-purpose, high-level programming language.",
    "who created python?": "Python was created in the late 1980s by Guido van Rossum, and released in 1991.",
    "what is java": "Java is a class-based, object-oriented programming language developed by Sun Microsystems in the 1990s."
  }

  # tokenize the user's input string
  def tokenize(user_input): 
    tokens = nltk.word_tokenize(user_input) 
    return tokens

  # generate a response from the chatbot
  def response(user_input, greetings, greet_responses, question_responses): 
    tokens = tokenize(user_input) 

    # check if the user's input contains a greeting
    for token in tokens:
      if token.lower() in greetings: 
        random_greeting = random.choice(greet_responses)
        return random_greeting

    # check if the user's input is contained in the question_responses dictionary
    for token in tokens:
      if token.lower() in question_responses.keys(): 
        return question_responses[token]

  print("Hello! I'm your friendly programming chatbot. What can I help you with?")
    
  exit_chat = False
  while(exit_chat == False):
    user_input = input() 
    user_input = user_input.lower() 
    
    if user_input != 'bye': 
      if user_input == 'thanks' or user_input =='thank you': 
        exit_chat = True
        print("My pleasure!")
      
      else:
        if response(user_input, greetings, greet_responses, question_responses) != None:
          chatbot_response = response(user_input, greetings, greet_responses, question_responses)
          print(chatbot_response)
        else:
          print("I'm sorry, I don't understand. Can you ask in a different way?")
    else:
      exit_chat = True
      print("Bye! Have a nice day!")