import random

# Initialize the game
level = 1
points = 0

while True:
 # Randomly generate the level
 level = random.randint(1, 10)
 
 # Print out the level and ask for input
 print('Level {}'.format(level))
 user_input = input()
 
 # Logic for checking the input
 if user_input == 'correct':
 points += 10
 elif user_input == 'wrong':
 break

# Print out the result
print('Points:', points)