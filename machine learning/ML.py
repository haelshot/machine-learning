import pandas as pd
import numpy as np
from sklearn import linear_model
import math

df = pd.read_csv('assests/interview.csv')
# print(df)
median_file = math.floor(df.test_score.median())
# print(median_file)
df.test_score = df.test_score.fillna(median_file)
# print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score', 'interview_score']], df.salary)
# print(reg.coef_)
print(math.floor(reg.predict([(2, 10, 10)])))
