#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:28:06 2022

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

import argparse
import math
import numpy as np
import scipy.stats as scs
import statsmodels.api as sm
import pandas as pd
import datetime as dt
from pylab import mpl, plt
from termcolor import colored as cl
from math import floor

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# local libraries
import macd
import file_io
import relative_strength

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
        
class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        # Create toolbar, passin canvas as first parameter
        toolbar = NavigationToolbar(sc,self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

def getData(start_date, end_date, stock, verbose=False):
    if verbose is True:
        print("Getting stock " + stock)
    
    stock_data = file_io.get_data(stock);
    
    # generate a query to get the MACD data
    macd_query = "date >= '" + start_date + "' & date <= '" + end_date + "'"
    
    # now get the stock data for the MACD data range
    data_range = stock_data.query(macd_query)
    
    if verbose is True:
        print("Calculating MACD")
    
    macd_results = macd.get_macd(stock, data_range, 26, 12, 9)
    macd.plot_mach(stock, macd_results['close'], macd_results['macd'], macd_results['signal'], macd_results['hist'])
    
    if verbose is True:
        print("Calculating Relativce Strength")
    
    rsi = relative_strength.calc_relative_strength(data_range)
    relative_strength.plot_rsi(stock, rsi)


###################################################matplotlib.backends.backend_qt5agg##################
### Main Application
#####################################################################

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action='store_true', help="include debugging output")
    parser.set_defaults(verbose=False)
    args = parser.parse_args()
    print(args.verbose)

    # get today's date
    today = dt.datetime.today()
    # convert it to a string
    today_str = str(today).split()[0]

    # Get the MACD Date (24 weeks in the past)
    back_date = today - dt.timedelta(weeks=24)
    # convert the MACD dat to a string.
    back_date_str = str(back_date).split()[0]

    watchlist = file_io.get_watchlist()

    app = QtWidgets.QApplication([])
    w = MainWindow()

    for stock in watchlist:
        getData(back_date_str, today_str, stock, args.verbose)

    app.exec_()

if __name__ == '__main__':
    main()
