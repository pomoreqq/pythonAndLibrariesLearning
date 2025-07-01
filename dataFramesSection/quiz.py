# 1–10: Podstawowe operacje na DataFrame
# Jakie są różnice między .iloc[] a .loc[] w kontekście indeksowania?
    #iloc uzywa sie po indeksach numerycznych a loc po label basing
# Co zwraca df.iloc[2:5, [0, 2]]?
    #zwraca z dataframe wiersze 2-4 kolumn 0 i 2
# Jak sprawdzić, czy kolumna "A" zawiera jakiekolwiek wartości NaN?
    # df['A'].isna().any()
# Czym się różni df['A'] od df[['A']]?
    # pierwsze to jest wybor danej kolumny a drugie to przypisanie jej jako pierwszej kolumny
# Jak usunąć kolumnę "B" z DataFrame bez modyfikowania oryginału?
    #newDf = df.drop('B',axis=1)
# Jak ustawić kolumnę "id" jako indeks w DataFrame?
    # df.set_index('id')
# Jakie metody służą do filtrowania DataFrame w oparciu o wartości logiczne?
    # apply z lambdami, uzywanie filtrowania maskowego czyli df[mask], isin(),query(), loc, iloc
# Jak zaokrąglić wszystkie liczby zmiennoprzecinkowe do 2 miejsc po przecinku?
    # df.round(2)
# Czym się różni .apply() od .map() w kontekście kolumn DataFrame?
    # map dziala tylko na series a apply moze na dataframe, apply akceptuje tylko funkcje a map akceptuje funkcje,slowniki i series, apply operuje na wszystkioch wierszach lub kolumnach
    # dla data frame i one at time dla series apply i map operuje tylko na jednym elemncie at time. troche tego nie rozumie wytlumacz mi to
# Co zwróci df[df['col'].isin(['a', 'b'])]?
    #zwroci wartosci wierszy kolumn gdzie w masce wychodzi true
# 11–20: Agregacje, grupowania, sortowanie
# Jak posortować DataFrame po dwóch kolumnach: "age" rosnąco i "score" malejąco?
    # df.sort_values(by=['age','score'],ascending=[True,False] )
# Co zwróci df.groupby('category')['sales'].mean()?
    #zwroci sume sales dla kazdej kategori
# Co oznacza as_index=False w groupby()?
    # ze nazwy grup nie sa indeksami, wiec zostana przypisane numeryczne indeksy
# Jak obliczyć medianę salary dla każdej grupy "department"?
    # df.groupby('department')['salary'].median()
# Jak policzyć liczbę unikalnych user_id w każdej grupie "region"?
    # df.groupby('region')['user_id'].nunique()
# Jak usunąć duplikaty w kolumnie "user_id" pozostawiając pierwszy napotkany?
    # df.duplicates(subset='user_id', keep = first)
# Jak działa .agg() w kontekście groupby()?
    #umozliwia operacje agregacji danych czyli umozliwia na podstawie innych kolumn tworzenie nowych kolumn dla danych kazdej grupy
# Jak z groupby uzyskać jednocześnie count i mean?
    #df.groupby().agg(count = ('xxx','count'), mean = ('xxx','mean'))
# Czym się różni sort_values() od sort_index()?
    # nie wiem
# Jak posortować MultiIndex po jednym poziomie indeksu?
    # df.sortlevel(level ='xxx')
# 21–27: Operacje na kolumnach i danych
# Jak dodać nową kolumnę będącą różnicą dwóch istniejących kolumn?
    #df['new'] = df['a'] - df['b']
# Co robi df.assign(new_col=df['A'] + df['B'])?
    # tworzy nowa kolumne z sumy dwoch kolumn
# Jak zmienić typ kolumny "id" na str?
    #df['id'].astype(str)
# Jak wypełnić brakujące wartości w kolumnie "age" średnią?
    #df['col'].fillna(value=df['col'].mean())
# Co robi .replace({'old': 'new'})?
    # zamienia wartosci starej kolumny na nowej
# Jak sprawdzić liczbę wartości unikalnych w kolumnie "city"?
    # df['column'].nunique()
# Jak działa .query("score > 50 & gender == 'M'")?
    # filtruje dana kolumne/df po tym ze score ma byc wiekszy niz 50 i dla gender M
# 28–35: Inne: NumPy, merge, join, zaawansowane filtrowanie
# Jak połączyć dwa DataFrame po wspólnym indeksie?
    #pd.merge(df1,df2,left_index=True,right_index=True)
# Jak działa df.merge(df2, on='id', how='left')?
    #   merguje tylko te wiersze ktore w prawej kolumne zgadzaja sie z wierszami id lewej kolumny
# Co robi pd.concat([df1, df2], axis=1)?
    # laczy do siebie obok w plaszczyznie wertykalnej czyli jako kulmny
# Jak zresetować indeks bez dodawania go jako kolumny?
    #df.reset_index(drop=True)
# Jak zamienić wszystkie kolumny typu object na typ category?
    #df.astype({col:'category' for col in df.select_dtypes('object').columns})
# Co oznacza errors='coerce' w pd.to_numeric()?
    #ze zamienia w kolumnie jak sa stringi na nan
# Jakie są różnice między copy() a przypisaniem referencyjnym (=)?
    # tworzy totalnie nowa kopie copy() a przypisanie refenrecyjne jesto to pointer do oryginalnego obiektu wiec jesli zrobi zmiane na kopi to zostanie zmiana zastosowana na oryginale
# Jak wyeksportować DataFrame do pliku CSV bez indeksu?
    #df.to_csv('xxx',index=False)
