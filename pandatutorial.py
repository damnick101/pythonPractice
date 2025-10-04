import pandas as pd

df = pd.read_csv('orders.csv')
desc = pd.describe(df)
print(desc)