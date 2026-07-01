import gym
import numpy as np

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

# Training hyperparameters
n_timesteps = 500000

# Create the environment
env = gym.make('Tetris-v0')
env = DummyVecEnv([lambda: env])

# Create the agent
model = PPO2(MlpPolicy, env, n_timesteps=n_timesteps)

# Train the agent
model.learn(total_timesteps=n_timesteps)

# Test the agent
env.reset()
state, done = env.reset(), False
total_reward = 0

while not done:
    action, _states = model.predict(state)
    state, reward, done, info = env.step(action)
    total_reward += reward # accumulate the reward

print('Total Reward: ', total_reward)