import pandas as pd

events = pd.read_csv('dataFramesSection/minip/events_df.csv')
# 0 duplikatow, #NaN'ow #user ma typ object a jest to indentyfikator 'UXX' lepszym wyborem bedzie dla tej kolumny typ danych category
#print(events.duplicated().count())
#print(events.isna().count())
events['user_id'] = events['user_id'].astype('category')
# print(events.dtypes)

sales = pd.read_csv('dataFramesSection/minip/sales.csv')
#0 duplicates 0 nans, zmieniam date na datetime,zmieniam category z object na category
# print(sales.duplicated().sum())
# print(sales.isna().sum())
sales['category'] = sales['category'].astype('category')
sales['date'] = sales['date'].astype('str')
sales['date'] = pd.to_datetime(sales['date'])
# print(sales.dtypes)
# print(sales)

regions = pd.read_csv('dataFramesSection/minip/regions_df.csv')
#0 nans, 0 duplicates, zmieniam regionname z object na category
# print(regions.duplicated().sum())
# print(regions.isna().sum())
regions['region_name'] = regions['region_name'].astype('category')
# print(regions.dtypes)
# print(regions)

subscriptions = pd.read_csv('dataFramesSection/minip/subscriptions_df.csv')
# o duplicates, 0 nans, zmieniam plan na typ category, userid tez na category bo zmieniem to w events na category oraz subscrtion date z object na datetime
# print(subscriptions.duplicated().sum())
# print(subscriptions.isna().sum())
subscriptions['user_id'] = subscriptions['user_id'].astype('category')
subscriptions['plan'] = subscriptions['plan'].astype('category')
subscriptions['subscription_date'] = pd.to_datetime(subscriptions['subscription_date'])
# print(subscriptions.dtypes)

users = pd.read_csv('dataFramesSection/minip/users_df.csv')
# 0 duplikatow, 0 nanow zamiana typow na wlasciwe
# print(users.duplicated().sum())

users['user_id'] = users['user_id'].astype('category')
users['platform'] = users['platform'].astype('category')
users['signup_date'] = pd.to_datetime(users['signup_date'])

# niespojnosci

#1. Czy wszyscy userzy z events_df występują w users_df?
result = (events['user_id'].isin(users['user_id']).all()) # true, czyli znaczy ze nie ma zadnego false
#2. Czy wszyscy userzy z subscriptions_df istnieją w users_df?
result2 = (subscriptions['user_id'].isin(users['user_id']).all()) # nie ma zadnego false
#. Czy każdy region_code z users_df istnieje w regions_df?
result3 = (users['region_code'].isin(regions['region_code']).all()) # true 
# Czy wszyscy użytkownicy w subscriptions_df mają unikalny wpis?
# print(subscriptions['user_id'].nunique()) # tak wszyscy maja unikalny wpis bo tylko jest 1 wpis danego usera

#etap 2

# print(users)
# print(regions)

#merge usersDF and regionDf
mergedUsersRegion = pd.merge(users,regions,on='region_code',how='left')
# print(mergedUsersRegion)
groupedAndAgg = mergedUsersRegion.groupby(['region_name','platform']).agg(
    usersCount = ('user_id', 'size')
)

# print(groupedAndAgg) # w azji liczba uzytkownikow desktop i mobile wynosi po dwa, w europie desktop 4 mobile 6, w polnocnej amercye desktop 1 mobile 5

# srednia liczba eventow na uzytkownika

groupedAndAgg2 = events.groupby('user_id').agg(
    sumOfEventsPerUsers = ('event_id', 'nunique'),
)
meanPerUser = groupedAndAgg2['sumOfEventsPerUsers'].mean() # srednio user mial 5 eventow
mostActiveUsers = (groupedAndAgg2[groupedAndAgg2['sumOfEventsPerUsers'] > 5]) # 8 userow bylo bardziej aktywnych



#etap 3
#1
precentUsersWithSub = len(subscriptions['user_id']) / len(users['user_id']) * 100 ## 40% uzytkownikow ma subskrypcje

#2
mergedSubsWithEventsAgg = pd.merge(subscriptions,groupedAndAgg2,on='user_id', how='left')
# print(mergedSubsWithEventsAgg)

meanOfSubAndNotSub = mergedSubsWithEventsAgg.groupby('plan').apply(lambda s: s['sumOfEventsPerUsers'].mean())

# print(meanOfSubAndNotSub) # srednia eventow per sub 5.5, basic 6.75

print(users['signup_date'])
#3
mergedSignUpFromUsersWithSubsDf = pd.merge(subscriptions,users[['user_id','signup_date']],on='user_id', how='left')
print(mergedSignUpFromUsersWithSubsDf)
mergedSignUpFromUsersWithSubsDf['diffInHours'] = (mergedSignUpFromUsersWithSubsDf['subscription_date'] - mergedSignUpFromUsersWithSubsDf['signup_date']).dt.days

meanOfHoursDiff = mergedSignUpFromUsersWithSubsDf['diffInHours'].mean() # 29.125 srednia czasu zmiany z planu darmowego na subskrycpke
medianOfHoursDiff = mergedSignUpFromUsersWithSubsDf['diffInHours'].median() # mediana to 17


#4 liczba uzytkownikow na plan oraz ktory plan szybciej wybieraja

aggData = mergedSignUpFromUsersWithSubsDf.groupby('plan').agg(
    userSumPerPlan = ('user_id','count'),
    meanTimeToGetPlanPerPlan = ('diffInHours', 'mean')
)

print(aggData)
# uzytkownicy per plan 4 dla obu, krotszy czas srednio do wyboru planu jest do planu basic 16,75 dnia, dla pro wynosi on 41,5

# 1. ✅ Którzy użytkownicy są najaktywniejsi i co ich łączy?
# Czy subskrybenci są bardziej aktywni niż użytkownicy bez planu?
    # nie sa
# Czy są różnice między planami (basic vs pro) pod kątem aktywności?
    # basic sa delikatnie aktywnejsi

#     2. 🌍 Czy platforma lub region wpływają na zaangażowanie?
# Może użytkownicy mobile mają mniej eventów?
    # nie robilismy zadan pod taka analize nie moge stiwerdzic
# A może w jednym regionie subskrybują szybciej?
    # nie robilismy zadan pod taka analize nie moge stwierdzic

#3. ⏱ Kiedy użytkownicy najczęściej subskrybują?
# Krótko po rejestracji?

# Czy może po dłuższym czasie, np. po testowaniu?
    # subskrybuja po jakims czasie czyli po testowaniu

#     4. 💰 Który plan jest bardziej atrakcyjny — basic czy pro?
# Co sugerują liczby (popularność, czas decyzji, aktywność)?

# Czy różnica w czasie (16 vs 41 dni) może sugerować coś o strategii?
    # sugeruje moze to ze cena planu basic jak na jego funckjonalnosci jest o wiele bardziej atrakcyjna niz wersja pro


    #5. 📌 Rekomendacje marketingowe lub produktowe
# Czy warto przypominać o planie pro po X dniach?
    # RACZEJj nie, jest to zbyt agresywna reklama ktora nie nalzy do przyjemnych dla uzytkownika, chyba ze z jakims discountem
# Czy zachęcać szybciej do subskrypcji na mobile?
    # nie robilismy pod to analizy
# Może w jakimś regionie warto zwiększyć obecność?  # nie robilismy pod to analizy