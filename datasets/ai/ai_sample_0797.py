# import required libraries
import pandas as pd

# define the rating scale
rating_scale = [1,2,3,4,5]

# create an empty DataFrame
rating_df = pd.DataFrame(columns=['Team', 'Rating'])

# function to take in user input and add it to the DataFrame
def add_rating(team, rating):
    rating_df = rating_df.append({'Team': team, 'Rating': rating}, ignore_index=True)

# function to allow a user to rate a team
def rate_team():
    team = input('Which team would you like to rate? ')
    rating = input('Please enter a rating between 1 and 5: ')
    if rating not in rating_scale:
        print('Error: Rating must be between 1 and 5!')
        rate_team()
    else:
        add_rating(team, rating)
        print('Rating added successfully!')

# call the rate_team() function
rate_team()