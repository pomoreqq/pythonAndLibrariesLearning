# 📘 QUIZ: Pandas Basics (30 Questions)

# 1. Jak utworzyć DataFrame z listy słowników?  
#   df = pd.DataFrame(listOfDict)     
# 2. Jak wczytać dane z pliku CSV o nazwie "sales.csv"?
    #df = pd.read_csv('sales.csv')

# 3. Jak dodać nową kolumnę "total" jako iloczyn kolumn "price" i "quantity"?
    #df['total'] = df['price'] * df['quantity']
# 4. Jak przefiltrować wiersze, gdzie kolumna "category" równa się "books"?
    #filteredDf = df[df['category'] == 'books']
# 5. Jak posortować DataFrame według kolumny "price" malejąco?
    #sortedDf = df.sort_values('price',ascending=False)
# 6. Jak ustawić kolumnę "id" jako indeks?
    #dfIdSet = df.set_index('id')
# 7. Jak zresetować indeks do domyślnych wartości liczbowych?
    #dfResetIndex = df.reset_index()
# 8. Czym się różni `loc[]` i `iloc[]`? Podaj przykład.
    #loc  umozliwia dostep do kolumn i wierszy po label index czyli np result = df.loc['a','b'] a iloc po numerycznym indexie result = df.iloc[1,2]
# 9. Jak policzyć średnią dla kolumny "sales"?
    #mean_sales = df['sales'].mean()
# 10. Jak zsumować wartości w kolumnie "revenue"?
        #df.groupby('category')['total'].sum().idxmax()
# 11. Jak połączyć dwa DataFrame po kolumnie "product" metodą wewnętrzną (inner join)?
    #mergedDf = pd.merge(df1,df2, on='product', how='inner')
# 12. Co oznacza `how='outer'` w `merge()`?
    #laczenie wszystkich wierszy nawet jak nie maja dopasowania
# 13. Jak utworzyć nową kolumnę "seniority", gdzie wiek > 30 to "senior", inaczej "junior"?
    #df['seniority'] = df['age'].apply(lambda x: 'senior' if x > 30 else 'junior')
# 14. Jak zgrupować dane po kolumnie "region" i zsumować kolumnę "sales"?
    #groupedByAndSumed = df.groupby('region')['sales'].sum()
# 15. Jak znaleźć nazwę kategorii, która ma największy przychód?
    #groupedByAndSumed = df.groupby('category')['sales'].sum()
    #indexOfMax = groupedByAndSumed.idxmax()
    #print(groupByAndSumed[indexOfMax])
# 16. Co robi metoda `apply()` i w jakiej sytuacji ją stosujesz?
    #apply umozliwa stosowanie funkcji na series, stosuje w celu specjalnych przeksztalcen
# 17. Co oznacza `axis=0` i `axis=1` w `sum()`?
    #axis 0 oznacza sumuj wartosci w kuolumnach po wierszach
# 18. Jak policzyć liczbę wystąpień wartości w kolumnie "department"?
         #valueCounts = df['department'].value_counts()
# 19. Jak wybrać tylko kolumny "name" i "salary" z DataFrame?
    #selectedColumns = df.loc[:,['name','salary']]
# 20. Jak sprawdzić typy danych wszystkich kolumn?
        #df.dtypes
# 21. Jak sprawdzić, czy są puste wartości (`NaN`) w kolumnie "email"?
    #isNan = df['email'].isna()
# 22. Jak usunąć kolumnę "temp_column"?
    # df = df.drop('tem_column',axis=1)
# 23. Jak usunąć wiersze zawierające `NaN`?
    #withoutNan = df[:].dropna()
# 24. Jak uzupełnić brakujące dane w kolumnie "price" wartością 0?
    #df['price'].fillna(0, inplace=True)
# 25. Jak zapisać DataFrame do pliku CSV bez indeksu?
        #df.to_csv('out.csv',index=False)
# 26. Jak zmienić kolejność kolumn — np. aby kolumna "name" była pierwsza?
        #df = df[['name', 'price', 'quantity', ...]]
# 27. Jak sprawdzić podstawowe statystyki (min, max, mean, std) dla kolumn liczbowych?
    # za pomoca metody describe()
# 28. Jak sprawdzić, ilu unikalnych klientów znajduje się w kolumnie "client_id"?
    #dfUnique = df['client_id'].unique()
# 29. Jak sprawdzić, ile produktów zostało sprzedanych każdego dnia?
    # groupByAndSumed = df.groupby('day')['sales'].sum()
# 30. Jakie są różnice między `Series` a `DataFrame`?
    #data frame to zbior seriesow cos jak matrix i vektor
# ✍️ Uzupełnij odpowiedzi w osobnym pliku .py lub .ipynb jako komentarze lub kod.


# 1. Jak utworzyć DataFrame z listy słowników zawierających dane o imieniu i wieku?
    # df = pd.DataFrame(listofdict)
# 2. Jak dodać kolumnę "seniority", która przypisuje "senior" jeśli wiek > 30, inaczej "junior"? 
    #df['seniority'] = df['wiek'].apply(lambda x: 'senior' if x > 30 else 'junior' )
# 3. Jak odfiltrować tylko pracowników z działu "IT"?
        #filteredDf = df[df['employee'] == 'IT']
# 4. Jak ustawić kolumnę "name" jako indeks, a potem go zresetować?
        # df.set_index('name')
        #df.reset_index()
# 5. Jak posortować DataFrame według wieku malejąco?
    #sortedDf = df.sort_values('age',ascending=False)
# 6. Jak obliczyć średnią wieku wszystkich pracowników?
    #workersMean = df['workers'].mean()
# 7. Jak utworzyć kolumnę "revenue" jako iloczyn kolumn "sales" i "price"?
    #df['revenue'] = df['sales'] * df['price']
# 8. Co robi metoda `merge()`? Jak połączyć dwa DataFrame po kolumnie "product"?
    # laczy kolumny po pasujacych wartosiach kolumn
    #mergedDf = pd.merge(df1,df2, on='product', how='inner')
# 9. Jak wygląda wynikowy DataFrame po użyciu `merge(..., how="right")`?
        #prawa kolumna zostawia wszystkie wiersza a dodawane sa tylko pasujace z lewej
# 10. Jak zgrupować dane po kolumnie "category" i policzyć sumę kolumny "total"?
    #groupedAndSum = df.groupby('category')['total'].sum()
# 11. Jak znaleźć kategorię z najwyższym przychodem?
    # groupedAndHighest = df.groupby('category').idxmax()
# 12. Jak zgrupować dane po "date" i policzyć łączną sprzedaż?
    #groupedAndSum = df.groupby('date')['total'].sum()
# 13. Jak posortować DataFrame rosnąco według wartości w kolumnie "total"?
    # sortedDf = df.sort_values('total')
# 14. Jak użyć `apply()` do przekształcenia kolumny stringów na małe litery?
    #df['exampleStringCol'] = df['exmapleStringCol].apply(lambda x: x.lower())
# 15. Jak za pomocą list comprehension utworzyć nową kolumnę na podstawie innej?
    # df['newCol'] = [df['newCol'].append(x) for x in df['oldCol'] ]
# 16. Jakie metody możesz użyć do usunięcia duplikatów?
        #metody duplicated
# 17. Jak sprawdzić typy danych wszystkich kolumn?
        #df.dtypes
# 18. Jak odczytać plik CSV i od razu ustawić kolumnę "id" jako indeks?
    # df = pd.read_csv('xyz.cxv', index_col = 'id')
# 19. Jak usunąć kolumnę "temp_column" z DataFrame?
    #newDf = df.drop('temp_column')
# 20. Jak znaleźć liczbę unikalnych wartości w kolumnie "region"? 
    # uniqueDf = df['region'].unique()
# 21. Co oznacza `axis=0` w `groupby().sum()`?
    #grupuje po wierszach i je sumuje. wytlumacz mi to dokladniej
# 22. Jak sprawdzić, ile produktów sprzedano w każdym dniu?
    #groupByDay = df.groupby('day')['total'].sum()
# 23. Jakie statystyki podstawowe zwraca metoda `describe()`?
    #liczbe wartosci,srednia, odchylenie standardowe, najmniejszsa wartosc do maksymalnej
# 24. Czym różni się `df['col']` od `df[['col']]`?
    # pierwsze wybiera dana kolumne a drugie ustawa dana kolumne jako 1 w dataframe
# 25. Jak zapisać DataFrame do pliku CSV bez indeksu?
    #df.to_csv(index=False)