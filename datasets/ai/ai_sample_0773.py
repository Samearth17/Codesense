import pandas as pd

# Load data
movies = pd.read_csv('dataset/movies.csv')

# Create recommendations based on user interests
def recommend_movies(interests):
 # Create a list of movies based on user interests
 recommended_movies = movies[movies['Genre'].isin(interests)]
 # Sort movies by popularity
 recommended_movies = recommended_movies.sort_values('Popularity', ascending=False)
 
 return recommended_movies[['Title', 'Rating', 'Genre']]

# Use the function to get recommendations
recommend_movies(['Sci-Fi', 'Horror'])