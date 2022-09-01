#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:34:26 2022

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