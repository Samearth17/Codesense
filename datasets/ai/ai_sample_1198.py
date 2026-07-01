import gym
import numpy as np
   
# Set up the environment
env = gym.make('CartPole-v1')
env.reset()

# Define the hyperparameters
learning_rate = 0.01
discount = 0.95
episodes = 5000

# Discretize the state space of the environment
NUMBER_OF_BUCKETS = (1, 1, 6, 3)  # (x, x', theta, theta')
state_bounds = list(zip(env.observation_space.low, env.observation_space.high))
state_bounds[1] = [-0.5, 0.5] # Limit x velocity as it only goes from -0.5 to 0.5
state_bounds[3] = [-math.radians(50), math.radians(50)] # Limit theta as it goes from -50 to 50 degrees

# Create the Q-table
q_table = np.zeros(NUMBER_OF_BUCKETS + (env.action_space.n,))
  
# Train the agent
for episode in range(episodes):
 done = False
 state = env.reset()

 # Discretize the state
 state_discrete = [np.digitize(s, bins=bounds) for s, bounds in zip(state, state_bounds)]
 
 # Repeat until the episode is done
 while not done:
 # Choose an action
 action = np.argmax(q_table[state_discrete])

# Perform the action
 state, reward, done, _ = env.step(action)
  
# Discretize the new state
 state_discrete = [np.digitize(s, bins=bounds) for s, bounds in zip(state, state_bounds)]

# Update the Q-table
 q_table[state_discrete + (action,)] = reward + discount * np.max(q_table[state_discrete])

# Print out the Q-table
print(q_table)