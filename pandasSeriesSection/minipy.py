import pandas as pd


errors_df = pd.DataFrame({
    'service_name': ['auth', 'api', 'db', 'auth', 'db', 'api', 'auth', 'db', 'api', 'auth', 'db', 'api', 'auth', 'db', 'auth'],
    'status': ['ok', 'error', 'ok', 'warn', 'ok', 'ok', 'error', 'warn', 'ok', 'ok', 'ok', 'warn', 'error', 'error', 'warn'],
    'duration_ms': [120, None, 200, None, 180, 150, None, None, 110, 130, 210, 160, None, None, None],
    'log_time': pd.date_range('2024-06-01 00:00', periods=15, freq='H'),
    'server_id': ['S1', 'S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S3', 'S3', 'S3', 'S4', 'S4', 'S4', 'S5', 'S5']
})




serviceNameStatistis = errors_df.groupby('service_name').agg(
    errorCount = ('status', lambda s: (s == 'error').sum()),
    warnCount = ('status', lambda s: (s == 'warn').sum()),
    # meanDurationTime = ('duration_ms', lambda s: s[errors_df.loc[s.index,'status'] == 'ok'].mean())
    #
    meanDurationTime = ('duration_ms', lambda s: s[s.index.isin(errors_df[errors_df['status'] == 'ok'].index)].mean())
)
print(serviceNameStatistis)
uniqueForServerId = errors_df.groupby('server_id')['status'].nunique()
sumOfStatuses = errors_df.groupby('server_id')['status'].count()
errorsPerServer = errors_df.groupby('server_id')['status'].apply(lambda s: (s == 'error').sum())

print(errorsPerServer)

errors_df['hours'] = errors_df['log_time'].dt.hour
errors_df['time_block'] = pd.cut(errors_df['hours'],bins=[0,6,12,15],labels=['noc','rano','poludnie'], right=False)

# meanTimePerTimeBlock = errors_df.groupby('time_block').agg(
#     meanDuration = ('duration_ms',lambda s: s[errors_df.loc[s.index,'status'] == 'ok'].mean())
# )
filteredPerOkStatus = errors_df[errors_df['status'] == 'ok']
meanDurationPerTimeBlock = filteredPerOkStatus.groupby('time_block',observed=True)['duration_ms'].mean()



warnAndDurationStatforService = errors_df.groupby('service_name').agg(
    warnCount = ('status', lambda s: (s=='warn').sum() ),
    meanDurationMs = ('duration_ms', lambda s: s[s.index.map(errors_df['status']) == 'ok'].mean()
                      ))

filteredwarnAndDurationStatforService = warnAndDurationStatforService[(warnAndDurationStatforService['warnCount'] > 0.5 )& (warnAndDurationStatforService['meanDurationMs'] < 150)]


# tak usluga auth najczesciej zwraca status warn i ma najnizszy czas odpowiedzi 125ms

isAllErrorIn = errors_df.groupby(['server_id', 'service_name'], observed=False)['status'].apply(lambda s: (s == 'error').all())
isAllErrorIn = isAllErrorIn[isAllErrorIn].reset_index()
print(isAllErrorIn)
# tak sa dla serveru 1 serwisu api wszystkie logi to error, dla s2 serwisu auth wszystkie logi to error, dla s4 serwisu auth wszystkie logi to error i dla s5 serwisu db wszystkie logi to error

## 
# ✍️ Raport końcowy
# Zakończ analizę krótkim wnioskiem:

# Które usługi są najbardziej problematyczne?
    #moim daniem najbardziej problematyczna usluga jest usluga auth poniewaz posiada na dwoch serwerach same errory, i takze posiada najwiecej warnow
# Czy są różnice między serwerami?
# tak sa roznice mimo to zdecydowanie serwis auth odpowiada najszynciej na te errory i warny, za to db odpowiada najwolniej
# Jakie działania byś zarekomendował?
# zarekomendowalym bym wiekszy naklad monitorowania serwisu auth skad wynikaja te bledy, zarekomendowalbym takze poprawe architektury dla syrwisu db