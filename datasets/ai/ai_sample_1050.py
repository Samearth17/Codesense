from random import randint

def rock_paper_scissors():
    moves = ["rock", "paper", "scissors"]
    player_move = input("Choose rock, paper, or scissors: ")
    comp_move = moves[randint(0,2)]
    print(f"Computer's move is {comp_move}")
    if (player_move == comp_move):
        print("It's a tie!")
    elif (player_move == "rock" and comp_move == "scissors"): 
        print("You win!")
    elif (player_move == "rock" and comp_move == "paper"): 
        print("Computer wins!")
    elif (player_move == "paper" and comp_move == "scissors"): 
        print("Computer wins!")
    elif (player_move == "paper" and comp_move == "rock"): 
        print("You win!")
    elif (player_move == "scissors" and comp_move == "rock"): 
        print("Computer wins!")
    elif (player_move == "scissors" and comp_move == "paper"): 
        print("You win!")