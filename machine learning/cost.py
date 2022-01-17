import math

import pandas as pd

df = pd.read_csv("assests/new_model7.csv")


# print(df)

def gradient(x, y):
    m_curr = b_curr = 0
    n = len(x)
    iterations = 2000000000000
    learning_rate = 0.00009
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        b = cost
        r = math.isclose(cost, b, rel_tol=0, abs_tol=0)
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum((y - y_predicted))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if r == False:
            break
        print("m {}, b {}, cost {}, iteration{}".format(m_curr, b_curr, cost, i))


x = df.math
y = df.cs

gradient(x, y)
