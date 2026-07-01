import random

# list of possible answers
possible_responses = [
 'We serve a variety of dishes - from salads to pizzas to steaks!',
 'Check out our menu for a full list of options',
 'We serve a variety of dishes, including traditional Italian, Mexican, and American fare. What would you like to try?',
 'We have a great selection of meals! What kind of dish are you looking for?',
 'We have a unique selection of meals - have you checked out our menu?'
]

# read the user's question
with open('random_user_question.txt') as user_question:
    question = user_question.read()

# choose a random response
response = random.choice(possible_responses)

# display the response to the user
print(response)