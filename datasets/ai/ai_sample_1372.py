import random

# Set the number of turns
MAX_GUESSES = 5

# Create an empty list that will contain the guessed letters
guessed_letters = []

# Welcome the user
print("Welcome to Hangman!")

# Generate a random word
with open("words.txt", "r") as f:
    words = f.read().splitlines()
word = random.choice(words)

# Create a list for the hidden word
hidden_word = ["_" for i in range(len(word))]

# Main game loop
for i in range(MAX_GUESSES):
    # Print the current state of the game
    print("\nTurn {}".format(i+1))
    print(" ".join(hidden_word))
    print("Letters guessed: {}".format("".join(guessed_letters)))
    
    # Get a guess from the user
    guess = input("Enter a letter: ")
    guessed_letters.append(guess)
    
    # Update the hidden_word with the guessed letter
    if guess in word:
        indices = [i for i, x in enumerate(word) if x == guess]
        for index in indices:
            hidden_word[index] = guess
    
    # Check if the user won
    if "_" not in hidden_word:
        print("You Win!")
        break

# Check for a loss
if "_" in hidden_word:
    print("You Lose! The word was {}.".format(word))