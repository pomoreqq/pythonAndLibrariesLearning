import numpy as np


# Temat:
# Analiza zachowan uzytkownikow platformy streamingowej
# Opis danych:
# Kazdy rekord to jedna sesja uzytkownika i zawiera:
# - user_id: ID uzytkownika (int)
# - content_id: ID ogladanego filmu/serialu (int)
# - watch_time: Czas ogladania w minutach (float: 1.0 - 180.0)
# - subscription_type: Typ subskrypcji: "Basic", "Standard", "Premium"
# - device: Urzadzenie: "Mobile", "Desktop", "TV"
# - watched_to_end: Czy obejrzano material do konca? 1 - tak, 0 - nie
# - watch_date: Data ogladania (string: "2023-01-01" do "2023-01-31")

np.set_printoptions(linewidth=200,edgeitems=10)
headers= np.genfromtxt('numpyBiggerExercise/streaming_data_dirty.csv',delimiter=',',dtype=np.str_,max_rows=1)



data = np.genfromtxt('numpyBiggerExercise/streaming_data_dirty.csv',delimiter=',',skip_header=1,dtype=np.str_,encoding='utf-8')



# Etap 1: Wstepne przygotowanie danych
# 1. Usun lub popraw bledne wartosci w watch_time (ujemne, powyzej 200).
watchTime = data[:,2]
watchTime = watchTime.astype(np.float32)
# isNegativeTime = watchTime[watchTime < 1].any()
# isAbove180 = watchTime[watchTime > 180].any()
meanOfWatchTime = np.mean(watchTime)
watchTime = np.where((watchTime < 1) | (watchTime > 180),meanOfWatchTime,watchTime)
data[:,2] = watchTime
# isNegativeTime = watchTime[watchTime < 1].any()
# isAbove180 = watchTime[watchTime > 180].any()
# print(np.isnan(watchTime).any())
# 2. Ujednolic subscription_type i device (np. BASIC -> Basic, mobille -> Mobile).

def toLowerCase(arr):
    return np.strings.lower(arr)
vfunc = np.vectorize(toLowerCase)

indicesOfNullSubType = np.where(data[:,3] == 'Null')
data = np.delete(data,indicesOfNullSubType,axis=0)

subType = data[:,3]
subType = vfunc(subType)
data[:,3] = subType



indicesOfNullDevices = np.where((data[:,4] == 'NULL') | (data[:,4] == 'mobille'))
data = np.delete(data,indicesOfNullDevices,axis=0)

devicesFirst = data[:,4]
devicesFirst = vfunc(devicesFirst)
data[:,4] = devicesFirst
# 3. Usun/oznacz bledne watch_date (puste lub bledne formaty).
watchedDate = data[:,6]
# print(len(watchedDate))
indices = np.where((watchedDate == 'INVALID') | (watchedDate ==''))
data = np.delete(data,indices,axis=0)
# print(len(data))
# # 4. Usun/oznacz rekordy z watched_to_end = None.
watchedToEnd = data[:,5]
watchedToEnd = np.where(watchedToEnd == '','0',watchedToEnd)
data[:,5] = watchedToEnd



# 5. Oblicz:
# - Sredni i medianowy czas ogladania (watch_time). 90,9 srednia, mediana 90,9
watchTimeSecond = data[:,2].astype(np.float32)
medianOfWatchTime = np.median(watchTimeSecond)

# - Procent sesji zakonczonych pelnym obejrzeniem (watched_to_end = 1). okolo 45,45 %
watchedToEndSecond = data[:,5]
isCompletedPercentage = (len(watchedToEnd[watchedToEnd == '1']) / len(watchedToEndSecond)) * 100

# - Top 3 najczesciej uzywane urzadzenia (device). najczesciej uzywanie jest mobile 411, potem desktop 329 a na koniec tv 195
print(headers)
devices = data[:,4]
uniqueDevices = np.unique(devices,return_counts=True)
# print(f'unikalne urzadzenia: {uniqueDevices[0]}: i kolejno ich ilosc: {uniqueDevices[1]}')
# - Liczbe unikalnych uzytkownikow (user_id)/ 101 unikalnych uzytkownikow
uniqueUsersLen = len(np.unique(data[:,0]))




# Etap 3: Analiza subskrypcji
# 6. Dla kazdego subscription_type:
# - Sredni czas ogladania. dla basic jest to 90,1, dla standard 89,6, dla premium 92,17
watchTimeThird = data[:,2]

subTypeSecond = data[:,3]
indicesOfBasic = np.where(subTypeSecond == 'basic')
basicWatchTime = watchTimeThird[indicesOfBasic].astype(np.float32)
meanOfBasicWatchTime = np.mean(basicWatchTime)


indicesOfStandard = np.where(subTypeSecond == 'standard')
standardWatchTime = watchTimeThird[indicesOfStandard].astype(np.float32)
meanOfStandardWatchTime = np.mean(standardWatchTime)


indicesOfPremium = np.where(subTypeSecond == 'premium')
premiumWatchTime = watchTimeThird[indicesOfPremium].astype(np.float32)
meanOfPremiumWatchTime = np.mean(premiumWatchTime)

# unique_subs, inverse = np.unique(data[:,3], return_inverse=True)

# for i, sub in enumerate(unique_subs):
#     mask = inverse == i
#     avg_watch = np.mean(data[mask, 2].astype(float))
#     print(f'{sub}: {avg_watch:.2f}')
# - Procent zakonczonych sesji. dla basic to 43,6%, dla standard 44,8%, premium 48,9%
watchedToEndThird = data[:,5]

valueOfBasicInWatchedToEnd = watchedToEndThird[indicesOfBasic]
percentageOfBasic = (len(valueOfBasicInWatchedToEnd[valueOfBasicInWatchedToEnd == '1']) / len(valueOfBasicInWatchedToEnd)) * 100

# for i,sub in enumerate(unique_subs):
#     mask = inverse == i
#     groupSessions = watchedToEndThird[mask]
#     percentage = (np.sum(groupSessions == '1') / len(groupSessions)) * 100
#     print(f"{sub}: {percentage:.2f}% sesji zakończonych pełnym obejrzeniem")

valueOfStandardInWatchedToEnd = watchedToEndThird[indicesOfStandard]
percentageOfStandard = (len(valueOfStandardInWatchedToEnd[valueOfStandardInWatchedToEnd == '1']) / len(valueOfStandardInWatchedToEnd)) * 100


valueOfPremiumInWatchedToEnd = watchedToEndThird[indicesOfPremium]
percentageOfPremium = (len(valueOfPremiumInWatchedToEnd[valueOfPremiumInWatchedToEnd == '1']) / len(valueOfPremiumInWatchedToEnd)) * 100



# Etap 4: Dniowa aktywnosc
# 7. Jaki dzien tygodnia generuje najwiecej ogladalnosci (suma watch_time)? poniedzialek

from datetime import datetime
watchedDateSecond = data[:,6]
watchTimeFourth = data[:,2].astype(np.float32)

def getDayName(dateString):
    return datetime.strptime(dateString,"%Y-%m-%d").strftime("%A")

vGetDayName = np.vectorize(getDayName)

dayNames = vGetDayName(watchedDateSecond)

uniqueDays,inverseIndicies = np.unique(dayNames,return_inverse=True)

totalWatchArr = list()
for i,day in enumerate(uniqueDays):
    mask = inverseIndicies == i
    totalWatch = np.sum(watchTimeFourth[mask])
    totalWatchArr.append(totalWatch)

indiceOfMaxSumDay = np.argmax(totalWatchArr)
maxDay = uniqueDays[indiceOfMaxSumDay]

# # Monday
# mondayIndices = np.where(dayNames == 'Monday')
# mondayWatchTime = watchTimeFourth[mondayIndices]
# sumOfMonday = np.sum(mondayWatchTime)

# # Tuesday
# tuesdayIndices = np.where(dayNames == 'Tuesday')
# tuesdayWatchTime = watchTimeFourth[tuesdayIndices]
# sumOfTuesday = np.sum(tuesdayWatchTime)

# # Wednesday
# wednesdayIndices = np.where(dayNames == 'Wednesday')
# wednesdayWatchTime = watchTimeFourth[wednesdayIndices]
# sumOfWednesday = np.sum(wednesdayWatchTime)

# # Thursday
# thursdayIndices = np.where(dayNames == 'Thursday')
# thursdayWatchTime = watchTimeFourth[thursdayIndices]
# sumOfThursday = np.sum(thursdayWatchTime)

# # Friday
# fridayIndices = np.where(dayNames == 'Friday')
# fridayWatchTime = watchTimeFourth[fridayIndices]
# sumOfFriday = np.sum(fridayWatchTime)

# # Saturday
# saturdayIndices = np.where(dayNames == 'Saturday')
# saturdayWatchTime = watchTimeFourth[saturdayIndices]
# sumOfSaturday = np.sum(saturdayWatchTime)

# # Sunday
# sundayIndices = np.where(dayNames == 'Sunday')
# sundayWatchTime = watchTimeFourth[sundayIndices]
# sumOfSunday = np.sum(sundayWatchTime)

# array = np.array([sumOfTuesday,sumOfMonday,sumOfWednesday,sumOfThursday,sumOfFriday,sumOfSaturday,sumOfSunday])
# maxFrom = np.max(array).argmax()
# days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
# print(days[maxFrom])


# 8. Ktory dzien ma najnizszy wskaznik zakonczonych ogladan (watched_to_end = 1)? poniedzialek


watchToEndFourth = data[:,5]
totalPercentageArr = []
for i,day in enumerate(uniqueDays):
    mask = inverseIndicies == i
    groupDays = watchToEndFourth[mask]
    percentage = (np.sum(groupDays == '1') / len(groupDays)) * 100
    totalPercentageArr.append(percentage)

indiceOfMaxPercentage = np.argmin(totalPercentageArr)
minDay = uniqueDays[indiceOfMaxPercentage]



# mondayIndices = np.where(dayNames == 'Monday')
# mondayWatchToEnd = watchToEndFourth[mondayIndices]
# mondayPercentage = (np.sum(mondayWatchToEnd == '1') / len(mondayWatchToEnd)) * 100
# print(mondayPercentage)
    

# Etap 5: Wnioski i podsumowanie
# 9. Czy ktorys typ uzytkownikow (np. Premium) oglada istotnie dluzej?
#tak zdecydowanie, uztykownicy premium sa ponad srednia sesji zakonczych ogladaniem do konca oraz srednim czasem ogladania
# 10. Czy dane pokazuja typowe anomalie, ktore warto zglosic jako insig
    # tak, poniedzialek jest czasem najdluszego ogladania a jednoczesnie ma najwiecej niedokonczych sesji ogladania