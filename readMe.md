# Linear Regression: From Simple to Multiple Variables

## Part 1: Simple Linear Regression

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

- Mean of \(X\) (often written as $\(\bar{x}\)$):

$$
\bar{x} = X.\text{mean()} = \frac{1}{n} \sum_{i=1}^n x_i
$$

- Mean of \(Y\) (often written as $\(\bar{y}\)$):

$$
\bar{y} = Y.\text{mean()} = \frac{1}{n} \sum_{i=1}^n y_i
$$

- Sum of \(X\):

$$
X.\text{sum()} = \sum_{i=1}^n x_i
$$

---

## Step 2: Denominator

The denominator used in slope and intercept formulas:

$$
\text{denominator} = X.dot(X) - X.mean() \cdot X.sum()
= \sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i
= \sum_{i=1}^n x_i^2 - \frac{1}{n} \Big(\sum_{i=1}^n x_i\Big)^2
$$

---

## Step 3: Linear regression coefficients

- **Slope \(a\)** (step-by-step):

$$
\begin{align}
a &= \frac{X.dot(Y) - Y.mean() \cdot X.sum()} {\text{denominator}} \\
  &= \frac{\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i} {\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i} \\
  &= \frac{\sum_{i=1}^n x_i y_i - n \bar{x} \bar{y}}{\sum_{i=1}^n x_i^2 - n \bar{x}^2}
\end{align}
$$
- **Intercept \(b\)** (step-by-step):

$$
\begin{align}
b &= \frac{Y.mean() \cdot X.dot(X) - X.mean() \cdot X.dot(Y)}{\text{denominator}} \\
  &= \frac{\bar{y} \sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i y_i}{\sum_{i=1}^n x_i^2 - n \bar{x}^2}
\end{align}
$$

> Note: This is algebraically equivalent to the simpler form $\(b = \bar{y} - a \bar{x}\$).

- **Predicted values** $\(\hat{y}_i\)$ for each observation:

$$
\hat{y}_i = a x_i + b
$$

---

## Part 2: Multiple Linear Regression (Matrix Form)

### Step 1: Data as matrices

For multiple predictors \(p\), we organize the data into:

- **Design matrix** $\(X\) (size \(n \times (p+1)\)$ with intercept):

$$
X =
\begin{bmatrix}
1 & x_{11} & x_{12} & \dots & x_{1p} \\
1 & x_{21} & x_{22} & \dots & x_{2p} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n1} & x_{n2} & \dots & x_{np}
\end{bmatrix}
$$

- **Response vector** $\(Y\)$ (size $\(n \times 1\)$):

$$
Y =
\begin{bmatrix}
y_1 \\ y_2 \\ \vdots \\ y_n
\end{bmatrix}
$$

- **Coefficient vector** $\(w\)$ (size $\((p+1) \times 1\)$):

$$
w =
\begin{bmatrix}
b_0 \\ b_1 \\ \vdots \\ b_p
\end{bmatrix}
$$

- **Predicted values**:

$$
\hat{Y} = X w
$$

---

### Step 2: Least Squares Solution

The coefficients are obtained by solving the normal equations:

$$
X^\top X \, w = X^\top Y
$$

Python code:

```python
w = np.linalg.solve(X.T @ X, X.T @ Y)
Yhat = X @ w
```

Alternatively:

```python
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, w)
```

### Step 3: Coefficient of Determination (\(R^2\))

The $\(R^2\)$ value measures how well the multiple regression model fits the data.

- **Residuals**:

$$
d_1 = Y - \hat{Y}
$$

- **Total deviation from the mean**:

$$
d_2 = Y - \bar{Y}, \quad \bar{Y} = \frac{1}{n} \sum_{i=1}^{n} y_i
$$

- **R-squared**:

$$
R^2 = 1 - \frac{d_1^\top d_1}{d_2^\top d_2}
= 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
$$

- **Python implementation**:

```python
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print(f"R-squared: {r2}")

Python code:

```python
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print(f"R-squared: {r2}")
```
