import pandas as pd

transactions_df = pd.DataFrame({
    'transaction_id': range(1, 11),
    'client_id': ['C1', 'C2', 'C1', 'C3', 'C2', 'C3', 'C4', 'C5', 'C4', 'C5'],
    'amount': [100, 200, 150, 300, 180, 220, 90, 110, 95, 105],
    'date': pd.date_range('2024-01-01', periods=10, freq='15D')
})

clients_df = pd.DataFrame({
    'client_id': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'segment': ['A', 'B', 'A', 'B', 'A'],
    'join_date': pd.to_datetime(['2023-12-01', '2023-12-15', '2023-11-20', '2024-01-10', '2024-01-20'])
})


mergedDf = pd.merge(transactions_df,clients_df,on='client_id', how='left')

mergedDf['month'] = mergedDf['date'].dt.month

groupBySegAndMon = mergedDf.groupby(['segment','month']).agg(
    meanAmount = ('amount','mean')
)

pivotTable = groupBySegAndMon.pivot_table(index='segment',columns='month',values='meanAmount')
print(pivotTable)
pivotTable = pivotTable.melt()
print(pivotTable)