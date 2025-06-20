import pandas as pd

df = pd.DataFrame({
    "region": ["East", "West", "East", "West", "East"],
    "sales": [100, 200, 150, 300, 120]
})


aggregatedData = df.groupby('region').sum()

eastSales = df[df['region'] == 'East']

srednia = eastSales['sales'].mean()
