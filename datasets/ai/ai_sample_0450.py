def movie_recommender_system(user):
    """
    This function uses a collaborative filtering algorithm 
    to suggest movies to the given user
    """
    # Get the list of rated movies by the user
    user_movies = user.get_rated_movies()

    # Get the list of ratings given by other users
    user_ratings = user.get_ratings()

    # Calculate the similarity between the user and other users
    user_similarity = user.calculate_similarity(user_movies, user_ratings)

    # Get the list of movies rated highly by other users
    other_rated_movies = user.get_top_rated_movies(user_ratings) 

    # Find the movies which the user has not seen so far, but recommended by other users
    unseen_movies = [m for m in other_rated_movies if m not in user_movies]
    
    # Sort the movies based on their similarity and the ratings given by other users
    sorted_movies = sorted(unseen_movies, 
                            key=lambda m: user_similarity[m] * user_ratings[m], 
                            reverse=True)
    
    # Get the top 10 movies
    top_movies = sorted_movies[:10]

    return top_movies