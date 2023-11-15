# 2. Bayesian Belief Networks: 10*4=40
# Problem Statement:
# You are given a dataset containing information about weather conditions (Temperature,
# Humidity, Wind, and Outlook) and whether people played tennis or not. Your task is to
# implement a Bayesian Belief Network (BBN) to predict whether people will play tennis based on
# the given weather conditions.
# Requirements:
# 1. Implement a Bayesian Belief Network (BBN) from scratch using a programming language of
# your choice (e.g., Python, Java, etc.).
# 2. The BBN should consist of nodes representing the following variables: Temperature,
# Humidity, Wind, Outlook, and PlayTennis.
# 3. Use the dataset provided to learn the conditional probability tables (CPTs) for each node.
# 4. Implement the inference algorithm (e.g., Variable Elimination) to make predictions about
# whether people will play tennis given specific weather conditions.
# Dataset:
# | Outlook | Temperature | Humidity | Wind | PlayTennis |
# |---------|-------------|----------|------|------------|
# | Sunny | Hot | High | Weak | Yes |
# | Sunny | Hot | High | Strong | No |
# | Overcast | Hot | High | Weak | Yes |
# | Rain | Mild | High | Weak | Yes |
# | Rain | Cool | Normal | Weak | Yes |
# | Rain | Cool | Normal | Strong | No |
# | Overcast | Cool | Normal | Strong | Yes |
# | Sunny | Mild | High | Weak | No |
# | Sunny | Cool | Normal | Weak | Yes |
# | Rain | Mild | Normal | Weak | Yes |
# | Sunny | Mild | Normal | Strong | Yes |
# | Overcast | Mild | High | Strong | Yes |
# | Overcast | Hot | Normal | Weak | Yes |
# | Rain | Mild | High | Strong | No |


import pandas as pd
from pgmpy.models import BayesianNetwork as BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Define the dataset
data = pd.DataFrame(data={
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Define the structure of the BBN
model = BayesianModel([('Outlook', 'PlayTennis'), ('Temperature', 'PlayTennis'), ('Humidity', 'PlayTennis'), ('Wind', 'PlayTennis')])

# Learn the CPTs
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Implement the inference algorithm
inference = VariableElimination(model)
print(inference.query(variables=['PlayTennis'], evidence={'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak'}))



