import pandas as pd

alerts = pd.DataFrame({
    'timestamp': pd.date_range('2024-04-01', periods=12, freq='H'),
    'system': ['db', 'auth', 'db', 'network', 'db', 'auth', 'db', 'network', 'auth', 'db', 'network', 'db'],
    'status_code': ['OK', 'FAIL', 'WARN', 'FAIL', 'FAIL', 'OK', 'OK', 'OK', 'FAIL', 'WARN', 'WARN', 'OK']
})


result = alerts[alerts['system'] == 'db']['status_code'].value_counts().sort_values()

# result = alerts.query("system == 'db'").loc[:, 'status_code'].value_counts().sort_values()