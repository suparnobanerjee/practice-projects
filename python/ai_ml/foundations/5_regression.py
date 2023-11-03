import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions
import pickle as pkl
import matplotlib.pyplot as plt

df = pd.read_csv('placement.csv')
df = df.iloc[:,1:]
# plt.scatter(df['cgpa'],df['iq'],c=df['placement'])
# plt.show()
X = df.iloc[:,:2]
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#with scaling
scl = StandardScaler()
X_train = scl.fit_transform(X_train)
X_test = scl.transform(X_test)

reg = LogisticRegression()
reg.fit(X_train,y_train)
y_predicted = reg.predict(X_test)

print(f"Accuracy : {accuracy_score(y_test,y_predicted)*100}%")

#plotting decision regions
plot_decision_regions(X_train, y_train.values, clf=reg, legend=2)
plt.show()

#saving to a pickle file
pkl.dump(reg,open('model_regression_5.pkl','wb'))