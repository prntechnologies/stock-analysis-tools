"""
Created on Tue Oct 25 12:11:00 2022

@author: phil

License Notice:
This file is part of the Stock Analysis Toolset.

The Stock Analysis Toolset is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or (at your 
option) any later version.

Stock Analysis Toolset is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warrant of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with 
the Stock Analysis Toolset.  If not, see <https://www.gnu.org/licenses/>.
"""

""" Acknowledgements:
    This environment was developed using a fork from notadam and his 
    Stock-Trading-Environment source code.
    https://github.com/notadamking/Stock-Trading-Environment"""

import gym
from gym import spaces
import pandas as pd
import numpy as np

MAX_REWARD = 2147483647

class stock_env(gym.Env):
    """ This class represents a OpenAI gym environment for the stock market."""
    metadata = {'render.modes': ['human']}

    def __init__(self, df):
        super(stock_env, self).__init()

        self.df = df
        self.reward_range = (0, MAX_REWARD)

        