import pandas as pd

products_df = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'category': ['A', 'B', 'A', 'C']
})

sales_df = pd.DataFrame({
    'product_id': [101, 101, 102, 103, 103, 103],
    'sale_date': pd.date_range(start='2024-01-01', periods=6, freq='D'),
    'quantity': [5, 3, 7, 1, 2, 3]
})


mergedDf = pd.merge(products_df,sales_df,on='product_id',how='left')


groupedAndSumed = mergedDf.groupby('product_id')['quantity'].sum().reset_index()
groupedAndSumed.rename(columns={'quantity': 'totalQuantity'},inplace=True)

mergedDf = mergedDf.merge(groupedAndSumed,on='product_id',how='left')
print(mergedDf)