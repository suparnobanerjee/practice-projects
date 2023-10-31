import pandas as pd
from sklearn import linear_model
from word2number import w2n

df=pd.read_csv('hiring.csv')
df.experience = df.experience.fillna(0)
def convert(x):
  try:
    return w2n.word_to_num(x)
  except:
    return int(x)
df.experience = df.experience.apply(convert)

m = df['test_score(out of 10)'].median()
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(m)

print(df)

reg = linear_model.LinearRegression()
reg.fit(df.drop('salary($)',axis='columns'),df['salary($)'])

print(reg.coef_)
print(reg.intercept_)

x1 = float(input("Enter experience : "))
x2 = float(input("Enter test score : "))
x3 = float(input("Enter interview score : "))
input_value = pd.DataFrame({'experience':[x1],'test_score(out of 10)':[x2],'interview_score(out of 10)':[x3]})
predicted_value = reg.predict(input_value)
print("Estimated salary (in USD) : ", predicted_value[0])