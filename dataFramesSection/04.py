import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Anna', 'Kamil', 'Zofia']
})

right = pd.DataFrame({
    'id': [3, 1, 4],
    'score': [88, 92, 75]
})

newMerged = pd.merge(left,right, how='left')

newMerged.loc[1,'score'] = 0
print(newMerged)

newMerged2 = pd.merge(left,right, on='id')

print(newMerged2)