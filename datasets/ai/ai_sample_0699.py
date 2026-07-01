# Import essential libraries
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer 
import numpy as np
 
# Define  the documents
doc1 = "This is the first document"
doc2 = "This is the second document"
 
# Tokenize the documents
words_in_doc1 = word_tokenize(doc1) 
words_in_doc2 = word_tokenize(doc2) 
 
# Remove the stop words
stop_words = set(stopwords.words('english'))
filtered_doc1 = [w for w in words_in_doc1 if not w in stop_words] 
filtered_doc2 = [w for w in words_in_doc2 if not w in stop_words] 
 
# Stem the documents
ps = PorterStemmer()
stem_doc1 = [ps.stem(word) for word in filtered_doc1] 
stem_doc2 = [ps.stem(word) for word in filtered_doc2] 
 
#Generate Bag of Words for both documents
bag_of_words1 = ' '.join(stem_doc1)
bag_of_words2 = ' '.join(stem_doc2)
 
# Generate the corpus
corpus = [bag_of_words1, bag_of_words2]
  
# Generate the Count Vector
cv = CountVectorizer()
vectors = cv.fit_transform(corpus).toarray()
  
# Calculate the cosine similarity
similarity = np.dot(vectors[0], vectors[1])/(np.linalg.norm(vectors[0])* np.linalg.norm(vectors[1]))
print("Similarity between the 2 texts: {}".format(similarity))