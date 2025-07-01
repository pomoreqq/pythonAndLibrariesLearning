
import pandas as pd

events = pd.DataFrame({
    'user_id': ['U1'] * 3 + ['U2'] * 7 + ['U3'] * 6 + ['U4'] * 2 + ['U5'] * 6,
    'event_type': ['purchase'] * 3 + ['purchase'] * 5 + ['click'] * 2 +
                  ['purchase'] * 6 + ['click'] * 2 + ['purchase'] * 6,
    'value': [100, 150, 120, 200, 250, 120, 50, 10, 60, 300, 400,
              50, 60, 70, 80, 90, 30, 40, 110, 200, 300, 100, 200, 150],
    'event_dt': pd.date_range('2024-01-01', periods=24)
})

filtered = events.loc[events['event_type'] == 'purchase'].groupby('user_id').agg(purchases = ('value','count'), totalSpent=('value','sum'))
filtered = filtered.loc[(filtered['purchases'] > 5) & (filtered['totalSpent'] > 500)].head(10)
print(filtered)