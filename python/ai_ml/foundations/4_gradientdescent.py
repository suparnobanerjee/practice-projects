import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

def gradient_descent(x,y):
  m_current = b_current = 0
  n = len(x)
  iterations = 1000000
  learning_rate = 0.0001
  cost=np.zeros(iterations)
  for i in range(iterations):
    y_predicted = m_current*x + b_current
    cost[i] = (1/n)*sum([val**2 for val in (y-y_predicted)])
    md = -(2/n)*sum(x*(y-y_predicted))
    bd = -(2/n)*sum(y-y_predicted)
    m_current = m_current - learning_rate*md
    b_current = b_current - learning_rate*bd
    if i%100==0:
      print(f"m : {m_current}, b : {b_current}, cost: {cost[i]}, count: {i}")
    if math.isclose(cost[i],cost[i-1],rel_tol=1e-20):
      print("BREAK APPLIED !")
      break
  return m_current, b_current
  

df = pd.read_csv('test_scores.csv')
x = np.array(df.math)
y = np.array(df.cs)
# m,b = gradient_descent(x,y)

reg = LinearRegression()
reg.fit(df[['math']],df['cs'])
print(f"m: {reg.coef_[0]}, b: {reg.intercept_}")
m=reg.coef_[0]
b=reg.intercept_

plt.scatter(x,y)
plt.plot(x,m*x+b,color='red')
plt.show()
