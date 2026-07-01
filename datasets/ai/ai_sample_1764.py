import random 

# Dictionary with all possible choices
choices = {"rock": 0, "paper": 1, "scissors": 2}

# A dictionary to store the results
results = {0:0, 1:0, 2:0}

# Number of rounds to be performed
rounds = 3

# Main game loop
for i in range(rounds):
    # Generate random player choices 
    user_choice = random.choice(list(choices.keys()))
    computer_choice = random.choice(list(choices.keys()))
    # Evaluate who won
    user_choice_val = choices[user_choice]
    computer_choice_val = choices[computer_choice]
    if user_choice_val == computer_choice_val:
        result = 0
    elif user_choice_val > computer_choice_val or (user_choice_val == 2 and computer_choice_val == 0):
        result = 1
    else:
        result = 2
    # Update the results dictionary
    results[result] += 1 

print("User Score: ", results[1])
print("Computer Score: ", results[2])