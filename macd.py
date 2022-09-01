#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:00:00 2022

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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_mach(ticker, prices, macd, signal, hist):
    ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)
    ax2 = plt.subplot2grid((8,1), (5,0), rowspan = 3, colspan = 1)
    
    ax1.plot(prices)
    ax2.plot(macd, color = 'grey', linewidth = 1.5, label = 'MACD')
    ax2.plot(signal, color = 'skyblue', linewidth = 1.5, label = 'SIGNAL')
    
    
    for i in range(len(prices)):
        if str(hist[i])[0] == '-':
            ax2.bar(prices.index[i], hist[i], color = '#ef5450')
        else:
            ax2.bar(prices.index[i], hist[i], color = '#26a69a')
            
    plt.legend(loc = 'lower left')
    
    plt.savefig("./reports/" + ticker + "_macd.png")
    
def get_macd(ticker, data, slow, fast, smooth):
    fastclose = data['close']
    slowclose = data['close']
    
    # Calculate the "fast" moving average
    exp1 = fastclose.ewm(span = fast, adjust = False).mean()
    # Calculate the "slow" moving average
    exp2 = slowclose.ewm(span = slow, adjust = False).mean()
    
    # MACD Line = FAST LENGTH EMA - SLOW LENGTH EMA
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'close':'macd'})
    # Signal Line = MACD EMA 
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    
    # Histogram is the MACD LINE - SIGNAL LINE
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    
    # create a new datastore with the new columns
    frames = [data, macd, signal, hist]
    df = pd.concat(frames, join = 'inner', axis = 1)
    
    return df
