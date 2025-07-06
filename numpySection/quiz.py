import numpy as np
# 📌 Podstawy i indeksowanie
# 1.Czym różni się slicing od indeksowania pojedynczego elementu w NumPy?
    # indeksowanie pojedynczego elementu daje nam dostep do tego elementu arrayu, a slicing polega na uzyskaniu dostepu do jakiejs docelowej porcji arrayu
# 2.Co oznacza [:], [::], [::-1] w kontekście arrayów?
    # [:] - oznacza caly array \, [::] to samo co [:], a [::-1] oznacza array od tylu
# 3.Jak działa indeksowanie warunkowe w NumPy?
    # cos jak w pandas czyli tworzymy maske logiczna dla jakiegos warunku, zwracane sa true/false dla danego elementu i sa nastepnie brane tylko te elementy ktore w masce byly True
# 4.Jakie są różnice między listą Pythona a tablicą NumPy?
    #numpy array jest o wiele szybsze ze wzgledu na to jak zostalo zbudowane, pamiec jest bardzfiej poukladana a dostep do niej jest bardziej jakby pokolei
    #
# 5.Co zwróci arr[1:4] dla arrayu np.array([10, 20, 30, 40, 50])?
    #array[20,30,40]
# 📌 Właściwości i typy danych
# 6.Jakie właściwości (atrybuty) ma ndarray (np. shape, dtype, ndim)?
    #shape to jest ksztat arrayu np (3,1) (3,), d type to sa jakie ma typy danych, ndim to jest ilosc wymiarow
# 7.Co się stanie, gdy spróbujesz przypisać wartość typu str do int arraya?
    #numpy autmatyczne zamieni caly array na object


# 8.Jak sprawdzić typ danych wewnątrz tablicy NumPy?
    # poprzez arr.dtype
# 9.Czym różni się object od string i number w kontekście NumPy?
    # object to dowlony tymp a string i int to konkrete typy jednorodne
# 10.Jakie są zalety korzystania z jednorodnych typów danych w NumPy?
    # latwiejsze i bardziej przewidywalne operacje, mniejsze pradopobienstwo na bledy
# 📌 Operacje element-wise
#11. Jakie operacje można wykonać element-po-elemencie w NumPy?
    # sa to operacjie arymetryczne
# 12.Co zwróci arr * 2 dla arr = np.array([1, 2, 3])?
    # array[2,4,6]
# 13.Czym różni się * od @ w NumPy?
    # * jest to mnozenie macierzy, @ jest to dot product macierzy czyli wychodzi skalar
# 14,Jak zastosować funkcję np.where() do warunkowego przypisywania?
    #   np.where(conidtion,if fullfiled x, if not y)
# 15.Jak sprawdzić, które elementy w arrayu są większe niż np. 5?
    #array = array[array > 5], np.where(arr > 5)

# 📌 Tworzenie i przypisywanie
# 16.Jak stworzyć array z samymi zerami/jedynkami?
    # metoda np.zeros albo np.ines
# 17.Jak przypisać wartość do wycinka arraya (np. arr[1:3] = 0)?
#x = np.array((exampleArray)), x[1:3] = 0, 
#18. Czym różni się np.full() od np.zeros() i np.ones()?
    # tym ze mozna dac jaka chce sie liczbe
# 19.Jak stworzyć array w zakresie 0–100 co 5?
    #np.arange(0,100,5)
# 20.Jak ustawić wartość tylko dla elementów spełniających warunek?
    #array[array>3] = 100
# 📌 Losowość i rozkłady
# 21.Jak działa np.random.seed() i po co się go używa?
    #generuje losowe liczby nie wiem jak dziala, uzywa sie go by zainicializowac randomowe numery
#22. Czym różni się rand(), randint() i normal() w NumPy?
    #rand generuje losowa liczbe, randint generuje losowego int, normal generuje losowa liczbe z rozkladu normalnego
# 23.Jak wylosować 5 elementów z przedziału 0–10 bez powtórzeń?
    #np.random.choice(np.arange(0, 11), size=5, replace=False)
# 24.Jak stworzyć histogram z wartości arraya?
    #np.histogram(data,bins)
# 📌 Braki danych i manipulacja
# 25.Jak sprawdzić, które elementy w arrayu są NaN?
    #metoda isnan, lub pokaz mi inna metode
# 26.Jak zamienić NaN na 0?
    #metoda nan_to_num lub metda where, lub mozesz pokazac inna metode
# 27.Jak usunąć NaN z arraya?
    #data = data[~np.isnan(data)], mozesz pokazac i ine metody
# 28.Czym różni się .reshape() od .ravel() i .flatten()?
    #reshape – nowy widok/tablica o innym kształcie.
# reshape – nowy widok/tablica o innym kształcie.

# ravel – 1D widok (płaski), szybki.

# flatten – 1D kopia, zawsze nowy obiekt.
# 29.Jak połączyć dwa arraye poziomo i pionowo?
    #metodami stack lub concatenate
# 30.Jak znaleźć unikalne wartości w arrayu?
    #metoda unique
