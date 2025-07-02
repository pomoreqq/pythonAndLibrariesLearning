import pandas as pd
import numpy as np
from datetime import date

campaign_df = pd.DataFrame({
    'campaign_id': [101, 102, 103, 104, 105, 106],
    'region': ['EU', 'NA', 'APAC', 'EU', 'NA', 'APAC'],
    'channel': ['Email', 'Search', 'Social', 'Search', 'Email', 'Social'],
    'budget': [1000, 1500, 1100, 1200, 1300, 1250],
    'start_date': pd.date_range('2024-01-01', periods=6, freq='15D')
})


clients_df = pd.DataFrame({
    'client_id': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'region': ['EU', 'NA', 'APAC', 'EU', 'NA'],
    'industry': ['tech', 'finance', 'retail', 'tech', 'finance'],
    'active': [True, True, False, True, True]
})


orders_df = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 6], 
    'client_id': ['C1', 'C2', 'C3', 'C4', 'C5'] * 4 + ['C1'],
    'campaign_id': [101, 102, 103, 104, 105, 106, 101, 102, 103, 104,
                    105, 106, 101, 102, 103, 104, 105, 106, 101, 102, 106],
    'order_value': np.random.choice([np.nan, 100, 200, 300, 400, 500, 900, 1000], size=21),
    'order_date': pd.date_range('2024-01-05', periods=21, freq='D')
})
# orders_df.loc[3, 'order_date'] = 'not a date'
# orders_df['campaign_id'] = orders_df['campaign_id'].astype(str)

orders_df['campaign_id'] = orders_df['campaign_id'].astype('Int32')
orders_df.loc[3,'order_date'] = pd.Timestamp('2024-01-8 00:00:00')
campaign_df = campaign_df.astype({col:'category' for col in campaign_df.loc[:,['region','channel']].select_dtypes('object').columns})
# print(campaign_df.dtypes)
campaign_df['campaign_id'] = campaign_df['campaign_id'].astype('Int32')
print(orders_df['order_value'].isna().any())
orders_df['order_value']= orders_df['order_value'].fillna(value=orders_df['order_value'].mean())
# print(orders_df['order_value'].isna().any())
isDuplicate = orders_df['order_id'].duplicated()
orders_df = orders_df[-isDuplicate]
# orders_df = orders_df.drop_duplicates(subset='order_id')

#3.
print(orders_df['campaign_id'].dtype)


merged_df = (
    orders_df
    .merge(campaign_df, on='campaign_id', how='left')
    .merge(clients_df, on='client_id', how='left')
)

meanAndSumOrderCampaign = merged_df.groupby('campaign_id').agg(
    totalOrderValue = ('order_value', 'sum'),
    meanOrderValue = ('order_value','mean')
)


meanAndSumOrderChanel = merged_df.groupby('channel').agg(
    totalOrderValue = ('order_value', 'sum'),
    meanOrderValue = ('order_value','mean')
)
# print(merged_df)

conversionRatePerCampaignGrouped = merged_df.groupby('campaign_id')

conversionRateIndicator = conversionRatePerCampaignGrouped['order_id'].count() / conversionRatePerCampaignGrouped['budget'].first()
conversionRateIndicator.name = 'Indicator'

mergeConversionRateIndicatorAndSum = pd.merge(meanAndSumOrderCampaign,conversionRateIndicator, on='campaign_id',how='left')


campaignTotalValueRank = mergeConversionRateIndicatorAndSum['totalOrderValue'].rank(ascending=False)
campaignIndicatorRank = mergeConversionRateIndicatorAndSum['Indicator'].rank(ascending=False)
campaignIndicatorRank.name = 'IndicatorRank'
campaignTotalValueRank.name = 'TotalValueRank'
mergedRanks = pd.merge(campaignIndicatorRank,campaignTotalValueRank,right_index=True,left_index=True, how='left')

pivotTable = merged_df.pivot_table(index='region_x',columns='channel',values='order_value',observed=True,aggfunc='mean')

pivotTable = pivotTable.stack(dropna=False).reset_index()


#4
clientsStats = merged_df.groupby('client_id').agg(
    meanOrderValue = ('order_value','mean'),
    uniqieCampaigns = ('campaign_id', lambda s: s.nunique()),
    mostFrequentChannel = ('channel', lambda s: s.value_counts().idxmax())
)

companiesCountPerClient = merged_df.groupby('client_id').agg(
    isActive = ('active', 'first'),
    uniqueCampaings = ('campaign_id', 'nunique')
)
companiesCountPerClient['powerUser'] = (
    (companiesCountPerClient['isActive'] == True) &
    (companiesCountPerClient['uniqueCampaings'] > 3)
)
merged_df = merged_df.merge(companiesCountPerClient[['powerUser']], on='client_id', how='left')

anomaly1Detection = merged_df[merged_df['order_value'] > 900]
print(anomaly1Detection)

anomaly2Detection = merged_df[(merged_df['channel'] == 'Social') & (merged_df['budget'] < 1100)]
print(anomaly2Detection)

anomaly3Detection = merged_df.groupby('campaign_id').agg(
    isLowOrderCampaign = ('order_id', lambda s: (s.count() < 3))
)

print(anomaly3Detection)


# anomaly 4

# Krok 1: odfiltrowanie zamówień, gdzie region klienta ≠ region kampanii
region_mismatch_df = merged_df[merged_df['region_x'] != merged_df['region_y']]

# Krok 2: licznik – liczba zamówień spoza regionu per kampania
mismatch_counts = region_mismatch_df.groupby('campaign_id')['order_id'].count()

# Krok 3: mianownik – łączna liczba zamówień per kampania
total_counts = merged_df.groupby('campaign_id')['order_id'].count()

# Krok 4: obliczenie udziału zamówień spoza regionu
mismatch_ratio = (mismatch_counts / total_counts).fillna(0)

# Krok 5: wybór kampanii z odsetkiem spoza regionu > 50%
anomaly4Detection = mismatch_ratio[mismatch_ratio > 0.5]
print(anomaly4Detection)