import random 
 
num = random.randint(1,10)
guess = 0
attempts = 0
 
while guess != num and attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == num:
        print("You guessed correctly in", attempts, "attempts")
    elif guess > num:
        print("Too High")
    else:
        print("Too Low")
if guess != num:    
    print("You failed to guess the number")