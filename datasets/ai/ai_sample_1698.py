import random

# Create the game board
board = ["_"] * 9

# Generate random numbers 
nums = random.sample(range(1,10), 2)

# Player 1 assigns O to two random positions
board[nums[0]] = "O"
board[nums[1]] = "O"

# Player 2 assigns X at random
nums = random.sample(range(1,10), 1)
board[nums[0]] = "X"

# Print out the game board
for i in range(9):
 if i % 3 == 0 and i != 0:
  print()
 print(board[i], end = " ")

print()