#  Markov regime-switching regression
# 1. MCMC: 10+10
# Perform Markov regime switching modelling and plot the regimes in the time series.
# Print the transition probabilities.
# Predict the future regimes for 5 time steps

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# if file s&p500.csv is not present, download it from yahoo finance
if not os.path.isfile('s&p500.csv'):
    import yfinance as yf
    data = yf.download('^GSPC', start="2000-01-01", end="2021-04-30")
    data.to_csv('s&p500.csv')

# read the data from s&p500.csv
data = pd.read_csv('s&p500.csv')

# Date,Open,High,Low,Close,Adj Close,Volume

model = sm.tsa.MarkovRegression(data['Adj Close'], k_regimes=2, trend='n', switching_variance=True)
model_fit = model.fit()

# print the transition matrix
print(model_fit.expected_durations)

# plot the regimes
plt.figure(figsize=(10, 8))
plt.plot(model_fit.smoothed_marginal_probabilities[0], label='Regime 0')
plt.plot(model_fit.smoothed_marginal_probabilities[1], label='Regime 1')
plt.legend()
plt.title('Regime switching')
plt.show()

# predict the future regimes
print(model_fit.predict(5))







