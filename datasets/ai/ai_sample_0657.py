import nltk

# sample input
input = 'Hello, how are you?'

# list of tokenized words
words = nltk.word_tokenize(input)

# list of part-of-speech tagged words
words_tagged = nltk.pos_tag(words)

# defining chatbot's greeting response 
greeting_response = 'Hi there! How can I help you?'

# defining chatbot's response to a question
if words_tagged[1][1] == "WP":
    response = 'I am sorry, I can not answer this question.'
    
# checking for greeting in input
if words_tagged[0][1] == 'UH':
    response = greeting_response

# printing the chatbot response
print(response)
# Hi there! How can I help you?