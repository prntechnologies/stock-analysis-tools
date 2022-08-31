#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:21:24 2022

@author: phil
"""
import matplotlib.pyplot as plt

def calc_relative_strength(data):
    delta = data['close'].diff()
    up = delta.clip(lower = 0)
    down = -1 * delta.clip(upper = 0)
    ema_up = up.ewm(com=14, adjust = False).mean()
    ema_down = down.ewm(com=14, adjust = False).mean()
    
    rs = ema_up / ema_down
    
    data['RSI'] = 100 - (100/(1 + rs))
    
    # skip the first 14 days as they have no real value
    data = data.iloc[14:]
    
    return data

def plot_rsi(ticker, data):
    fig = plt.figure(facecolor='white')
    textsize = 9
    #axescolor = '#f6f6f6'  # the axes background color
    
    left, width = 0.1, 0.8
    rect1 = [left, 0.7, width, 0.2]
    ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)

    fillcolor = 'darkgoldenrod'
    
    ax1.plot(data.index, data['RSI'], color=fillcolor)
    ax1.axhline(70, color=fillcolor)
    ax1.axhline(30, color=fillcolor)
    ax1.fill_between(data.index, data['RSI'], 70, where=(data['RSI'] >= 70), facecolor=fillcolor, edgecolor=fillcolor)
    ax1.fill_between(data.index, data['RSI'], 30, where=(data['RSI'] <= 30), facecolor=fillcolor, edgecolor=fillcolor)
    ax1.text(0.6, 0.9, '>70 = overbought', va='top', transform=ax1.transAxes, fontsize=textsize)
    ax1.text(0.6, 0.1, '<30 = oversold', transform=ax1.transAxes, fontsize=textsize)
    ax1.set_ylim(0, 100)
    ax1.set_yticks([30, 70])
    ax1.text(0.025, 0.95, 'RSI (14)', va='top', transform=ax1.transAxes, fontsize=textsize)
    ax1.set_title('%s daily' % ticker)
    
    fig.show()
    plt.savefig("./reports/" + ticker + "_rsi.png")
    
