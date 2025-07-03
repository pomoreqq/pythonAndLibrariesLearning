import pandas as pd

sales_df = pd.DataFrame({
    'date': pd.date_range(start='2024-01-01', periods=6, freq='D'),
    'store_id': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2'],
    'product': ['P1', 'P2', 'P1', 'P2', 'P1', 'P2'],
    'units_sold': [10, 5, 8, 6, 7, 9]
})


pivotTable = sales_df.pivot_table(index='store_id',columns='product',values='units_sold',aggfunc='sum')


print(pivotTable)


pivotTable = pivotTable.melt()


print(pivotTable)