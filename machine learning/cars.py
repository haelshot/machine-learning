import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv('assests/cars.csv')

dummies = pd.get_dummies(df.car_model)
merged = pd.concat([df, dummies], axis='columns')
final = merged.drop(['car_model', 'Mercedez'], axis='columns')
model = LinearRegression()
x = final.drop(['sell_price'], axis='columns')
y = final.sell_price

model.fit(x, y)
#print(model.predict([(86000, 7, 1, 0)]))
print(model.score(x, y))