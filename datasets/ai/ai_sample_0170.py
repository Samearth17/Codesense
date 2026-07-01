import random 
  
# printing the board  
def drawBoard(board): 
  
    print("---------------") 
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ") 
    print("___|___|___") 
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ") 
    print("___|___|___") 
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ") 
    print("   |   |   ") 
  
# defining the part of the game  
def checkWin(board, player): 
    return ( 
        (board[1] == board[2] == board[3] == player) or
        (board[5] == board[4] == board[6] == player) or 
        (board[7] == board[8] == board[9] == player) or 
        (board[1] == board[5] == board[9] == player) or 
        (board[3] == board[5] == board[7] == player) or 
        (board[1] == board[4] == board[7] == player) or 
        (board[2] == board[5] == board[8] == player) or 
        (board[3] == board[6] == board[9] == player))  
       
def getComputerSpot(board,player): 
    openSpots = [] 
    indices = [i for i, spot in enumerate(board) if spot == '-'] 
    
    for i in indices: 
        board[i] = player  
          
        if checkWin(board, player):  
            board[i] = '-'  
            return i  
        board[i] = '-'  
          
    for i in indices: 
        openSpots.append(i) 
    if len(openSpots): 
        return random.choice(openSpots) 
    else: 
        return None 
      
                
def playGame(): 
    board = ['-' for x in range(10)] 
    won = False
    turn = -1
    while not won: 
        if turn == -1: 
            # human turn   
            humanSpot = int(input("Enter your spot: "))
            if board[humanSpot] == '-': 
                board[humanSpot] = 'X' 
            else: 
                print("the spot is already filled!") 
                continue
            turn *= -1
       
        if checkWin(board,'X'): 
            drawBoard(board) 
            print("You won!") 
            won = True
            break
          
        if turn == 1: 
            # computer turn  
            computerSpot = getComputerSpot(board,'O') 
            if computerSpot == None: 
                drawBoard(board) 
                print("The game is drawn!")
                break
            else: 
                board[computerSpot] = 'O' 
            turn *= -1
              
        drawBoard(board) 
          
playGame()