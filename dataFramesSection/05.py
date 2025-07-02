# Masz dwa zbiory:

# users_df: użytkownicy z user_id, region, signup_date

# logins_df: logi logowań z user_id, login_time

# 👉 Zadanie:

# Połącz dane tak, by do każdego użytkownika dodać jego ostatnie logowanie.

# Zastosuj merge() i agregację groupby() + max().

import pandas as pd
import numpy as np

# Ćwiczenie 1 – merge z warunkiem
users_df = pd.DataFrame({
    'user_id': ['U1', 'U2', 'U3', 'U4'],
    'region': ['NA', 'EU', 'EU', 'APAC'],
    'signup_date': pd.to_datetime(['2023-01-01', '2023-02-15', '2023-03-10', '2023-04-01'])
})

logins_df = pd.DataFrame({
    'user_id': ['U1', 'U2', 'U1', 'U3', 'U3', 'U4'],
    'login_time': pd.to_datetime([
        '2023-06-01', '2023-06-02', '2023-07-01',
        '2023-06-01', '2023-08-01', '2023-06-05'
    ])
})

mergedDf = pd.merge(users_df,logins_df, on='user_id', how='left')

last_login = logins_df.groupby('user_id')['login_time'].max().reset_index()
mergedDf = mergedDf.merge(last_login,on='user_id', how='left')
print(mergedDf)