#importing necessary libraries
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

#Defining a function to calculate cosine similarity
def cosine_similarity(text):
   vectors = [t for t in text]
   cv = CountVectorizer()
   counts = cv.fit_transform(vectors)
   return cosine_similarity(counts)
   
#Declaring the corpus of documents
corpus = ['the goal of this search engine is to find documents similar to a query', 
          'the algorithm begins by vectorizing the query and the documents',
          'the query and documents are then compared using cosine similarity']
          
#Calculating similarity
similarity_matrix = cosine_similarity(corpus)

#Printing the cosine similarity matrix
print(similarity_matrix)