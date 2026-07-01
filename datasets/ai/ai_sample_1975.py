import nltk
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

# Define a function for processing the user query
def process_message(message):
    # Split the query into separate words 
    tokens = nltk.word_tokenize(message)
    
    # Lemmatize each word 
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Return the list of lemmatized tokens 
    return tokens

# Define the answer function
def answer_query(query):
    # Process the message
    tokens = process_message(query)
    
    # Check if the query includes the word "refund"
    if 'refund' in tokens:
        # Return the message 
        return 'Yes, you can get a refund if your product is defective.'
    
    # Return the message 
    return 'Sorry, I can\'t answer that question.'