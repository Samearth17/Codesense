# We define the possible winning combination of the game
WINNING_COMBINATION = {
  "rock": "scissors",
  "paper": "rock",
  "scissors": "paper"
}

def playRockPaperScissors():
  # Player 1's turn
  player1_choice = input("Player 1: Choose rock, paper or scissors: ")
  # Player 2's turn
  player2_choice = input("Player 2: Choose rock, paper or scissors: ")

  # Find the winner
  if WINNING_COMBINATION[player1_choice] == player2_choice:
    print("Player 1 has won.")
  elif WINNING_COMBINATION[player2_choice] == player1_choice:
    print("Player 2 has won.")
  else:
    print("It's a tie!")

playRockPaperScissors()