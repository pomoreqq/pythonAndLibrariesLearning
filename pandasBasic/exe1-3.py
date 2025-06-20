dane = [
    {"name": "Anna", "age": 29, "department": "HR"},
    {"name": "Tomek", "age": 35, "department": "Finance"},
    {"name": "Kasia", "age": 24, "department": "IT"}
]

import pandas as pd

df = pd.DataFrame(dane)

df['seniority'] = ['senior' if x > 30 else 'junior' for x in df['age']]
# df['seniority'] = df['age'].apply(lambda x: 'senior' if x > 30 else 'junior')

onlyIT = df[df['department'] == 'IT']
onlyHR = df[df['department']== 'HR']

# print(df['name'])
# print(df['seniority'])


df = df.set_index('name')
df = df.sort_values('age',ascending=False)
df = df.reset_index('name')

print(df)