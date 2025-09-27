import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# some numbers show up as 1,170,000,000 (commas)
# some numbers have references in square brackets after them
non_decimal = re.compile(r'[^\d]+')

for line in open('data/moore.csv'):
    r = line.split('\t')

    # x - year
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    # y - transistor count
    y = int(non_decimal.sub('', r[1].split('[')[0]))

    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

# display exp scatter plot
plt.scatter(X,Y)
plt.show()

# to display linear-ish scatter plot
Y = np.log(Y)
plt.scatter(X,Y)
plt.show()

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

Yhat = a*X + b

plt.scatter(X,Y)
plt.plot(X, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()

r2 = 1 - d1.dot(d1) / d2.dot(d2)

print(f"a: {a} b: {b}")
print(f"the r-squared is: {r2}")


# tc - transistor count
# log (tc) = a * year + b
# tc = exp(b) * exp(a * year)
# 2*tc = 2 *exp(b) * ex(a*year) = exp(ln(2)) * exp(b) * exp(a *year)
#      = exp(b) * exp(a * year + ln(2))
# exp(b)*exp(a*year2) = exp(b)*exp(a*year1 + ln2)
# a*year2 = a*year1 + ln2
# year2 = year1 + ln2/a

print(f"time to double: {np.log(2)/a} years")
