import pandas as pd 


df_sales = pd.DataFrame({
    "product": ["A", "B", "C"],
    "sales": [100, 150, 200]
})

df_prices = pd.DataFrame({
    "product": ["A", "B", "C"],
    "price": [10, 15, 20]
})


mergedDf = df_sales.merge(df_prices,how='right')
print(mergedDf)


mergedDf['revenue'] = mergedDf['sales'] * mergedDf['price']

print(mergedDf)