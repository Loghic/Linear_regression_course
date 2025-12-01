import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
The data (X1, X2, X3) are for each patient.
X1 = systolic blood pressure
X2 = age in years
X3 = weight in pounds
"""

# Load data
# explicitly tell pandas which engine to use for .xls
df = pd.read_excel('data/mlr02.xls', engine='xlrd')

# convert dataframe to numpy array
X = df.to_numpy()

# using age to predict systolic blood pressure
plt.scatter(X[:,1], X[:,0])
plt.show()
# looks pretty linear!

# using weight to predict systolic blood pressure
plt.scatter(X[:,2], X[:,0])
plt.show()
# looks pretty linear!

# Spliting the data
df['ones'] = 1
Y = df['X1']
X = df[['X2', 'X3', 'ones']]

# we want to know if X2 or X3 predicts it well
X2only = df[['X2', 'ones']]
X3only = df[['X3', 'ones']]

# creating function for r-squared
def get_r2(X, Y):
    w = np.linalg.solve(X.T @ X, X.T @ Y)
    Yhat = X @ w

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1) / d2.dot(d2)

    return r2

print(f"r2 fo x2 only: {get_r2(X2only, Y)}")
print(f"r2 fo x3 only: {get_r2(X3only, Y)}")
print(f"r2 for both: {get_r2(X, Y)}")


