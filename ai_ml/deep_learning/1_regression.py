import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("houseprices.csv")

reg=linear_model.LinearRegression()
reg.fit(df[['year']],df['per_capita_income_usd'])
yr = input("Enter the year : ")
input_data = pd.DataFrame({'year':[yr]})
predicted_value = reg.predict(input_data)


print("Estimated per capita income (in USD) : ", predicted_value[0])

plt.scatter(df.year,df.per_capita_income_usd,color="blue",marker="o")
plt.scatter(df['year'],reg.predict(df[['year']]),color="red",marker="x")
plt.show()