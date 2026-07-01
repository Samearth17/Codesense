import numpy as np
import random 

class QLearner:
    def __init__(self, alpha=0.2, gamma=0.9):
        self.alpha = alpha
        self.gamma = gamma
        self.Q = dict()
    
    def get_Q(self, state, action):
        """
        Return Q-value for a given state and action.
        """
        return self.Q.get((state, action), 0.0)
    
    def learn_Q(self, state, action, reward, next_state):
        """
        Update the Q-value for a given state, action and reward.
        """
        QValue = self.get_Q(state, action) 
        next_QValue = max(self.get_Q(next_state, a) for a in self.get_legal_actions(next_state))
        new_QValue = (1 - self.alpha) * QValue + self.alpha * (reward + self.gamma * next_QValue)
        self.Q[(state, action)] = new_QValue
    
    def choose_action(self, state):
        """
        Select the best action from a given state.
        """
        best_action = None
        max_value = -np.inf
        actions = self.get_legal_actions(state)
        for action in actions:
            value = self.get_Q(state, action)
            if value > max_value:
                max_value = value
                best_action = action
        return best_action
    
    def get_legal_actions(self, state):
        """
        Return legal moves for the given game state.
        """
        # Return a list of legal actions for the given state.
        pass
    
    def learn(self):
        """
        Update Q-value based on the results of the game.
        """
        # Implement the learning part of the assignment.
        pass