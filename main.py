#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:28:06 2022

@author: phil
"""

import math
import numpy as np
import scipy.stats as scs
import statsmodels.api as sm
import pandas as pd
import datetime as dt
from pylab import mpl, plt
from termcolor import colored as cl
from math import floor

# local libraries
import macd
import file_io
import relative_strength

#####################################################################
### Main Application
#####################################################################

# Pseudo-code for the operation of this app
# 1) Get list of stocks to analyze from an input file
# 2) Starting from the first, pull in data from datafile (if exists)
#       if it doesn't exist, pull in data from the web
# 3) 

# get today's date
today = dt.datetime.today()
# convert it to a string
today_str = str(today).split()[0]

# Get the MACD Date (24 weeks in the past)
back_date = today - dt.timedelta(weeks=24)
# convert the MACD dat to a string.
back_date_str = str(back_date).split()[0]

watchlist = file_io.get_watchlist()

count = 0

for stock in watchlist:
    print("Getting stock " + stock)
    stock_data = file_io.get_data(stock);
    
    # generate a query to get the MACD data
    macd_query = "date >= '" + back_date_str + "' & date <= '" + today_str + "'"
    #macd_query = "date < '" + today_str + "'"
    
    # now get the stock data for the MACD data range
    data_range = stock_data.query(macd_query)
    
    print("Calculating MACD")
    macd_results = macd.get_macd(stock, data_range, 26, 12, 9)
    macd.plot_mach(stock, macd_results['close'], macd_results['macd'], macd_results['signal'], macd_results['hist'])
    
    print("Calculating Relativce Strength")
    rsi = relative_strength.calc_relative_strength(data_range)
    relative_strength.plot_rsi(stock, rsi)