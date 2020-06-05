# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:07:35 2020

@author: PC
"""

# Week 2 Key

# Here is the key to Week 2
# This is one possible solutions, but there are many, many other ways 
# this can be done. Probably some are better than this way. 

# For more practice with Matplotlib, spend some times playing with the 
# visualization attributes

#-----------Import Necessary Packages------------#
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
#%%
# Question 1
IAU = yf.download(tickers = 'IAU', period = '1y') #download the IAU ETF for the last year
#%%
# Question 2
# Plot the closing prices of IAU
IAU['Close'].plot()
plt.title("IAU ETF") # add title to the graph
plt.ylabel('Price ($)') # add y axis label to graph
#%%
# plot sandles, 
# change bar size
# export the figure to a file



#%%
# Question 5
IAU = yf.download(tickers = 'IAU', period = '2y') #download the IAU ETF for the last 2 years
SLV = yf.download(tickers = 'SLV', period = '2y') #download the IAU ETF for the last 2 years
#%%
# Question 6
# First I will assign the closing values to a new dataframe "data"
data = pd.DataFrame({
        'IAU' : IAU['Close'],
        'SLV' : SLV['Close']})
# Now I will calculate the log returns for each column
data['IAUr'] = data['IAU'].pct_change() * 100
data['SLVr'] = data['SLV'].pct_change() * 100
data = data.dropna() # drop all the of the NA values
#%%
# Question 7
plt.plot(data['IAUr'], data['SLVr'], 'o', color = 'black') # plot scatter plot 
plt.title('IAU versus SLV Returns') # Add title
plt.xlabel('IAU Daily Return (%)') # add x label
plt.ylabel('SLV Daily Return (%)') # add y label
# I am going to add a line of best fit. No worries if you don't understand the code yet
plt.plot(np.unique(data['IAUr']), np.poly1d(np.polyfit(data['IAUr'], data['SLVr'], 1))(np.unique(data['IAUr'])), 
         color = 'b')
# You can eyeball the strength of this relationship, or even run a correlation analysis of regress the two 
# on one another and look at the goodness of fit

#%%
# Question 8
# First I will manually set the bins. I do some extreme silver returns
bins = np.linspace(-7.5, 7.5, 100)

plt.hist(data['IAUr'], bins, alpha = 0.7, label = 'IAU Returns')
plt.hist(data['SLVr'], bins, alpha = 0.3, label = 'SLV Returns')
plt.legend(loc = 'upper right')

# You can see that the returns for the last two years are both 
# centered at 0.0 +/- 0.5 (what you would expect)
# Silver seems more volatile, with fatter tails
# A regression analysis of returns, or looking at the standard deviation could 
# support this claim. 

IAU_std = round(np.std(data['IAUr']), 2)
SLV_std = round(np.std(data['SLVr']), 2)

print("The standard deviation of daily returns for the last two years in IAU has been", str(IAU_std),  
      "compared to", str(SLV_std), "in SLV." )

     