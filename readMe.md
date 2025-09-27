# Simple Linear Regression: Expanding Dot Products into Sums

## Step 1: Interpret the operations

We work with vectors:

$$
X = (x_1, x_2, \dots, x_n), \quad Y = (y_1, y_2, \dots, y_n)
$$

The operations used in code can be written in summation notation as follows:

- Dot product of \(X\) with itself:

$$
X.dot(X) = X \cdot X = \sum_{i=1}^n x_i^2
$$

- Dot product of \(X\) and \(Y\):

$$
X.dot(Y) = X \cdot Y = \sum_{i=1}^n x_i y_i
$$

- Mean of \(X\) (often written as \(\bar{x}\)):

$$
\bar{x} = X.\text{mean()} = \frac{1}{n} \sum_{i=1}^n x_i
$$

- Mean of \(Y\) (often written as \(\bar{y}\)):

$$
\bar{y} = Y.\text{mean()} = \frac{1}{n} \sum_{i=1}^n y_i
$$

- Sum of \(X\):

$$
X.\text{sum()} = \sum_{i=1}^n x_i
$$

## Step 2: Linear regression coefficients

- Slope \(a\):

$$
a = \frac{\sum_{i=1}^n x_i y_i - n \bar{x} \bar{y}}{\sum_{i=1}^n x_i^2 - n \bar{x}^2}
$$

- Intercept \(b\):

$$
b = \bar{y} - a \bar{x}
$$

- Predicted value $\(\hat{y}_i\)$ (using "hat" notation):

$$
\hat{y}_i = a x_i + b
$$

