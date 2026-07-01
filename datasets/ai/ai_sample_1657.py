import nltk
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

#files in th eclipse         
path = 'data'
token_dict = {} 
stemmer = PorterStemmer()

#read all the files in the given directory
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

#read the file and add the tokens to token dict
def tokenize(text):
 token = [t.lower() for t in nltk.word_tokenize(text)]
 tokens = [word for word in token if word not in string.punctuation]
 stems = stem_tokens(tokens, stemmer)
 return stems

for subdir, dirs, files in os.walk(path):
 for file in files:
  file_path = subdir + os.path.sep + file
  f = open(file_path, 'r')
  text = f.read()
  token_dict[file] = text

#create TFIDF vectorizer
tfidfvectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
#train the vectorizer
tfidfvectorizer.fit_transform(token_dict.values())

#function to search the files
def search(query):
 query_tfidfvectorizer = tfidfvectorizer.transform([query])
 #search for the files
 results =  tfidfvectorizer.transform(token_dict.values()).transpose() * query_tfidfvectorizer
 best_result_index = results.argmax()
 
 return list(token_dict.keys())[best_result_index]