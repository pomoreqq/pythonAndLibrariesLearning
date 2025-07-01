import pandas as pd

errors_df = pd.DataFrame({
    'service_name': ['auth', 'api', 'db', 'auth', 'db', 'api', 'auth', 'db', 'api', 'auth'],
    'status': ['ok', 'error', 'ok', 'warn', 'ok', 'ok', 'error', 'warn', 'ok', 'ok'],
    'duration_ms': [120, None, 200, None, 180, 150, None, None, 110, 130],
    'log_time': pd.date_range('2024-06-01', periods=10, freq='T'),
    'server_id': ['S1', 'S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S3', 'S3', 'S3']
})


reuslt = errors_df.groupby('service_name').agg(
    errorCount = ('status',lambda s: (s == 'error').sum()),
    warnCount = ('status',lambda s: (s == 'warn').sum()),
    durationMsMean = ('duration_ms', lambda s: s[errors_df.loc[s.index, 'status'] == 'ok'].mean())
)
print(reuslt)