
import pandas as pd


df = pd.read_csv('pandasBasic/miniprojekt/dane.csv')

df['total'] = df['price'] * df['quantity']


totalSum = df['total'].sum()

groupByCategory = df.groupby('category')['total'].sum()

groupByDay = df.groupby('date')['total'].sum()
print(groupByCategory)
print(groupByDay)

maxCategory = df.groupby('category')['total'].sum().idxmax()
maxDay = df.groupby('category')['total'].sum().idxmax()

sortedTotalDf = df.sort_values('total', ascending=False)
print(sortedTotalDf)