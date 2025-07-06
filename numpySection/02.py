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

#nie wiem wytlumacz
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

arr1 = np.array(np.arange(1,10))
arr2 = np.array(np.arange(9,0,-1))
elementWise = arr1 * arr2
dotProduct = np.dot(arr1,arr2)
isEqual = np.equal(arr1,arr2)
print(isEqual)