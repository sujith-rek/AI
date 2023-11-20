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
    try:
        import yfinance as yf
    except:
        os.system('pip install yfinance')
    
    import yfinance as yf
    data = yf.download('^GSPC', start="2000-01-01", end="2021-04-30")
    data.to_csv('s&p500.csv')


# read the data from s&p500.csv
data = pd.read_csv('s&p500.csv')

# Date,Open,High,Low,Close,Adj Close,Volume

model = sm.tsa.MarkovRegression(data['Adj Close'], k_regimes=3, trend='ct', switching_variance=True)
model_fit = model.fit()

# print the transition matrix
print(model_fit.expected_durations)

# plot the regimes
plt.figure(figsize=(10, 8))
plt.plot(model_fit.smoothed_marginal_probabilities[0], label='Regime 0')
plt.plot(model_fit.smoothed_marginal_probabilities[1], label='Regime 1')
plt.plot(model_fit.smoothed_marginal_probabilities[2], label='Regime 2')
plt.legend()
plt.title('Regime switching')
plt.show()

# print transition matrix
print(model_fit.expected_durations)

# predictions
transition_matrix = model_fit.expected_durations # [  1.00855706 452.45552742 524.38073604]
for i in range(5):
    print("Prediction for ",i,"th time step: ",transition_matrix)
    transition_matrix = np.matmul(transition_matrix,transition_matrix)







