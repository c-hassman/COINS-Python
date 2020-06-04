# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:07:35 2020

@author: PC
"""

# Week 2 Key

# Here is the key to Week 2
# This is one possible solutions, but there are many, many other ways 
# This can be done. Probably some are better than this way

#-----------Import Necessary Packages------------#
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib import style
from matplotlib.mplfinance import candlestick2_ohlc
#%%
IAU = yf.download(tickers = 'IAU', period = '1y') #download the IAU ETF for the last year
#%%
IAU['Close'].plot()
plt.title("IAU ETF")
plt.ylabel('Price ($)')

#%%
fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, IAU.values, width=2, colorup='g')

# This does not work. Maybe go back to see in which books you did this succesfully
# be sure to change the riginal indstructions. 