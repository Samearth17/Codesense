import gym
import numpy as np

# Set up the environment
env = gym.make('CartPole-v0')

# Set hyperparameters 
learning_rate = 0.01
n_episodes = 1000
max_steps_per_episode = 1000

# Initialize the q-table
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Reinforce the agent
for episode in range(n_episodes):
 # Reset the environment
 observation = env.reset()

 # Initialize reward
 total_reward = 0

 # Iterate over the episode
 for t in range(max_steps_per_episode):
 # Sample action
 action = np.argmax(q_table[observation, :])

 # Take an action
 observation_next, reward, done, info = env.step(action)

 # Update the q-table
 q_table[observation, action] = \
 q_table[observation, action] + \
 learning_rate * (reward + np.max(q_table[observation_next, :]) \
 - q_table[observation, action])

 # Update the total reward and the observation
 total_reward += reward
 observation = observation_next

 # End the episode if done
 if done:
 break

# Print out the total reward
print('Total Reward:', total_reward)