import random

movies = ["Guardians of the Galaxy",
          "The Godfather",
          "The Shawshank Redemption",
          "Pulp Fiction",
          "Inception",
          "The Dark Knight"]

def random_movie_selector(movies):
    return random.choice(movies)
  
# Driver Code 
print(random_movie_selector(movies)) 

# Output (Example): 
# The Shawshank Redemption