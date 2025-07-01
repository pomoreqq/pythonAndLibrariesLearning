import pandas as pd 

sales = pd.DataFrame({
    'region': ['EU', 'EU', 'NA', 'EU', 'APAC', 'NA', 'NA', 'EU'],
    'category': ['tech', 'furniture', 'tech', 'tech', 'furniture', 'furniture', 'tech', 'tech'],
    'revenue': [1000, 1500, 900, 1200, 1300, 800, 950, 1100],
    'quantity': [5, 3, 4, 6, 2, 1, 3, 5]
})

result = sales.groupby('region').agg(
    revenueMean = ('revenue', lambda s: s.mean()),
    sumQuantity = ('quantity', lambda s: s.sum()),
    higsetRegionRevenueForTech = ('revenue', lambda s: s[sales.loc[s.index,'category'] == 'tech' ].mean())             
)

result2= sales.groupby(['region','category'])['quantity'].sum()
print(result2)