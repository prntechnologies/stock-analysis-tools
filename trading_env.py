import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np

MAX_ACCOUNT_BALANCE = 2147483647
MAX_NUM_SHARES = 2147483647
MAX_SHARE_PRICE = 5000
MAX_OPEN_POSITION = 5
MAX_STEPS = 20000

INITIAL_ACCOUNT_BALANCE = 10000

class trading_env(gym.Env):
    """ Custom Stock Trading Environment using gym 
    and its interface definition"""
    metadata = {'render.modes': ['human']}

    def __init__(self, df):
        super(trading_env, self).__init__()

        self.df = df
        self.reward_range = (0, MAX_ACCOUNT_BALANCE)

        # Actions of the format Buy x%, Sell x%, Hold, etc.
        self.action_space = spaces.Box(
            low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)
        
        # Prices contain the OHCL values for the last five prices
        self.observation_space = space.Box(
            low = 0, high = 1, shape=(6, 6) dtype=float16)

    def _next_observation(self):
        # Get the stock data points for the last 5 days and scale to between 0-1
        framp = np.array
    def step(self, action):
        # Execute one time stpe within the environment

    def reset(self):
        # Reset the state of the environment to an initial state

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        