# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:38:35 2020

@author: PC
"""

import pandas as pd
import yfinance as yf

CORN = yf.download(tickers = 'CORN', period ='2y')
SOYB = yf.download(tickers = 'SOYB', period = '2y')
WEAT = yf.download(tickers = 'WEAT', period = '2y')

data = [CORN["Close"], SOYB["Close"], WEAT["Close"]]
headers = ["Corn", "Soyb", "Weat"]
df = pd.concat(data, axis = 1, keys = headers)

print(df.head())
