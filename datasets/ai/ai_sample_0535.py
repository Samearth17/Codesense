import random

# set the maximum number of guess
max_guesses = 5

# generate a random number
target_num = random.randint(1, 10)

# initialize number of guesses
num_guesses = 0

# prompt user for a guess
while num_guesses < max_guesses:
    user_guess = int(input("Guess a number between 1 and 10: "))
    
    # check if user guess is correct
    if user_guess == target_num:
        print("You have guessed the number correctly")
        break
    # check if user guess is greater or lesser
    elif user_guess > target_num:
        print("Your guess is greater than the target number")
    else:
        print("Your guess is lesser than the target number")
    num_guesses += 1

if num_guesses == max_guesses:
    print("You have reached your maximum number of guesses")