# 📘 QUIZ: Pandas Basics (30 Questions)

# 1. Jak utworzyć DataFrame z listy słowników?  
#   df = pd.DataFrame(listOfDict)     
# 2. Jak wczytać dane z pliku CSV o nazwie "sales.csv"?
    #df = pd.read_csv('sales.csv')

# 3. Jak dodać nową kolumnę "total" jako iloczyn kolumn "price" i "quantity"?
    #df['total'] = df['price'] * df['quantity']
# 4. Jak przefiltrować wiersze, gdzie kolumna "category" równa się "books"?
    #filteredDf = df[df['category'] == books]
# 5. Jak posortować DataFrame według kolumny "price" malejąco?
    #sortedDf = df.sort_vales('price',ascending=False)
# 6. Jak ustawić kolumnę "id" jako indeks?
    #dfIdSet = df.set_indes('id')
# 7. Jak zresetować indeks do domyślnych wartości liczbowych?
    #dfResetIndex = df.rest_index()
# 8. Czym się różni `loc[]` i `iloc[]`? Podaj przykład.
    #loc  umozliwia dostep do kolumn i wierszy po label index czyli np result = df.loc['a','b'] a iloc po numerycznym indexie result = df.iloc[1,2]
# 9. Jak policzyć średnią dla kolumny "sales"?
    #mean_sales = df['sales'].mean()
# 10. Jak zsumować wartości w kolumnie "revenue"?
        #sumOfRevenue() = df['revenue'].sum()
# 11. Jak połączyć dwa DataFrame po kolumnie "product" metodą wewnętrzną (inner join)?
    #mergedDf = pd.merge(df1,df2, on='product' how='inner')
# 12. Co oznacza `how='outer'` w `merge()`?
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
    #axis 0 oznacza ze sumujemy kolumny a axis 1 ze wiersze
# 18. Jak policzyć liczbę wystąpień wartości w kolumnie "department"?
         #valueCounts = df.value_counts('department')
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
