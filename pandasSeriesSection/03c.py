import pandas as pd

sessions_df = pd.DataFrame({
    'user_id': ['U1'] * 4 + ['U2'] * 5 + ['U3'] * 4,
    'device': ['mobile', 'desktop', 'mobile', 'tablet',
               'desktop', 'mobile', 'desktop', 'tablet', 'mobile',
               'desktop', 'desktop', 'mobile', 'tablet'],
    'session_duration': [300, 500, 200, 100,
                         450, 320, 250, 150, 200,
                         600, 350, 400, 120],
    'country': ['PL', 'PL', 'DE', 'PL',
                'US', 'US', 'DE', 'US', 'PL',
                'FR', 'FR', 'DE', 'DE'],
    'timestamp': pd.date_range('2024-03-01', periods=13, freq='H')
})

result = sessions_df.groupby('user_id').agg(
    desktop = ('device', lambda s: (s == 'desktop').sum()),
    tablet = ('device', lambda s: (s == 'tablet').sum()),
    avgSession = ('session_duration', lambda s: s.mean()),
    uniqueCountries = ('country', lambda s: s.nunique())
)

print(result)