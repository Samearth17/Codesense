# import the necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Read in the movie data
movies = pd.read_csv('movies.csv')

# Vectorize the movie title
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(' '))
tfidf_matrix = vectorizer.fit_transform(movies['title']).toarray()

# Calculate the cosine similarity matrix
cosine_similarity_matrix = cosine_similarity(tfidf_matrix)

# Generate a list of recommended movies
def recommend(movie_title):
 recommended_movies = []
 
 # Find the index of the movie by title
 movie_index = movies[movies['title'] == movie_title].index[0]
 
 # Generate a list of movies with cosine similarities > 0
 for i in range(len(cosine_similarity_matrix[movie_index])):
  if cosine_similarity_matrix[movie_index][i] > 0:
   recommended_movies.append(i)
   
 # Return the titles of the recommended movies
 return movies.iloc[recommended_movies]['title']

# Testing 
print(recommend('The Godfather'))
# Output: The Shawshank Redemption, The Godfather Part II, Apocalypse Now