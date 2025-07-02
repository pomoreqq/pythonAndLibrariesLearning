import pandas as pd

clients_2024 = pd.DataFrame({
    'client_id': ['C1', 'C2'],
    'region_code': [1, 2],
    'joined': ['2024-01-01', '2024-01-15']
})

clients_2025 = pd.DataFrame({
    'client_id': ['C3', 'C4'],
    'region_code': [2, 3],
    'joined': ['2025-01-05', '2025-02-10']
})

regions_df = pd.DataFrame({
    'region_code': [1, 2, 3],
    'region_name': ['North', 'East', 'South']
})

concatedDf = pd.concat((clients_2024,clients_2025),axis=0)

mergedDf = concatedDf.merge(regions_df,on='region_code',how='left')
print(mergedDf)