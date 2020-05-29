# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:12:23 2020

@author: PC
"""

# Python for COINS
# Week 1 Key

# 2) Import Packages
import pandas as pd
import yfinance as yf

# 3) Import Data from yfinance

CORN = yf.download(tickers = 'CORN', period = '2y') #download the WEAT ETF for the last two years
SOYB = yf.download(tickers = 'SOYB', period = '2y') #download the WEAT ETF for the last two years
WEAT = yf.download(tickers = 'WEAT', period = '2y') #download the WEAT ETF for the last two years

#%%