# Task: Analyze transactional sales data from a CSV file.
# - Load data from a CSV file containing 'price', 'quantity', 'category', and 'date'.
# - Add a new column 'total' by multiplying 'price' and 'quantity'.
# - Calculate the total revenue.
# - Group and sum revenue by product category and by day.
# - Identify the category and day with the highest total revenue.
# - Sort all transactions by 'total' value in descending order.
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