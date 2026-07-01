import random

# Possible game outcomes
outcomes = ['rock', 'paper', 'scissors']

# Print a welcome message
print('Welcome to Rock, Paper, Scissors!')

# Prompt for the user's choice
user_choice = input('What is your choice? rock/paper/scissors\n')

# Validate the user's choice
if user_choice not in outcomes:
    print('Invalid choice!')
    exit()

# Generate a random choice
computer_choice = random.choice(outcomes)

# Compare the choices
if user_choice == computer_choice:
    print('It\'s a tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('Computer wins!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'scissors':
    print('Computer wins!')
elif user_choice == 'scissors' and computer_choice == 'rock':
    print('Computer wins!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')

# Print the choices
print(f'You chose {user_choice}, computer chose {computer_choice}')