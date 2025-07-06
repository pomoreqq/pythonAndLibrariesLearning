import numpy as np
import numpy.ma as ma
from random import sample
# 📌 Zadanie 1: Slicing + modyfikacja
# Stwórz tablicę NumPy o wartościach od 0 do 99. Zamień wartości w ostatnich 10 pozycjach na -1.

# array = np.array((range(0,100)))

# array[90:] = -1

# print(array)

#📌 Zadanie 2: Operacje element-wise
# Masz tablicę arr = np.array([1, 2, 3, 4, 5]). Podnieś każdy element do kwadratu, a następnie odejmij 2.

# arr = np.array([1, 2, 3, 4, 5])

# arr = arr**2 - 2
# print(arr)

# 📌 Zadanie 3: Indeksowanie warunkowe
# Wygeneruj tablicę losową 100 liczb całkowitych od 0 do 20. Wyodrębnij tylko liczby większe niż 10 i podziel je przez 2.


# arr = np.array(np.random.randint((20), size=100))
# arr = arr[arr > 10] / 2
# print(arr)



# 📌 Zadanie 4: Tworzenie maski logicznej
# Zbuduj maskę logiczną, która wskaże, 
# które wartości w tablicy arr = np.array([5, np.nan, 7, 3, np.nan, 10]) są liczbami (czyli nie są NaN), i użyj jej do wyodrębnienia tych wartości.

# arr = np.array([5, np.nan, 7, 3, np.nan, 10])

# arr = arr[~np.isnan(arr)]
# print(arr)


# 📌 Zadanie 5: Transformacje kształtu
# Stwórz tablicę NumPy od 1 do 12, a następnie przekształć ją w tablicę 3x4. Zamień ją na jednowymiarową w możliwie najbardziej płaski sposób.


# arr = np.array(range(1,13))
# arr = np.reshape(arr,(3,4))
# arr = arr.flatten()
# print(arr)


# 📌 Zadanie 6: Losowość i reproducja
# Wylosuj tablicę 5×5 liczb zmiennoprzecinkowych z przedziału 0–1, ale tak, by za każdym razem wyniki były identyczne (tzn. seed).

# np.random.seed(100)
# arr = np.array(np.random.uniform(low=0,high=1,size=(5,5)))
# print(arr)

# 📌 Zadanie 7: Histogram z danych
# Wygeneruj 1000 liczb z rozkładu normalnego i policz ile z nich mieści się w przedziale od -1 do 1.

# arr = np.array(np.random.normal(size=1000))

# count = arr[(arr > -1) & (arr < 1)].shape
# print(count)


# 📌 Zadanie 8: Zamiana wartości
# Masz tablicę arr = np.array([1, 2, 3, 4, 5]). Zamień wartości większe niż 3 na 99.

arr = np.array([1, 2, 3, 4, 5])

arr = np.where(arr > 3,99,arr)
# print(arr)

# 📌 Zadanie 9: Agregacje i unikalność
# Stwórz tablicę losowych wartości całkowitych 0–9 o rozmiarze 100. Policz liczbę wystąpień każdej wartości.

array = np.array(np.random.randint(low=0,high=9,size=100))
uniqueArr = np.unique_counts(array)
vals, counts = np.unique(arr, return_counts=True)
# print(dict(zip(vals, counts)))
# print(uniqueArr)

# 📌 Zadanie 10: Wybór i losowanie
# Z tablicy 1D 100 elementów wybierz 10 unikalnych, losowych wartości bez powtórzeń.

#arr = np.arange(100)
# sampled = np.random.choice(arr, size=10, replace=False)
# print(sampled)