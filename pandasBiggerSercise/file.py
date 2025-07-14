import pandas as pd


data = pd.read_csv('pandasBiggerSercise/sales_team_activity_5000_dirty.csv')

# 🗃️ Zbiór danych: sales_team_activity_5000_dirty.csv
# Kolumny:
#     • rep_id – ID handlowca
#     • date – data wizyty (różne formaty, część braków)
#     • client_name – nazwa klienta (może być missing, -)
#     • visit_duration – długość wizyty w minutach (czasem missing)
#     • value_usd – wartość sprzedaży (liczbowa, czasem brak)
#     • status – status wizyty (różne wersje tego samego słowa)
#     • city – miasto klienta (różne warianty zapisu)
#     • is_absent – czy handlowiec był nieobecny (yes, YES, No, no)
#     • notes – luźne notatki o spotkaniu

# ✅ Etap 1: Czyszczenie danych
# Wyczyszczenie brudnego zbioru:
#     • 🧼 Zmień formaty dat (date) na spójny, / done
#     • 🧽 Standaryzuj city, status, is_absent, client_name,
#     • 🗑️ Usuń wiersze bez date i client_name (missing, -), / done
#     • 🔢 Zamień visit_duration i value_usd na typ liczbowy, / done
#     • 📉 Uzupełnij braki w visit_duration rozsądnie (np. mediana), / done
#     • ❓ Zdecyduj, co zrobić z brakami value_usd – usuń? uśrednij? (obroty? długość wizyty?)



#praca z kolumna date
#ilosc nanow w data
# dateNanQuantity = data['date'].isna().sum()
# print(dateNanQuantity)
#1272 nanow wiec je dropne
data = data[~data['date'].isna()]

dateNanQuantity = data['date'].isna().sum()
# print(dateNanQuantity)
# print(data)
#zostalo 3728 rowow

#teraz ustandaryzuje date
data['date'] = data['date'].apply(lambda x: pd.to_datetime(x,dayfirst=True,format="mixed").strftime(format="%Y-%m-%d"))
data['date'] = data['date'].astype('datetime64[ns]')
#praca z clientname columna
clientNameUnique = data['client_name'].unique()
clientNameValueCounts = data['client_name'].value_counts()

# print(clientNameValueCounts)
# 427 REKORDOW TO Missing oraz znak minusa to 416 usune je wszystkie
data = data[(data['client_name'] != '-') & (data['client_name'] != 'missing')]

clientNameUnique = data['client_name'].unique()
clientNameValueCounts = data['client_name'].value_counts()
# print(clientNameValueCounts)
# print(clientNameUnique)
#zostalo 2885 rowow/ zmieniam typ danych z object na category w client name
data['client_name'] = data['client_name'].astype('category')

#teraz zajmuje sie kolumna visitDuration

#wypisuje unikalne wartosci
# visitDurationUnique = data['visit_duration'].unique()
# print(visitDurationUnique)
#zamieniam wartosci missing na 30 uznaje to za standardowy czas wizity oraz wpierw musze zamienic te missin g zeby moc zmienic typ danych kolumny na integer
data['visit_duration'] = data['visit_duration'].replace(to_replace='missing',value='30')
data['visit_duration'] = data['visit_duration'].astype('Int32')
visitDurationUnique = data['visit_duration'].unique()
# print(visitDurationUnique)


# kolumna valueusd jest 260 nanow, zapelnie je mediana kolumny valueUSD
isNaValuesUSD = data['value_usd'].isna().sum()
medianValueUSD = data['value_usd'].median()
data['value_usd'] = data['value_usd'].fillna(value=medianValueUSD)
# isNaValuesUSD = data['value_usd'].isna().sum()
# print(isNaValuesUSD)

uniqueValuesUSD = data['value_usd'].unique()



# kolumna status teraz
#ma zero nanow
isNansStatus = data['status'].isna().sum()
uniqueStatus = data['status'].unique()
# print(uniqueStatus) # standaryzuje wszystkie statusy do lowercase
data['status'] = data['status'].apply(lambda s: s.lower())
# uniqueStatus = data['status'].unique()
# print(uniqueStatus) # 
data['status'] = data['status'].astype('category')


#zajmuje sie teraz kolumna city
#sprawdzam ilosc nanow
isNansCity = data['city'].isna().sum()
# print(isNansCity) 0 nanow
#standaryzuje nazwy miast bo zobaczylem ze niektore sa lowercase tak zeby pierwsza litera byla duza
data['city'] = data['city'].apply(lambda s: s.capitalize())
data['city'] = data['city'].astype('category')

#kolumna is absent

isNanAbsent = data['is_absent'].isna().sum()
# print(isNanAbsent) 0 nanow, standaryzuje kolumne do lowerCase
data['is_absent'] = data['is_absent'].apply(lambda s: s.lower())
isAbsentValueCounts = data['is_absent'].value_counts()
# print(isAbsentValueCounts)

#kolumna notes
isNanNotes = data['notes'].isna().sum()
# print(isNanNotes) 0
notesUnique = data['notes'].unique()
notesValueCounts = data['notes'].value_counts()

data['notes'] = data['notes'].replace(['missing', '-'], 'No notes made')

# 🔧 Etap 2: Transformacja danych
# Przygotowanie do analizy:
#     • Dodaj kolumny:
#         ◦ day_of_week – dzień tygodnia,
#         ◦ week_number – numer tygodnia,
#     • Zakoduj kolumny tekstowe (is_absent, status, city – jeśli potrzebne),
#     • Stwórz agregacje tygodniowe i miesięczne per handlowiec

data['day_of_week'] = data['date'].dt.day_name()
data['week_number'] = data['date'].dt.strftime('%Y-%U')
data['month'] = data['date'].dt.month_name()




repGroupedByMonth = data.groupby(['rep_id','month']).agg(
    sumOfSales = ('value_usd',"sum"),
    meanOfSales = ('value_usd','mean'),
    visitCount = ('visit_duration','count'),
    meanVisitDuration = ('visit_duration','mean')
)

# 📈 Etap 3: Analiza danych (EDA)
# Odpowiedz na pytania:
# 🧑‍💼 Efektywność handlowców:
#     • Kto ma najwyższy średni obrót na wizytę?
#     • Kto odwiedza najwięcej klientów miesięcznie?
#     • Kto ma niski obrót mimo wielu wizyt?
# 🗓️ Czas i skuteczność:
#     • W które dni tygodnia osiągana jest najwyższa wartość sprzedaży?
#     • Czy długość wizyty koreluje z wartością sprzedaży?
#     • Czy krótkie wizyty są mniej skuteczne?
# 🚫 Nieobecności i skutki:
#     • Czy handlowcy z dużą liczbą nieobecności mają niższe wyniki?
#     • Czy są osoby często nieobecne, ale skuteczne?

#     • Kto ma najwyższy średni obrót na wizytę? handlowiec 104 ma najwiekszy obrot na wizyte


groupedByRep = data.groupby('rep_id').agg(
    sumOfSales = ('value_usd','sum'),
    visitCount = ('visit_duration','count'),
    meanVisitDuration = ('visit_duration','mean'),
    absentRatio = ('is_absent',lambda s: ((s == 'yes').sum() / s.count()) * 100 )
)

groupedByRep['ratioOfSumPerVisit'] = groupedByRep['sumOfSales'] / groupedByRep['visitCount'] 
idxMaxOfRatioSumPerVisit = groupedByRep['ratioOfSumPerVisit'].idxmax()

# • Kto odwiedza najwięcej klientów miesięcznie? rep103
groupedByRep['ratioOfMeanVisitPerMonth'] = groupedByRep['visitCount'] / 12
idxMaxOfMeanVisitPerMonth = groupedByRep['ratioOfMeanVisitPerMonth'].idxmax()

#  • Kto ma niski obrót mimo wielu wizyt? rep 101 mimo prawie najwiekszej liczby wizyt jego obrot jest najmniejszy

# 🗓️ Czas i skuteczność:
#     • W które dni tygodnia osiągana jest najwyższa wartość sprzedaży?najwieksza czesc handlowcow osiagala najwyzsza sprzedaz w piatki, a ogolnie najwyzsdzy wynik zdarzylsie we wtorek

groupedByDay = data.groupby(['rep_id','day_of_week']).agg(
    sumOfSales = ('value_usd','sum')
)
sortedData = groupedByDay.sort_values(by=['rep_id','sumOfSales'],ascending=[True,False])
#     • Czy długość wizyty koreluje z wartością sprzedaży? # wszyscy handlowcy mieli podobna srednia dlugosc wizyt od 49-51 minut wiec uznaje ze nie ma istotnej
#korelacji miedzy dlugoscia wizyty a wartoscia sprzedazy

#     • Czy krótkie wizyty są mniej skuteczne? # jak wyzej tak samo sadze ze nie widac tu istatnej korelacji
# #groupedByRep = data.groupby('rep_id').agg(
#     sumOfSales = ('value_usd','sum'),
#     visitCount = ('visit_duration','count'),
#     meanVisitDuration = ('visit_duration','mean')
# )

# 🚫 Nieobecności i skutki:
#     • Czy handlowcy z dużą liczbą nieobecności mają niższe wyniki? nie nie jest to prawda, handlowiec 1 ma absent ratio na poziomie 5# a ma 4 najwyzszy wynik z tym rzecz ze nie
#odbiegaja od siebie bardzo miejsca 1-4
# groupedByRep = data.groupby('rep_id').agg(
#     sumOfSales = ('value_usd','sum'),
#     visitCount = ('visit_duration','count'),
#     meanVisitDuration = ('visit_duration','mean'),
#     absentRatio = ('is_absent',lambda s: ((s == 'yes').sum() / s.count()) * 100 )
# )
#     • Czy są osoby często nieobecne, ale skuteczne? 

#     • Kto ma najwyższy średni obrót na wizytę? handlowiec 104 ma najwiekszy obrot na wizyte