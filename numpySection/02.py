import numpy as np
# 🧩 Zadania: NumPy – Tablice 2D / 3D
# 📌 Zadanie 1: Sumy po wymiarach
# Stwórz tablicę 5×4 z liczbami od 0 do 19. Oblicz sumy:

# dla każdego wiersza (axis=1),

# dla każdej kolumny (axis=0),

# całościowo (bez podania osi).

# arr = np.reshape(np.array(np.arange(0,20)),shape=(5,4))

# arrColumnMean = arr.mean(axis=0)
# arrRowMean = arr.mean(axis=1)
# allMean= arr.mean()



# 2.Masz tablicę 4×3 z losowymi liczbami całkowitymi z przedziału 10–100.
# Dla każdego wiersza wykonaj normalizację:

# 1. Tworzymy tablicę
# arrr = np.random.randint(10, 101, size=(4, 3))
# print("Oryginalna tablica:\n", arrr)

# # 2. Obliczamy min i max dla każdego wiersza
# row_min = arrr.min(axis=1, keepdims=True)  # shape (4, 1)
# row_max = arrr.max(axis=1, keepdims=True)  # shape (4, 1)

# # 3. Normalizujemy
# normalized = (arrr - row_min) / (row_max - row_min)
# print("Znormalizowana tablica:\n", normalized)
#📌 Zadanie 3: Maska dla wartości brzegowych
# Dla tablicy 6×6 z wartościami losowymi z przedziału 0–1:

# Zamień wszystkie wartości z pierwszego i ostatniego wiersza oraz kolumny na 0 (obramowanie 0).

# Wnętrze pozostaje bez zmian.
# array = np.array(np.random.uniform(0,1,(6,6)))

# array[:,[0,5]] = 0
# array[[0,5],:] = 0
# print(array)


# 📌 Zadanie 4: Operacje między tablicami
# Utwórz dwie tablice 3×3:

# A = wartości od 1 do 9,

# B = wartości od 9 do 1.

# Oblicz:

# element-wise iloczyn,

# dot product (macierzowy),

# czy są równe (element-wise porównanie).

# arr1 = np.array(np.arange(1,10)).reshape((3,3))
# arr2 = np.array(np.arange(9,0,-1)).reshape((3.3))
# elementWise = arr1 * arr2
# dotProduct = np.dot(arr1,arr2) # arr @ arr
# isEqual = np.equal(arr1,arr2) # A == B (porównanie)
# print(isEqual)

# 📌 Zadanie 5: Rzutowanie i reshape
# Utwórz tablicę 3D o kształcie (2, 3, 4) z kolejnymi liczbami od 0.
# Wykonaj:

# zamianę jej w 2D (kształt: 6×4),

# zamianę jej w 1D,

# odtwórz z powrotem do (2, 3, 4).
# count = 2*3*4
# print(count)
# arr = np.array(np.arange(0,24)).reshape((2,3,4))
# arr = arr.reshape(6,4)
# arr = arr.flatten()
# arr = arr.reshape((2,3,4))


# 📌 Zadanie 6: Największa wartość w każdym kanale
# Stwórz tablicę 3D o kształcie (4, 4, 3) reprezentującą 4×4 obraz RGB.
# Dla każdego piksela wybierz maksymalny kanał (np. max z R, G, B).
# Wynik: nowa 2D tablica 4×4 z wartościami maksymalnymi.

#nie wiem


#📌 Zadanie 7: Tablica o strukturze szachownicy
# Utwórz 8×8 tablicę NumPy z naprzemiennymi 0 i 1 jak szachownica.
# arrayOfZeroes = np.zeros((8,8))

# arrayOfZeroes[1::2,::2] = 1
# arrayOfZeroes[::2,1::2] = 1

# print(arrayOfZeroes)


# 📌 Zadanie 8: Indeksowanie zaawansowane
# Masz tablicę 5×5 z losowymi wartościami.
# Wypisz:

# przekątną główną,

# wartości z drugiego i czwartego wiersza,

# elementy z indeksami (0,1), (2,2), (4,4).

# randArray = np.array(np.random.randint(0,100,25)).reshape(5,5)
# print(randArray)
# #diagonal
# diagonal = np.diag(randArray)

# secondAndFourthRow = randArray[[1,3],:]


# #elementswithindicies

# elements = randArray[[0,2,4],[1,2,4]]
# print(elements)


# Masz tablicę A o kształcie (4,4) oraz wektor B długości 4.
# Dodaj wektor B do każdej kolumny A (broadcasting po wierszach).


# arrayX = np.array(np.random.randint(0,100,16)).reshape((4,4))
# wektorB = np.array(np.random.randint(0,100,4))

# addiction = arrayX + wektorB


# 📌 Zadanie 10: Filtr przestrzenny (2D)
# Masz tablicę 6×6 z losowymi wartościami.
# Wytnij z niej wszystkie możliwe okna 3×3 (bez paddingu) – ile będzie takich okien?
# Z każdego okna oblicz średnią. Wynik: nowa tablica.

arr = np.random.rand(6,6)
result =[]

for i in range(4):
    for j in range(4):
        window = arr[i:i+3,j:j+3]
        result.append(window.mean())

final = np.array(result).reshape(4,4)
print(final)