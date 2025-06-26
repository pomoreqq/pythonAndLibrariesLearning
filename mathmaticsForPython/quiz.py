# 📘 Quiz – Sekcja: Matematyka w Pythonie (64–74)

# 1. Czym jest macierz i jak można ją zapisać w Pythonie bez użycia bibliotek?
    #macierz jest prosokatna przestrzenia numerow,symbolow,ekspresji ktore sa uporzadkowane w kolumny i wiersze
        #1d = matrix1d = [1,2,3,4] , matrix2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 2. Podaj przykład macierzy 2x3 zapisanej jako lista list w Pythonie.
        #2d 2x3 mat = [[1,2,3],[4,5,6]]
# 3. Czym różni się skalar od wektora?
    #skalar to jest pojedyncza liczba,ekspresja,symbol a wektor ma tez kierunek
# 4. Czym jest wektor kolumnowy i jak go przedstawić w Pythonie?
    #1d vector = [[1],[2],[3],[4]]. wektor kolumny to macierz z jedna kolumna ma shape n x 1
# 5. Co się stanie, jeśli spróbujesz dodać dwie macierze o różnych rozmiarach?
    # niemozliwe jest dodanie macierzy o dwoch roznych rozmiarach
# 6. Napisz funkcję, która dodaje dwie macierze o takich samych wymiarach.
        #def add_matrices(A, B):
    # result = []
    # for i in range(len(A)):
    #     row = []
    #     for j in range(len(A[0])):
    #         row.append(A[i][j] + B[i][j])
    #     result.append(row)
    # return result
# 7. Czym jest tensor i jak różni się od macierzy?
    #jest to wielowymiarowy obiekt tym sie rozni od macierzy
# 8. Zapisz przykład tensora 2x2x2 w Pythonie.
        # nie wiem jak
# 9. Na czym polega transpozycja macierzy? Podaj przykład.
    #polega na zamianie wierszy z kolumnami
        # [1,2,3   [1  4  7
        #  4,5,6 =  2   5   8
        #   7,8,9]   3  6   9]
# 10. Napisz funkcję, która dokonuje transpozycji dowolnej macierzy (lista list).
    #def transpose(matrix):
    #return [list(row) for row in zip(*matrix)]
# 11. Na jakich warunkach można wykonać mnożenie macierzy?
        # jesli liczba kolumn pierwszej rowna sie liczbie wierszy drugiej
# 12. Co oznacza operacja iloczynu skalarnego (dot product) dla dwóch wektorów?
                # jest to mnozenie skalarow
# 13. Podaj przykład dwóch wektorów i oblicz ich iloczyn skalarny.
        # def dot_product(v1, v2):
    #return sum(a * b for a, b in zip(v1, v2))
# 14. Jakie wymiary będzie miała wynikowa macierz po mnożeniu 2x3 i 3x2?
    # 2x2
# 15. Dlaczego kolejność mnożenia macierzy ma znaczenie?
    # bo mnozenie nie jest naprzemienne
# 16. Co oznacza wynik 0 w iloczynie skalarnym dwóch wektorów?
        # nie wiem
# 17. Co oznacza błąd „ValueError” przy mnożeniu macierzy?
        # ze typy danych sie nie zgadzaja
# 18. Podaj przykład sytuacji biznesowej, gdzie przyda się mnożenie macierzy.
        # kalkulacja kosztow kampanii marketingowe 
# 19. Jak obliczyć średni koszt jednego kliknięcia na podstawie kosztu i liczby kliknięć?
        # pytanie nie z tego zakresu ale poprostu podzielic sredni koszt przez srednie klikniecie
# 20. Dlaczego warto znać podstawy algebry liniowej programując w Pythonie?
    # bo biblioteki np numpy opiera sie na algebrze liniowej
# 💡 Pytania opracowane wyłącznie w oparciu o sekcję „Mathematics for Python” – bez NumPy.
