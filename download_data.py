#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:34:26 2022

@author: phil
"""

import pandas as pd
import yfinance as yf


yahoo_financials = YahooFinancials('GE')

data = yahoo_financials.get_historical_price_data(start_date = '1800-01-01', 
                                                  end_date = '2019-12-31',
                                                  time_interval= 'daily')
tsla_df = pd.DataFrame(data['GE']['prices'])
tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
print (tsla_df.head())

data_type = yahoo_financials.get_stock_quote_type_data()

print (data_type)