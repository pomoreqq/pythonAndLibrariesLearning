
import pandas as pd

ads_df = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'Central'],
    'impressions': [1000, 800, 950, 400, 600],
    'clicks': [60, 30, 80, 25, 28]
})


ads_df['ctr'] = ads_df['clicks'] / ads_df['impressions']

newSeries = (
    ads_df
    .loc[ads_df['ctr'] > 0.05, ['region', 'ctr']]
    .set_index('region')
    .squeeze()
    .sort_values(ascending=False)
)

print(newSeries)

