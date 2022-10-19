import gym
from gym import spaces

class trading_env(gym.Env):
    """ Custom Stock Trading Environment using gym 
    and its interface definition"""
    metadata = {'render.modes': ['human']}

    def __init__(self, arg1, arg2, ...):
        super(trading_env, self).__init__()

        # Define action and observation space
        # They must be gym.spaces objects

        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

    def step(self, action):
        # Execute one time stpe within the environment

    def reset(self):
        # Reset the state of the environment to an initial state

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        