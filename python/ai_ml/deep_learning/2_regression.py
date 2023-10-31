import pandas as pd
from sklearn import linear_model

df=pd.read_csv('homeprices.csv')
# print(df.bedrooms)  ## Before
m = df.bedrooms.median()
df.bedrooms = df.bedrooms.fillna(m)
print(df.bedrooms)    ## After (filling NA with median)

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df['price'])

# print(reg.coef_) # m1,m2,m3...
# print(reg.intercept_) # c


X1=float(input("Enter the area : "))
X2=float(input("Enter the number of bedrooms : "))
X3=float(input("Enter the age : "))
input_data=pd.DataFrame({'area':[X1],'bedrooms':[X2],'age':[X3]})
y = reg.predict(input_data)
print("Estimated price (in USD) : ", y[0])

