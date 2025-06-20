import pandas as pd 

df = pd.read_csv('pandasBasic/miniprojekt/sales.csv')

total = df['price'] * df['quantity']

df['total'] = total

totalSum = df['total'].sum()

totalSumByRegion = df.groupby('category')['total'].sum()
totalSumByDate = df.groupby('date')['total'].sum()

najlepszyprodukt = df.groupby('product')['total'].sum().idxmax()
najlepszy_dzien = df.groupby('date')['total'].sum().idxmax()
print(najlepszy_dzien)

#najwiecej przyniosla przychoda kategoria electronics, a dzien najwiekszego przychodu to 01.05.2025