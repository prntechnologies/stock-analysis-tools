#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:16:00 2022

@author: phil
"""

import pandas as pd
from datetime import datetime, timedelta
from yahoofinancials import YahooFinancials

import os.path

DATAFILE_PATH = "./data/"
DATAFILE_EXT = ".csv"

def build_filename(ticker):
    filename = DATAFILE_PATH + ticker + DATAFILE_EXT
    
    return filename

def data_exists(ticker):
    exists = False
    
    fn = build_filename(ticker)
    
    print("Filename = " + fn)
    if os.path.isfile(fn):
        print("File Exists")
        exists = True
    
    return exists

def download_data(ticker, start, end):
    
    yahoo_financials = YahooFinancials(ticker)

    data = yahoo_financials.get_historical_price_data(start_date = start, 
                                                      end_date = end,
                                                      time_interval= 'daily')
    data_df = pd.DataFrame(data[ticker.upper()]['prices'])
    
    if data_df.size > 0:
        # clean up the data
        data_df = data_df.drop('date', axis=1).set_index('formatted_date')
        data_df.index.names = ["date"]

    return data_df

def update_data(ticker):
    return

def get_data(ticker):
    fn = build_filename(ticker)

    # get the current date.  We're getting it here because we're going to use
    # it in either case of the if statement below.
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    today_str = now.strftime("%Y-%m-%d")
    
    if data_exists(ticker):
        data = pd.read_csv(fn, index_col=0, parse_dates=False)
        # Check the last entry in the file.
        last_date_str = data.index[-1]
        first_day = datetime.strptime(last_date_str, '%Y-%m-%d')
        first_day_str = (first_day + timedelta(days=1) ).strftime("%Y-%m-%d")
        
        #add  
        #last_date_str = last_date.strftime("%Y-%m-%d")
        
        if (today_str > last_date_str):
            #new_data = download_data(ticker, first_day_str, today_str)
            new_data = download_data(ticker, first_day_str, tomorrow_str)
            
            if new_data.size > 0:
                data = data.append(new_data)
        
    else:
        print("File doe not exist")
    
        data = download_data(ticker, '1800-01-01', today_str)
    
    if data.size > 0:
        data.to_csv(fn, index=True)
        
        print(data.head())
        print(data.tail())
        
    return data

def get_watchlist():
    filename = DATAFILE_PATH + "watchlist.dat"
    
    # Using readlines()
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    # strip out all of the whitespace and newlines at the end.
    Lines = [line.rstrip() for line in Lines]
    
    return Lines