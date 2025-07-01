import pandas as pd

data = pd.DataFrame({
    'client_id': ['C1'] * 4 + ['C2'] * 5 + ['C3'] * 3 + ['C4'] * 6 + ['C5'] * 5,
    'region': ['EU', 'EU', 'NA', 'NA', 'EU', 'NA', 'NA', 'EU', 'APAC', 'APAC', 'EU', 'NA', 'APAC', 'EU', 'NA', 'EU', 'APAC', 'APAC', 'NA', 'NA', 'EU', 'APAC', 'EU'],
    'response_time_ms': [120, 150, None, 180, 140, 300, 200, 170, 210, 190, None, 250, 220, 160, 240, None, 210, 190, 300, 280, 150, 230, None],
    'status': ['ok', 'ok', 'error', 'ok', 'warn', 'ok', 'error', 'ok', 'warn', 'ok', 'error', 'ok', 'ok', 'warn', 'ok', 'error', 'warn', 'ok', 'error', 'ok', 'ok', 'warn', 'ok'],
    'timestamp': pd.date_range('2024-05-01 08:00', periods=23, freq='H')
})


#1
statusesCount = data.groupby('client_id').agg(
    errorCount = ('status',lambda s: s.eq('error').sum()),
    warnCount = ('status',lambda s: s.eq('warn').sum())
)

responsesOkFiltered = data[data['status'].eq('ok')]
responsesOkFilteredGroupByClientMeanResponse = responsesOkFiltered.groupby('client_id')['response_time_ms'].mean()


mostRegionsPerClient = data.groupby('client_id')['region'].apply(lambda s: s.value_counts().idxmax())




#2

groupedByRegion = data.groupby('region').agg(
    sumOfStatuses = ('status', 'count'),
     errorsCount = ('status', lambda s: s.eq('error').sum()),
     meanResponse = ('response_time_ms', lambda s: s[data.loc[s.index,'status'].eq('ok')].mean()),
     warnCount = ('status', lambda s: (s == 'warn').sum())
)
groupedByRegion['errorIndicator'] = groupedByRegion['errorsCount'] / groupedByRegion['sumOfStatuses']



# najszybciej dziala region eu a najmniej warnow ma NA najlepszy errorWskaznik ma apac

data['hours'] = data['timestamp'].dt.hour

data['time_block'] = pd.cut(data['hours'], bins=[0,6,12,18,24], labels=['noc','rano','poludnie','popoludniu'],right=False)


dataGroupByTimeBlock = data.groupby('time_block').agg(
    meanResponse = ('response_time_ms', lambda s: s[data.loc[s.index,'status'].eq('ok')].mean()),
    errorsCount = ('status', lambda s: s.eq('error').sum()),
)


print(dataGroupByTimeBlock)
    # najwiecej bledow jest popoludniu, oraz wtedy najwolniejszy jest response time