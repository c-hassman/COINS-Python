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
# 4) Concatenated Data into a single dataframe
data = [CORN["Close"], SOYB["Close"], WEAT["Close"]] #create list of proper columns
headers = ["Corn", "Soyb", "Weat"] #create list of dataframe column names
df = pd.concat(data, axis = 1, keys = headers) #concatenate the lists into a dataframe, 
# assigning headers as the column names

#%%
# 5) Subsetting data (WEAT)
# there are so many ways to do this. The index of the datastructures are all dates
# and pandas works extremely well with dates (IMO much better than R)
# Here I illustrate one possible way to subset. The instructions were vague enough
# that you could have also subseted the original dataframe. 
WEAT_subset = df["Weat"]['June 1, 2019':]

#%%
# 6) Percent of time closed above the current price
# This could be done in one line, much more succinctly, but I am breaking it out into
# steps to illustrate what is happening

#first lets find the previous close
prev_close = WEAT_subset[-1]
#use boolean logic to return a vector of True and False
weat_bool_vector = WEAT_subset > prev_close 
# like R (and other languages), python counts True as 1 and False as 0
# thus we can get the count of True by summing the vector
true_count = weat_bool_vector.sum()
# to get the pecercent above, we need the total acount
total_count = WEAT_subset.count() #could also use len(WEAT_subset)
# calculate percent
per_above = true_count/total_count
print(per_above)
#%%
# Lets do it one line
per_above_1 = (WEAT_subset > WEAT_subset[-1]).sum()/WEAT_subset.count()
print(per_above_1)
#%%
# 7) Daily Returns
# Just for fun, here are three common ways to calculate percent changes
WEAT_subset_df = pd.DataFrame(WEAT_subset) #first lets convert our Series into a Dataframe
WEAT_subset_df['lagged'] = WEAT_subset_df['Weat'].shift(1) #create a column of the lagged series
#%%
# Method 1
WEAT_subset_df["Percent_A"] = ((WEAT_subset_df['Weat']- WEAT_subset_df['lagged']) / WEAT_subset_df['Weat']) * 100
# Method 2: Log returns
# for this we need log function from numpy
import numpy as np
WEAT_subset_df['Percent_B'] = (np.log(WEAT_subset_df['Weat']/WEAT_subset_df['lagged']))* 100
# Method 3: Easy way
# pandas provides a really easy way to do percent changes
WEAT_subset_df["Percent_C"] = WEAT_subset_df['Weat'].pct_change() * 100
print(WEAT_subset_df)
# You will notice small differences between the recutnrs calculated 
#%%
# Largest Daily increase
# Here I show three ways to do it
print(WEAT_subset_df['Percent_C'].max()) # this returns the value, but I want the whole row
print(WEAT_subset_df[WEAT_subset_df['Percent_C'] == WEAT_subset_df["Percent_C"].max()]) #returns row
print(WEAT_subset_df.loc[WEAT_subset_df['Percent_C'].idxmax()]) # this also works

#%%
# Largest Daily decrease
print(WEAT_subset_df[WEAT_subset_df['Percent_C'] == WEAT_subset_df['Percent_C'].min()])

#%%
# Largest Absolute
# we obviously already know it from the increase/decrease, but we can just double check
print(WEAT_subset_df["Percent_C"].abs().max())