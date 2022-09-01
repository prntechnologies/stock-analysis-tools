# stock-analysis-tools

This readme defines what the intention is for this set of tools to perform stock analysis.

## Dependencies
The primary dependency is to make sure that you have Python3 installed on your system.

Numpy (for Ubuntu)
Numpy is a package  for scienctific computing with Python
```bash
sudo apt-get install python3-numpy
```

SciPy
SciPy provides algorithms for optimization, integration, statistics and many
other math tools in Python
```bash
sudo apt-get install python3-scipy
```

Python PIP
Package installer for Python
```bash
sudo apt-get install pip
```

StatsModels
Provides classes and functions for the estimation of many different statistical models
```bash
python3 -m pip install statsmodels
```

MatPlotLib
A comprehensive library for creating static, animated, and interactive visualizations
in Python
```bash
sudo apt-get install python3-matplotlib
```

TermColor
Color formatting for output in terminal
```bash
python3 -m pip install termcolor
```

Yahoo Financials
Returns stock, cryptocurrency, forex, mutual fund, commodity futures, ETF, and 
US Treasury financial data from Yahoo Finance.
```bash
python3 -m pip install yahoofinancials
```

## Installation
Verify that all of hte dependencies have been installed on your system.  

Installation is accomplished by creating a folder to store the scripts.  Within the
installation folder, create a "data" folder and "reports" folder.  

The "data" folder will keep a copy of the price data that was downloaded for a given 
stock symbol.  The results "folder" will be used to store the resulting reports which
currently consists of MACD charts as well as RSI charts for each of the stocks in the 
"watchlist.dat" file.

## Executing
To execute the script type the following:
```bash
python3 main.py
```
The script will start by loading all of the stock symbols in the "watchdog.dat" file.
It will then download stock data from the Yahoo Finance website and produce MACD charts
and RSI charts for each stock.