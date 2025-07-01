import pandas as pd
import numpy as np
logs_df = pd.DataFrame({
    'user_id': ['U1'] * 5 + ['U2'] * 5 + ['U3'] * 4,
    'event_type': ['play', 'like', 'pause', 'play', 'like',
                   'pause', 'play', 'play', 'like', 'pause',
                   'play', 'like', 'play', 'pause'],
    'duration': [300, None, None, 200, None,
                 None, 400, 100, None, None,
                 150, None, 350, None],
    'event_time': pd.date_range('2024-05-01', periods=14, freq='T')
})

result = logs_df.groupby('user_id').agg(
    likes=('event_type', lambda s: (s == 'like').sum()),
    pauses=('event_type', lambda s: (s == 'pause').sum()),
    total_play_time=('duration', lambda s: s[logs_df.loc[s.index, 'event_type'] == 'play'].sum())
    
)
print(result)