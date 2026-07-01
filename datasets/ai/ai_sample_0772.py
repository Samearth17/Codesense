# importing required libraries 
import random 
import string 
import spacy 
import nltk 

# Function to generate response 
def chatbot_response(user_input): 
    # Preprocessing user input 
    user_input = user_input.lower() 
    user_input = user_input.translate(str.maketrans('', '', string.punctuation)) 

    # Loading spacy model to parse and understand user input 
    nlp = spacy.load('en_core_web_sm') 
    doc = nlp(user_input) 

    # Initializing nltk for Stopwords removal 
    nltk.download('stopwords') 
    from nltk.corpus import stopwords 
    stopwords = stopwords.words('english') 

    # Extracting keyword from user input 
    key_word = [word for word in doc if word.text not in stopwords] 

    # Generating response 
    response = ''
    if key_word:
        # Generate a random response if keyword is recognized by chatbot 
        response = random.choice(['That is an interesting topic.', 'I see. Tell me more.', 
                            'I am happy to help.']) 
    else:
        response = "Sorry, I didn't quite understand what you said."

    return response