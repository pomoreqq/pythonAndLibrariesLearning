
import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'age': [25, 30, 22, 28, 40],
    'income': [3000, 3500, 2800, 3200, 4000]
})
def conditions(row):
    if row['age'] < 26:
        age = 'junior'
    elif row['age'] >= 26 and row['age'] <= 35:
        age = 'adult'
    else:
        age = 'senior'
    return age
df['age_group'] = df.apply(conditions,axis=1)

df['income'] = df['income'].apply(lambda s: s / 4000)

resultMean = df.groupby('gender').apply(lambda s: s['income'].mean(),include_groups=False)

resultAge = df.groupby('gender')['age'].mean()
print(resultAge)