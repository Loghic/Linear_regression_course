import numpy as np
import matplotlib.pyplot as plt

# Load the data
X = []
Y = []

for line in open('data/data_poly.csv'):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x*x])
    Y.append(float(y))

# Convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot to see what the data looks like
plt.scatter(X[:,1], Y)
plt.show()

# calculate weights
w = np.linalg.solve(X.T @ X, X.T @ Y)
Yhat = X @ w

# plot it all together (can draw lines between all points if not sorted)
# plt.scatter(X[:,1], Y)
# plt.plot(X[:,1], Yhat)
# plt.show()

# plot it all together (but sort it)
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.show()

# determine how good the model is by computing the r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - ((d1 @ d1) / (d2 @ d2))
print(f"the r-squred is: {r2}")
