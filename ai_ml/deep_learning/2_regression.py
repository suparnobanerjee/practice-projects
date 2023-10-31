import pandas as pd
import numpy as np
from sklearn import linear_model
import math

df=pd.read_csv('homeprices.csv')
# print(df.bedrooms)  ## Before
mdian = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(mdian)
print(df.bedrooms)    ## After (filling NA with median)
