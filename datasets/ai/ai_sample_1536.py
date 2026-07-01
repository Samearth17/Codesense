import random

random_number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100. Can you guess it?')

while True:
	guess_str = input('Enter your guess: ')
	guess = int(guess_str)

	if guess == random_number:
		print('Congratulations! You guessed it correctly.')
		break
	elif guess < random_number:
		print('Your guess is too low.')
	else:
		print('Your guess is too high.')