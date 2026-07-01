def extract_keywords(text):
 # lowercase the text
 text = text.lower()
 
 # split the text into words
 words = text.split(' ')
 
 # create a list to store the keywords
 keywords = []
 
 # iterate over each word and extract keywords
 for word in words:
 # if the word contains more than 3 characters
 # and is not in a stopwords list
 # then it is a keyword
 if len(word) > 3 and word not in stopwords:
 keywords.append(word)
 
 # return the list of keywords
 return keywords 

extract_keywords('This is a text string with some important keywords.')
# => ['text', 'string', 'important', 'keywords']