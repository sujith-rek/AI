#  Markov regime-switching regression
# 1. MCMC: 10+10
# Perform Markov regime switching modelling and plot the regimes in the time series.
# Print the transition probabilities.
# Predict the future regimes for 5 time steps

import pandas as pd
import os

# if file s&p500.csv is not present, download it from yahoo finance
if not os.path.isfile('s&p500.csv'):
    import yfinance as yf
    data = yf.download('^GSPC', start="2000-01-01", end="2021-04-30")
    data.to_csv('s&p500.csv')

# read the data from s&p500.csv
data = pd.read_csv('s&p500.csv')

# Date,Open,High,Low,Close,Adj Close,Volume





