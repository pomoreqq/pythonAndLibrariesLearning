import pandas as pd


df = pd.DataFrame({
    'name': ['Anna', 'Jan', 'Zofia', 'Kamil', 'Ola'],
    'score': [90, 85, 78, 92, 88],
    'passed': [True, True, True, True, False]
}, index=['a', 'b', 'c', 'd', 'e'])



df.loc['c','score'] = 95
df = df[df['passed'] == True]
print(df)