import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('assests/township.csv')
# print(df)
dummies = pd.get_dummies(df.town)
merged = pd.concat([df, dummies], axis='columns')
# print(merged)
final = merged.drop(['town', 'west windsor'], axis='columns')
# print(final)
model = LinearRegression()
x = final.drop(['price'], axis='columns')
y = final.price

model.fit(x, y)
# print(model.predict([(2800, 0, 1)]))
# print(model.score(x, y))
le = LabelEncoder()
dfle = df
dfle.town = le.fit_transform(dfle.town)
#print(dfle)
z = df[['town', 'area']].values
w = dfle.price
ohe = OneHotEncoder(categorical_features=[0])

ohe.fit_transform(z).toarray()
print(z)