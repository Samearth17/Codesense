import random

# Create class for environment
class TicTacToeEnv():
    # Define initializer
    def __init__(self):
        self.state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.player = 'X'
        self.player_turn = 0
    
    # Define a reset method to set initial state
    def reset(self):
        self.state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.player = 'X'
        self.player_turn = 0
        return self.state
        
    # Define step function
    def step(self, action):
        # Set player mark
        self.state[action] = self.player
        # Check for winner
        winner = self.check_winner()
        done = False
        if winner == 'X' or winner == 'O':
            reward = 1
            done = True
        else:
            reward = 0
        # Switch players
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        # Check for draw and switch player turn
        if self.player_turn == 8:
            done = True
            reward = 0.5
        self.player_turn += 1
        # Return state, reward, done, info
        return self.state, reward, done, None
        
    # Define a method to check if someone has won
    def check_winner(self):
        win_state = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in win_state:
            if self.state[i[0]] == self.state[i[1]] == self.state[i[2]] == 'X':
                return 'X'
            if self.state[i[0]] == self.state[i[1]] == self.state[i[2]] == 'O':
                return 'O'
        return None

# Play a game
env = TicTacToeEnv()
env.reset()
done = False
while not done:
    action = random.randint(0, 8)
    state, reward, done, _ = env.step(action)
    print(env.state)
    if reward == 1 or reward == 0.5:
        print("Winner: "+str(reward))