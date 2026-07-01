import re 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 

# Function to find the negation words
def findNegation(sentence):
    # save all the negation words
    negationwords = {'not', 'never', 'no', 'none', 'non', 'neither',
                     'nobody', 'nowhere', 'cannot', 'couldnt', 'shouldnt', 
                     'wouldnt', 'dont', 'didnt', 'hasnt', 'havent', 'isnt', 'arent'} 
    words = nltk.word_tokenize(sentence)
    neg = []
    for word in words:
        if word in negationwords:
            neg.append(word)
    return neg

# Function to check if the sentence is affirmative or negative
def isAffirmativeorNegative(sentence):
     negationwords = findNegation(sentence)
    if len(negationwords)==0: 
        return "Affirmative" 
    else: 
        return "Negative"    

sentence = "He always comes late but I dont mind."
result = isAffirmativeorNegative(sentence) 
print(result)  # prints Negative